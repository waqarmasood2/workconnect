from django.shortcuts import render

# Create your views here.
# views.py
from django.views.generic import TemplateView

class AdminDashboardView(TemplateView):
    template_name = 'wcadmin/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_activities'] = [
            {
                'icon': 'user-plus',
                'message': 'New freelancer "JohnDoe" registered',
                'timestamp': '2 minutes ago'
            },
            {
                'icon': 'file-signature',
                'message': 'Project "Website Redesign" started',
                'timestamp': '1 hour ago'
            },
            {
                'icon': 'check-circle',
                'message': 'Payment completed for project #1234',
                'timestamp': '3 hours ago'
            }
        ]
        return context