# Generated by Django 3.2.12 on 2022-10-14 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_blog_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='coped_from',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.blog'),
        ),
    ]
