# Generated by Django 3.1.7 on 2022-08-09 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0002_auto_20220731_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='head_shot',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
