# Generated by Django 4.0 on 2022-01-04 10:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0006_alter_studentclubstitle_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_about', models.CharField(max_length=200)),
                ('about_description', models.TextField(null=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-publish'],
            },
        ),
        migrations.AlterModelOptions(
            name='announcement',
            options={'ordering': ['-publish']},
        ),
        migrations.RenameField(
            model_name='announcement',
            old_name='title',
            new_name='title_announcement',
        ),
    ]