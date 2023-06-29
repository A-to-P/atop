# Generated by Django 4.2.2 on 2023-06-29 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('consulting', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='content',
            new_name='comment',
        ),
        migrations.AddField(
            model_name='consulting',
            name='final_report',
            field=models.FileField(null=True, upload_to='final_report'),
        ),
        migrations.CreateModel(
            name='Accusation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evidence', models.FileField(null=True, upload_to='evidence')),
                ('comment', models.TextField(blank=True, default='')),
                ('complainant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complainant', to=settings.AUTH_USER_MODEL)),
                ('defendant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='defendant', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]