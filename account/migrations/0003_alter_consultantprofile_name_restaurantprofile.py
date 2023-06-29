# Generated by Django 4.2.2 on 2023-06-29 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_consultantprofile_college_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultantprofile',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.CreateModel(
            name='RestaurantProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('birth', models.DateField(null=True)),
                ('career', models.CharField(default='', max_length=25)),
                ('self_introducing', models.TextField(default='', max_length=500)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile/')),
                ('contact_at', models.TextField(default='', max_length=200)),
                ('location', models.CharField(default='', max_length=25)),
                ('menu', models.CharField(default='', max_length=25)),
                ('area', models.CharField(default='', max_length=25)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'restaurant_profile',
            },
        ),
    ]