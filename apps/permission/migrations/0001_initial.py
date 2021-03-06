# Generated by Django 3.1.2 on 2021-07-11 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RuleClassify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='变更时间')),
                ('remark', models.CharField(blank=True, max_length=1024, null=True, verbose_name='备注')),
                ('name', models.CharField(help_text='分类名', max_length=120, unique=True, verbose_name='名称')),
            ],
            options={
                'verbose_name': '角色',
                'verbose_name_plural': '角色',
                'db_table': 'rule_classify',
                'unique_together': {('name',)},
            },
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='变更时间')),
                ('remark', models.CharField(blank=True, max_length=1024, null=True, verbose_name='备注')),
                ('name', models.CharField(help_text='名称', max_length=256, verbose_name='名称')),
                ('path', models.CharField(max_length=128, unique=True, verbose_name='api路径')),
                ('method', models.CharField(max_length=128, verbose_name='请求方法')),
                ('rule_classify', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='permission.ruleclassify')),
            ],
            options={
                'verbose_name': '权限规则',
                'verbose_name_plural': '权限规则',
                'db_table': 'role_rules',
                'unique_together': {('name', 'path', 'method')},
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='变更时间')),
                ('remark', models.CharField(blank=True, max_length=1024, null=True, verbose_name='备注')),
                ('name', models.CharField(help_text='名称', max_length=128, unique=True, verbose_name='名称')),
                ('rule', models.ManyToManyField(blank=True, related_name='role', to='permission.Rule', verbose_name='规则')),
            ],
            options={
                'verbose_name': '角色',
                'verbose_name_plural': '角色',
                'db_table': 'role',
                'unique_together': {('name',)},
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='变更时间')),
                ('remark', models.CharField(blank=True, max_length=1024, null=True, verbose_name='备注')),
                ('order', models.IntegerField(blank=True, null=True, verbose_name='子菜单排序')),
                ('path', models.CharField(max_length=64, verbose_name='路由路径')),
                ('component', models.CharField(max_length=128, verbose_name='视图路径')),
                ('name', models.CharField(max_length=32, verbose_name='路由名')),
                ('title', models.CharField(max_length=32, verbose_name='名称')),
                ('icon', models.CharField(max_length=32, verbose_name='图标名')),
                ('redirect', models.CharField(blank=True, max_length=128, null=True, verbose_name='重定向')),
                ('active_menu', models.CharField(blank=True, max_length=128, null=True, verbose_name='详情路由')),
                ('hidden', models.BooleanField(default=False, verbose_name='隐藏')),
                ('always_show', models.BooleanField(default=True, verbose_name='显示根路由')),
                ('no_cache', models.BooleanField(default=False, verbose_name='不缓存')),
                ('breadcrumb', models.BooleanField(default=False, verbose_name='是否在面包屑显示')),
                ('affix', models.BooleanField(default=False, verbose_name='固定')),
                ('pid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='permission.menu', verbose_name='父节点')),
                ('role', models.ManyToManyField(to='permission.Role', verbose_name='权限角色')),
            ],
            options={
                'verbose_name': '菜单',
                'verbose_name_plural': '菜单',
                'db_table': 'role_menu',
            },
        ),
    ]
