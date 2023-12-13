
from django.urls import path
from .views import home_view, TeamMemberListView, TeamMemberCreateView, TeamMemberUpdateView, TeamMemberDeleteView

urlpatterns = [
    path('', home_view, name='home'),  
    path('team/', TeamMemberListView.as_view(), name='team_member_list'),
    path('team/add/', TeamMemberCreateView.as_view(), name='team_member_add'),
    path('team/edit/<int:pk>/', TeamMemberUpdateView.as_view(), name='team_member_edit'),
    path('team/delete/<int:pk>/', TeamMemberDeleteView.as_view(), name='team_member_delete'),
]
