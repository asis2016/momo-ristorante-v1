# Generated by Django 3.2 on 2021-04-29 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('excerpt', models.CharField(blank=True, max_length=50)),
                ('content', models.TextField(blank=True)),
                ('create_date', models.DateField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('image_url', models.CharField(blank=True, max_length=20)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
