# Generated by Django 5.0.3 on 2024-03-20 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_alter_delegate_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delegate',
            name='fullname',
        ),
    ]
