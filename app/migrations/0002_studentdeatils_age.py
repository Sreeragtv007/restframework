# Generated by Django 5.0 on 2023-12-14 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdeatils',
            name='age',
            field=models.TextField(blank=True, null=True),
        ),
    ]