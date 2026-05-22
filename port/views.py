from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
# Create your views here
def home(request):
  return render(request,'index.html')
def contact(request):
  if request.method=="POST":
    name=request.POST.get('name')
    email=request.POST.get('email')
    message=request.POST.get('message')

    full_message= f"""
    Name:{name}
    Email:{email}

    Message:
    {message}
    """
    send_mail(
      subject='New portfolio message',
      message=full_message,
      from_email=settings.EMAIL_HOST_USER,
      recipient_list=['tejasmaheshdl@gmail.com'],
      fail_silently=False,
    )
    return redirect('/')
  return render(request,'index.html')
