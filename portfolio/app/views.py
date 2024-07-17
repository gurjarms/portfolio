from django.shortcuts import render,redirect
from django.http import JsonResponse

from django.views.generic import TemplateView
from .forms import contactFrom
from django.views.decorators.csrf import csrf_exempt
from django.core import mail
from django.conf import settings



# Create your views here.


# class Index(TemplateView):
#     template_name = "index.html"

def index(request):
    form = contactFrom()
    return render(request, 'index.html',{'form':form})

@csrf_exempt
def contact(request):
    if request.method == "POST":
        form = contactFrom(request.POST)

        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        if form.is_valid(): 

            form.save()
        msg = f'''Feedback from: {name}
Subject: {subject}
User contact: {email}

{message}
                  '''
        to_email = 'gurjarmahisingh33@gmail.com'
        try:
            sending = mail.send_mail('Feedback from Portfolio', msg, settings.EMAIL_HOST_USER, [to_email], fail_silently=False)
        except:
            ...

        if form.is_valid():

            form.save()

    # return JsonResponse(data,safe=False)
    return redirect(index)
