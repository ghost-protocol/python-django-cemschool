# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-24 03:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('whooping_cough', models.DateTimeField()),
                ('diphteria', models.DateTimeField()),
                ('tetanus', models.DateTimeField()),
                ('measels', models.DateTimeField()),
                ('medical_officer_remarks', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('MR', 'MR'), ('MRS', 'MRS'), ('MISS', 'MISS'), ('DR', 'DR')], max_length=10)),
                ('relationship', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('othername', models.CharField(blank=True, max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('residence', models.CharField(max_length=100)),
                ('occupation', models.CharField(max_length=100)),
                ('education_level', models.CharField(max_length=100)),
                ('children_home', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('othername', models.CharField(blank=True, max_length=100)),
                ('dateofbirth', models.DateTimeField(default=datetime.datetime.now)),
                ('hometown', models.CharField(max_length=100)),
                ('date_admission', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.AddField(
            model_name='parent',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Student'),
        ),
        migrations.AddField(
            model_name='medical',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Student'),
        ),
    ]
