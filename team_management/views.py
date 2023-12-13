
from django.views.generic import ListView, CreateView
from django.shortcuts import render
from .models import TeamMember
from .forms import TeamMemberForm 
from django.urls import reverse_lazy

class TeamMemberListView(ListView):
    model = TeamMember
    template_name = 'team_management/team_member_list.html'

class TeamMemberCreateView(CreateView):
    form_class = TeamMemberForm
    template_name = 'team_management/team_member_form.html'
    success_url = reverse_lazy('team_member_list')  

def home_view(request):
    context = {}
    return render(request, 'team_management/home.html', context)