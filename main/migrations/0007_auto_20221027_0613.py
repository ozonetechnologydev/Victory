# Generated by Django 3.2.12 on 2022-10-27 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20221026_1500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutus',
            name='flat_page',
        ),
        migrations.RemoveField(
            model_name='corevalues',
            name='flat_page',
        ),
        migrations.RemoveField(
            model_name='emailaddress',
            name='flat_page',
        ),
        migrations.RemoveField(
            model_name='file',
            name='flat_page',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='flat_page',
        ),
        migrations.RemoveField(
            model_name='generalsetting',
            name='flat_page',
        ),
        migrations.RemoveField(
            model_name='image',
            name='flat_page',
        ),
        migrations.RemoveField(
            model_name='phonenumber',
            name='flat_page',
        ),
        migrations.RemoveField(
            model_name='socialnetwork',
            name='flat_page',
        ),
        migrations.RemoveField(
            model_name='team',
            name='flat_page',
        ),
    ]
