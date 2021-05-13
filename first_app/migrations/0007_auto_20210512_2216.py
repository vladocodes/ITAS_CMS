# Generated by Django 3.2 on 2021-05-12 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0006_auto_20210512_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='uncategorized', max_length=30),
        ),
        migrations.AlterField(
            model_name='careerspost',
            name='employmentType',
            field=models.CharField(default='employment type', max_length=30),
        ),
        migrations.AlterField(
            model_name='careerspost',
            name='location',
            field=models.CharField(default='location', max_length=50),
        ),
        migrations.AlterField(
            model_name='careerspost',
            name='profession',
            field=models.CharField(default='profession', max_length=30),
        ),
    ]
