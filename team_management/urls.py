
from django.urls import path
from .views import home_view, TeamMemberListView, TeamMemberCreateView

urlpatterns = [
    path('', home_view, name='home'),  
    path('team/', TeamMemberListView.as_view(), name='team_member_list'),
    path('team/add/', TeamMemberCreateView.as_view(), name='team_member_add'),
]
