# Generated by Django 3.1.2 on 2021-08-05 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permission', '0005_auto_20210729_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='name',
            field=models.CharField(help_text='名称', max_length=64, verbose_name='名称'),
        ),
        migrations.AlterField(
            model_name='rule',
            name='path',
            field=models.CharField(max_length=128, verbose_name='api路径'),
        ),
    ]