# Generated by Django 4.0 on 2022-01-04 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0012_club'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClubItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('history', models.TextField()),
                ('photo_participant', models.ImageField(upload_to='participants')),
                ('name_participant', models.TextField()),
                ('photo_projects', models.ImageField(upload_to='project logos')),
                ('team_project', models.TextField()),
                ('project_description', models.TextField()),
                ('photo', models.ImageField(upload_to='description projects')),
            ],
        ),
    ]
