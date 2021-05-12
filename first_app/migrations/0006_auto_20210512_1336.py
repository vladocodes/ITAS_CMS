# Generated by Django 3.2 on 2021-05-12 11:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0005_careerspost'),
    ]

    operations = [
        migrations.AddField(
            model_name='careerspost',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='careerspost',
            name='employmentType',
            field=models.CharField(default='Full-Time', max_length=30),
        ),
        migrations.AddField(
            model_name='careerspost',
            name='location',
            field=models.CharField(default='Banja Luka', max_length=50),
        ),
        migrations.AddField(
            model_name='careerspost',
            name='profession',
            field=models.CharField(default='Engineer', max_length=30),
        ),
        migrations.AlterField(
            model_name='careerspost',
            name='title',
            field=models.CharField(max_length=80),
        ),
    ]
