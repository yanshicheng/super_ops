# Generated by Django 3.1.2 on 2021-08-22 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0004_auto_20210627_1713'),
        ('service_tree', '0005_auto_20210821_1323'),
    ]

    operations = [
        migrations.CreateModel(
            name='NodeLinkAsset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='变更时间')),
                ('remark', models.CharField(blank=True, max_length=1024, null=True, verbose_name='备注')),
                ('asset', models.ManyToManyField(blank=True, related_name='link_classify', to='cmdb.Asset')),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service_tree.servicetree', verbose_name='关联表')),
            ],
            options={
                'verbose_name': '节点关联CMDB资产',
                'verbose_name_plural': '节点关联CMDB资产',
            },
        ),
    ]
