from django.db import models
from django.utils import timezone


class StudentClubsTitle(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    publish = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'description of student clubs'


class Announcement(models.Model):
    title_announcement = models.CharField(max_length=200)
    announcement_description = models.TextField(null=True)
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-publish']

    def __str__(self):
        return self.title_announcement

    class Meta:
        verbose_name_plural = 'announcements'


class About(models.Model):
    title_about = models.CharField(max_length=200)
    about_description = models.TextField(null=True)
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-publish']

    def __str__(self):
        return self.title_about

    class Meta:
        verbose_name_plural = 'about university'


class Club(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='clubs')

    def __str__(self):
        return self.name

class ClubItems(models.Model):
    name = models.CharField(max_length=255)
    history = models.TextField()
    photo_participant = models.ImageField(upload_to='participants')
    name_participant = models.TextField()
    photo_projects = models.ImageField(upload_to='project logos')
    team_project = models.TextField()
    project_description = models.TextField()
    photo = models.ImageField(upload_to='description projects')

    def __str__(self):
        return self.name
