# Generated by Django 2.2.4 on 2022-10-10 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0005_auto_20221010_1521'),
    ]

    operations = [
        migrations.RenameField(
            model_name='violaion',
            old_name='expierd_date_linsces',
            new_name='expierd_date_violation',
        ),
        migrations.RemoveField(
            model_name='violaion',
            name='relased_date_linsces',
        ),
    ]
