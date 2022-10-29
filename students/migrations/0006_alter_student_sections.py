# Generated by Django 3.2.12 on 2022-10-25 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0008_branch_location'),
        ('students', '0005_alter_student_sections'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='sections',
            field=models.ManyToManyField(blank=True, null=True, to='academy.Section'),
        ),
    ]