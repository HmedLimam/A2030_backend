# Generated by Django 5.0.3 on 2024-04-24 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0009_alter_score_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delegate',
            name='aiesecer',
        ),
        migrations.AddField(
            model_name='delegate',
            name='aiesecEmail',
            field=models.EmailField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='delegate',
            name='typeOfDelegate',
            field=models.CharField(max_length=255, null=True),
        ),
    ]