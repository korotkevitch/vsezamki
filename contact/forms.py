from django import forms
from captcha.fields import ReCaptchaField
from django.core.mail import send_mail as django_send_mail
from django.forms import ModelForm
from .models import ContactForm


class UserForm(ModelForm):
    # captcha = ReCaptchaField(
    #     public_key='6LdbmQkeAAAAADPuywAjtXN4u-Pd31SfkXBUAHxm',
    #     private_key='6LdbmQkeAAAAAN2ZnJ3-PPe3VkZzScSbyd3AVjKm',
    # )

    class Meta:
        model = ContactForm
        fields = '__all__'  # вместо перечисления всех полей: fields = ['name', 'phone', 'message']

    def send_mail(self):
        return django_send_mail('Сообщение с сайта vsezamki.by',
                    str('Имя: ') + self.cleaned_data['name'] + '\n' + str('Емейл: ') + self.cleaned_data['email'] + '\n' + str('Телефон: ') + self.cleaned_data['phone'] + '\n' + str('Сообщение: ') + self.cleaned_data['message'],
                    'no-reply@iko-studio.com',
                    ['info@iko-studio.com'])
