# Generated by Django 2.2.13 on 2021-06-04 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='post',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]
