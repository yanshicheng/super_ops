# Generated by Django 3.1.2 on 2021-08-20 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0004_auto_20210627_1713'),
        ('service_tree', '0003_delete_nodelinkserver'),
    ]

    operations = [
        migrations.CreateModel(
            name='NodeLinkClassify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='变更时间')),
                ('remark', models.CharField(blank=True, max_length=1024, null=True, verbose_name='备注')),
                ('classify', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='link_classify', to='cmdb.classify')),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service_tree.servicetree', unique=True, verbose_name='节点')),
            ],
            options={
                'verbose_name': '节点关联CMDB类型',
                'verbose_name_plural': '节点关联CMDB类型',
            },
        ),
    ]
