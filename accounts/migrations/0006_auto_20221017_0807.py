# Generated by Django 3.2.12 on 2022-10-17 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_userimage_role'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userimage',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.AddField(
            model_name='userimage',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
