
from django.test import TestCase, Client
from django.urls import reverse
from .models import TeamMember
from django.contrib.messages.storage.fallback import FallbackStorage

class TeamMemberTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('team_member_list')
        TeamMember.objects.create(
            first_name='John',
            last_name='Doe',
            phone_number='1234567890',
            email='john.doe@example.com',
            role='REG'
        )

    def test_team_member_list_GET(self):
        
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'team_management/team_member_list.html')
        self.assertContains(response, 'John Doe') 

    def test_team_member_add_POST(self):
        
        add_url = reverse('team_member_add')

        new_member_data = {
            'first_name': 'Jane',
            'last_name': 'Smith',
            'phone_number': '0987654321',
            'email': 'jane.smith@example.com',
            'role': 'REG'
        }

        response = self.client.post(add_url, new_member_data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(TeamMember.objects.count(), 2)
        new_member = TeamMember.objects.get(email='jane.smith@example.com')
        self.assertEqual(new_member.first_name, 'Jane')
        self.assertEqual(new_member.last_name, 'Smith')
        self.assertRedirects(response, self.list_url)


