# Generated by Django 3.2.8 on 2021-11-10 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20211110_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='date_published',
            field=models.DateTimeField(verbose_name='Date published'),
        ),
        migrations.AlterField(
            model_name='question',
            name='date_published',
            field=models.DateTimeField(verbose_name='Date published'),
        ),
    ]
