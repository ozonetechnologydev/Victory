# Generated by Django 3.2.12 on 2022-10-18 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='cover_image',
        ),
        migrations.AddField(
            model_name='branch',
            name='cover_image',
            field=models.ImageField(blank=True, default='academy/cover_image.jpg', null=True, upload_to='academy/cover_image'),
        ),
        migrations.RemoveField(
            model_name='department',
            name='cover_image',
        ),
        migrations.AddField(
            model_name='department',
            name='cover_image',
            field=models.ImageField(blank=True, default='/cover_image.png', null=True, upload_to='accdemy/cover_image'),
        ),
        migrations.RemoveField(
            model_name='section',
            name='cover_image',
        ),
        migrations.AddField(
            model_name='section',
            name='cover_image',
            field=models.ImageField(blank=True, default='/cover_image.png', null=True, upload_to='accdemy/cover_image'),
        ),
        migrations.RemoveField(
            model_name='subject',
            name='cover_image',
        ),
        migrations.AddField(
            model_name='subject',
            name='cover_image',
            field=models.ImageField(blank=True, default='/cover_image.png', null=True, upload_to='accdemy/cover_image'),
        ),
    ]