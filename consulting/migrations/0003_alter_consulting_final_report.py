# Generated by Django 4.2.2 on 2023-06-29 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0002_rename_content_review_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulting',
            name='final_report',
            field=models.FileField(blank=True, null=True, upload_to='final_report'),
        ),
    ]