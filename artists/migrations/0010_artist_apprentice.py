# Generated by Django 3.2.13 on 2022-11-28 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0009_auto_20221108_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='apprentice',
            field=models.BooleanField(default=False),
        ),
    ]
