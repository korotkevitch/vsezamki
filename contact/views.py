from django.shortcuts import render
from datetime import datetime
from django.views.generic import View, ListView
from .models import Contact, PhoneNumberField, ContactForm
from .forms import UserForm
from django.core.mail import BadHeaderError
from django.views.generic.edit import FormView
from django.core.mail import send_mail


# class ContactView(ListView):
#     model = Contact
#     template_name = 'contact.html'
#     context_object_name = 'contact' # вынесено в ContextProcessors


class ContactFormView(FormView):
    model = ContactForm
    form_class = UserForm
    template_name = 'contact.html'
    success_url = 'thanks'

    def form_valid(self, myform):
        myform.send_mail()
        myform.save()  # сохранение в БД
        return super().form_valid(myform)

