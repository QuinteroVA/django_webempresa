from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage 

# Create your views here.   
def contact(request):
    # print("Tipo de petición:{}" .format(request.method))
    # instancia
    contactForm=ContactForm()
    if request.method=="POST":
        contactForm=ContactForm(data=request.POST)
        if contactForm.is_valid():
            name=request.POST.get('name','')
            email=request.POST.get('email','')
            message=request.POST.get('message','')
            email=EmailMessage(
                "La Cafettiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name,email,message),
                "correo@inbox.mailtrap.io",
                ["aquintero@itsqmet.edu.ec"],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contact')+"?ok")
            except:
                return redirect(reverse('contact')+"?fail")
    return render(request,"contact/contact.html", {'contactForm':contactForm})