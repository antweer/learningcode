from django.template.response import TemplateResponse

def homepage (request):
  context={
    'page_title': 'Home Page',
    'name': 'John Madden',
    'numbers': [1, 2, 3, 4]
  }
  return TemplateResponse(request, 'homepage.html', context, {})

def contact(request):
  return TemplateResponse(request, 'contact.html', {})