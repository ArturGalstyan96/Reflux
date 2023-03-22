from django.shortcuts import render, redirect
# from.models import*
from .models import (UserInfo, AboutMe, 
                     Content, Skill, 
                     Prof, Image, 
                     Work, Contact)

from .forms import ContactForm
# Create your views here.

def home(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message= request.POST.get('message')

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = ContactForm()

    myUser = UserInfo.objects.all()[0]
    about = AboutMe.objects.all()[0]
    content1 = Content.objects.all()[0]
    content2 = Content.objects.all()[1]
    skill1 = Skill.objects.all()[0]
    prof_list = Prof.objects.all()
    image = Image.objects.all()
    work = Work.objects.all()[0]


    return render(request, 'main/index.html', context={
        'myUser': myUser,
        'AboutMe': about,
        'content1': content1,
        'content2': content2,
        'skill1': skill1,
        'prof_list': prof_list,
        'image': image,
        'work': work,
        'form': form,
        'name': name,
        'email': email,
        'subject': subject,
        'message': message
    })
