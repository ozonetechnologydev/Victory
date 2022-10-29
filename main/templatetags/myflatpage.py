from django import template
from django.template.defaultfilters import stringfilter

from main.models import EmailAddress, GeneralSetting, OfficeAddress, PhoneNumber, SocialNetwork

register = template.Library()

@register.simple_tag(name='syhello')
def some_function(value):
    return f"hello {value}" 

@register.simple_tag(name="general_setting")
def general_setting():
    return GeneralSetting.objects.first()
     
     
@register.simple_tag(name="phone_numbers")
def phone_numbers():
    return PhoneNumber.objects.all()

@register.simple_tag(name="email_address")
def email_address():
    return EmailAddress.objects.all()

@register.simple_tag(name="office_address")
def office_address():
    return OfficeAddress.objects.all()

@register.simple_tag(name="social_network")
def social_network():
    return SocialNetwork.objects.all()



