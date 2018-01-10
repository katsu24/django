# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0001_initial'),
        ('staff', '0001_initial'),
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuestSchedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date', models.DateField()),
                ('start', models.TimeField(default='00:00')),
                ('end', models.TimeField(default='00:00')),
                ('guest', models.ForeignKey(unique_for_date='date', to='guest.Guest')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MonthShift',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('year', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('month', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)])),
                ('completed', models.BooleanField(default=False)),
                ('groupschedule', models.ForeignKey(to='owner.GroupSchedule')),
            ],
        ),
        migrations.CreateModel(
            name='NgShift',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StaffSchedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date', models.DateField()),
                ('leader', models.BooleanField(default=False)),
                ('phoner', models.BooleanField(default=False)),
                ('staff', models.ForeignKey(unique_for_date='date', to='staff.Staff')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WorkTime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('start', models.TimeField(default='00:00')),
                ('end', models.TimeField(default='00:00')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('simbol', models.CharField(max_length=5, unique=True)),
                ('groupschedule', models.ForeignKey(to='owner.GroupSchedule')),
            ],
        ),
        migrations.AddField(
            model_name='staffschedule',
            name='worktime',
            field=models.ForeignKey(to='schedule.WorkTime'),
        ),
        migrations.AddField(
            model_name='ngshift',
            name='ng_shift',
            field=models.ManyToManyField(to='schedule.WorkTime'),
        ),
        migrations.AddField(
            model_name='ngshift',
            name='staff',
            field=models.ForeignKey(unique_for_date='date', to='staff.Staff'),
        ),
        migrations.AlterUniqueTogether(
            name='worktime',
            unique_together=set([('groupschedule', 'simbol'), ('groupschedule', 'title')]),
        ),
        migrations.AlterUniqueTogether(
            name='monthshift',
            unique_together=set([('year', 'month', 'groupschedule')]),
        ),
    ]
