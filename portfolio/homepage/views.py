from django.template.response import TemplateResponse
from django import forms, http
from .forms import ContactForm
from django.core.mail import send_mail
  
def homepage (request):
  context={
    'page_title': 'Home Page',
    'name': 'John Madden',
    'numbers': [1, 2, 3, 4]
  }
  return TemplateResponse(request, 'homepage.html', context, {})

def thanks(request):
  return TemplateResponse(request, 'thanks.html', {})
  
def hello(request):
  form = NameForm(request.POST or None)
  
  if request.method == 'POST':
    if form.is_valid():
      send_email()
      return http.HttpResponseRedirect('/thanks/')
      
  context= {
    'form':form
  }
  return TemplateResponse(request, 'hello.html', context, {})
  
def contact_me(request):
  form  = ContactForm(request.POST or None)
  if request.method == 'POST':
    if form.is_valid():
      send_mail(
        form.cleaned_data['your_name'],
        form.cleaned_data['your_question'],
        form.cleaned_data['your_email'],
        ['trajwani@gmail.com'],
        fail_silently=False,
      )
      return http.HttpResponseRedirect('/thanks/')
  
      
  context = {
    'form':form
    }
  return TemplateResponse(request, 'contact_me.html', context)