# Generated by Django 3.2.12 on 2022-10-26 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flatpages', '0001_initial'),
        ('main', '0005_auto_20221026_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='flat_page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='flatpages.flatpage'),
        ),
        migrations.AddField(
            model_name='corevalues',
            name='flat_page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='flatpages.flatpage'),
        ),
        migrations.AddField(
            model_name='emailaddress',
            name='flat_page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='flatpages.flatpage'),
        ),
        migrations.AddField(
            model_name='file',
            name='flat_page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='flatpages.flatpage'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='flat_page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='flatpages.flatpage'),
        ),
        migrations.AddField(
            model_name='generalsetting',
            name='flat_page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='flatpages.flatpage'),
        ),
        migrations.AddField(
            model_name='image',
            name='flat_page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='flatpages.flatpage'),
        ),
        migrations.AddField(
            model_name='phonenumber',
            name='flat_page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='flatpages.flatpage'),
        ),
        migrations.AddField(
            model_name='socialnetwork',
            name='flat_page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='flatpages.flatpage'),
        ),
        migrations.AddField(
            model_name='team',
            name='flat_page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='flatpages.flatpage'),
        ),
    ]
