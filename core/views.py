from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import CreateView
from .forms import CreatePersonForm
from django.urls import reverse_lazy
from .models import Town, State

class CreatePersonView(CreateView):
    form_class = CreatePersonForm
    template_name = 'core/create_person.html'

    def get_success_url(self):
        return reverse_lazy('create_person')

def load_towns(request):
    state_id = request.POST.get('sid')
    state = State.objects.get(id=state_id)
    towns = list(state.town_set.values('pk', 'name'))
    return JsonResponse({'data': towns})
    