# Generated by Django 3.2.12 on 2022-10-25 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0009_auto_20221025_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='it_is_full',
            field=models.BooleanField(default=False),
        ),
    ]