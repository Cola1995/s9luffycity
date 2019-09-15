# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-09-11 11:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='章节名称')),
                ('num', models.IntegerField(verbose_name='章节')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='课程名称')),
                ('course_img', models.CharField(max_length=100, verbose_name='课程图片')),
                ('level', models.IntegerField(choices=[(1, '初级'), (2, '中级'), (3, '高级')], verbose_name='等级')),
            ],
        ),
        migrations.CreateModel(
            name='CourseDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('why', models.CharField(max_length=255, verbose_name='why')),
                ('slogon', models.CharField(max_length=255, verbose_name='口号')),
                ('course', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.Course')),
                ('recommend_course', models.ManyToManyField(related_name='rc', to='api.Course', verbose_name='推荐课程')),
            ],
        ),
        migrations.AddField(
            model_name='chapter',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Course', verbose_name='所属课程'),
        ),
    ]