# Generated by Django 4.1 on 2022-09-30 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_img',
            new_name='img',
        ),
    ]