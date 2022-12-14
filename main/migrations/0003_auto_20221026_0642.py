# Generated by Django 3.2.12 on 2022-10-26 06:42

from django.conf import settings
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoreValues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('descriptions', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EmailAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator()])),
            ],
        ),
        migrations.CreateModel(
            name='GeneralSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(help_text='Enter your website name below', max_length=200)),
                ('site_description', models.TextField(help_text='The site title might be the name of your company or organization, or a brief description of the organization, or a combination of the two.')),
                ('logo', models.ImageField(height_field=40, help_text='Upload your website logo - 120 x 40 ', upload_to='main/images', width_field=120)),
                ('favicon', models.ImageField(height_field=32, help_text='Upload your website favicon - Standard for most desktop browsers. 32×32', upload_to='main/images', width_field=32)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SocialNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='this field can be Facebook Page ID, Twitter Username, YouTube Channel Name, Instagram Username and etc', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='file',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=200)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ManyToManyField(to='main.Image')),
            ],
        ),
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('about', models.TextField(help_text='brief description of the organization, or a combination of the two.it display on about page (this field can be markdown or HTML)')),
                ('global_reach', models.TextField()),
                ('core_values', models.ManyToManyField(to='main.CoreValues')),
                ('teams', models.ManyToManyField(to='main.Team')),
            ],
        ),
    ]
