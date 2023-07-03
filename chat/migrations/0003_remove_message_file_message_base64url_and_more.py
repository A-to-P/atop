# Generated by Django 4.2.2 on 2023-07-03 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_message_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='file',
        ),
        migrations.AddField(
            model_name='message',
            name='base64URL',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='message',
            name='filename',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
