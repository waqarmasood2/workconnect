# accounts/middleware.py
import time
from django.utils import timezone
from .models import Visitor

class VisitorTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        
        # Ensure session exists before processing
        if not hasattr(request, 'session') or not request.session.session_key:
            request.session.save()  # Creates session if it doesn't exist
        
        response = self.get_response(request)
        duration = time.time() - start_time
        
        # Skip admin and static files
        if request.path.startswith(('/admin', '/static', '/media')):
            return response
        
        # Get client IP (handles proxies)
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        ip_address = x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')
        
        # Save visitor data
        Visitor.objects.create(
            user=request.user if request.user.is_authenticated else None,
            session_key=request.session.session_key,
            ip_address=ip_address,
            user_agent=request.META.get('HTTP_USER_AGENT', ''),
            path=request.path,
            method=request.method,
            duration=duration
        )
        
        return response