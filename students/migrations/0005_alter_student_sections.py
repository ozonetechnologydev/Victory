# Generated by Django 3.2.12 on 2022-10-20 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0007_alter_department_options'),
        ('students', '0004_alter_student_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='sections',
            field=models.ManyToManyField(blank=True, to='academy.Section'),
        ),
    ]
