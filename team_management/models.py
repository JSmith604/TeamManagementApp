from django.db import models

class TeamMember(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    ROLE_CHOICES = [
        ('REG', 'Regular'),
        ('ADM', 'Admin'),
    ]
    role = models.CharField(max_length=3, choices=ROLE_CHOICES, default='REG')
