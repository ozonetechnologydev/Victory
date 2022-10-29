# Generated by Django 3.2.12 on 2022-10-18 08:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20221018_0740'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created']},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['-created']},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='contact',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]