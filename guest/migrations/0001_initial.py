# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=40)),
                ('groupschedule', models.ForeignKey(to='owner.GroupSchedule')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='guest',
            unique_together=set([('name', 'groupschedule')]),
        ),
    ]
