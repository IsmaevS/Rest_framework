from django.contrib.auth.models import User
from django.db import models


class Status(models.Model):
    STATUS = [
        ('new', 'New'),
        ('in progress', 'In progress'),
        ('done', 'Done')
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    solution = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS, default='new')
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title