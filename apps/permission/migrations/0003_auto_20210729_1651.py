# Generated by Django 3.1.2 on 2021-07-29 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permission', '0002_auto_20210711_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='component',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='视图路径'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='icon',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='图标名'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='路由名'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='order',
            field=models.IntegerField(default=1, verbose_name='子菜单排序'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='menu',
            name='role',
            field=models.ManyToManyField(blank=True, null=True, to='permission.Role', verbose_name='权限角色'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='title',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='名称'),
        ),
    ]
