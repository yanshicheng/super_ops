# Generated by Django 3.1.2 on 2021-08-05 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permission', '0007_auto_20210805_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='method',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='请求方法'),
        ),
        migrations.AlterField(
            model_name='rule',
            name='path',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='api路径'),
        ),
    ]
