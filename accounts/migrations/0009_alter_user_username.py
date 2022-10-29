# Generated by Django 3.2.12 on 2022-10-19 16:05

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20221019_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, help_text='Required. 150 characters or fewer. Usernames may contain alphanumeric, _, @, +, . and - characters.', max_length=191, null=True, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()]),
        ),
    ]
