# Generated by Django 3.2.12 on 2022-10-18 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20221018_0740'),
        ('blog', '0012_auto_20221018_0740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='comments',
            field=models.ManyToManyField(blank=True, to='home.Comment'),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
