from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request,'login.html')

def signup_view(request):
    return render(request,'signup.html')

def home_view(request):
    return render(request,'index.html')

def howitworks_view(request):
    return render(request,'howitworks.html')

def for_clients_view(request):
    return render(request,'forclients.html')

def browse_job_view(request):
    return render(request, 'browsejob.html')

def for_freelancer_view(request):
    return render(request, 'forfreelancer.html')