# Generated by Django 3.2.13 on 2022-12-15 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0013_artist_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='order',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
