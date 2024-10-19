from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Status(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("statuses")

    def get_update_status_url(self):
        return reverse('update_status', args=[self.pk])

    def get_delete_status_url(self):
        return reverse('delete_status', args=[self.pk])

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("tags")

    def get_update_tag_url(self):
        return reverse('update_tag', args=[self.pk])

    def get_delete_tag_url(self):
        return reverse('delete_tag', args=[self.pk])


class Task(models.Model):
    task_name = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True)
    author = models.CharField(max_length=150)
    creator = models.ForeignKey(User, related_name='task_creator', on_delete=models.PROTECT)
    executor = models.ForeignKey(User, related_name='task_executor', on_delete=models.PROTECT)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
