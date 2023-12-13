
from django.views.generic import ListView
from django.shortcuts import render
from .models import TeamMember
from django.urls import reverse_lazy

class TeamMemberListView(ListView):
    model = TeamMember
    template_name = 'team_management/team_member_list.html'

def home_view(request):
    context = {}
    return render(request, 'team_management/home.html', context)