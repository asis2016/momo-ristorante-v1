# Generated by Django 3.2 on 2021-06-05 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image_url',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
