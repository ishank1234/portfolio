from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail as sm
# Create your views here.
from .models import *

def home(request):

    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        text=request.POST.get('text')
        data=Info(name=name,email=email,text=text)
        data.save()
        res = sm(
        subject = 'Thank You '+name+' for showing interest in my portfolio, Ishank Chopra',
        message = 'I Ishank Chopra, so much delighted to have your message and I will contact you back through your Gmail. Thank You so much for giving your valuable time.\nThanks and Regards \n Ishank Chopra\n7985676179',
        from_email = 'ishu.ishank1411@gmail.com',
        recipient_list = [email],
        fail_silently=False,
        )
        r = sm(
        subject = 'Update in Portfolio databse by: '+name,
        message = text+'\n'+email,
        from_email = 'ishu.ishank1411@gmail.com',
        recipient_list = ['chopra.ishank1411@gmail.com'],
        fail_silently=False,
        )

        return render(request,'home.html',{'name':'Thank You '+name+' for showing your interst in me. One mail is sent to your email id for conformation.'})
    return render(request,'home.html')
