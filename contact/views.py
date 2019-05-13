from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import  ContactForm

# Create your views here.

def contact(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Enviamos el correo y redireccionamos
            email = EmailMessage(
                "La Caffetiera: nuevo mensaje de contacto",
                "De: {0} <{1}>\n\nEscribió:\n\n{2}".format(name, email, content),
                "acortes.8@zoho.com",
                ["f8abrahan@gmail.com"],
                reply_to=[email],
                headers={'Content-Type':'text/plain'},
            )
            try:
                email.send()
                # Todo ha ido bien
                return redirect(reverse('contact')+"?ok")
            except:
                # Algo no ha ido bien redireccionamos a FAIL
                return redirect(reverse('contact')+"?FAIL")
    return render(request, "contact/contact.html", {'form':contact_form})
