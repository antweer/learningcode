from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404
from django import forms

from poll.models import Poll, Choice

def poll_page (request, poll_slug):
  poll = get_object_or_404(Poll, slug=poll_slug)
  poll_choices = list(Choice.objects.filter(poll=poll))
  answer = poll_choices[0].cleaned_data["Choice"]
  
  vote_form = forms.ChoiceField(choices = poll_choices, widget=forms.RadioSelect)
  if request.method == 'POST':
    vote = vote_form
    #upvote = poll_choices.filter(answer=vote)
    vote_form.vote += 1
    upvote.vote.save()
    return http.HttpResponseRedirect('.../.../')
    
  context = {
    'poll': poll,
    'choices': poll_choices,
    'vote_form': vote_form,
  }
  return TemplateResponse(request, 'poll.html', context)


