# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PollutantionData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=5)),
                ('date', models.DateField()),
                ('DAILY_AQI_VALUE', models.IntegerField(max_length=2)),
                ('COUNTY_CODE', models.IntegerField(max_length=2)),
                ('COUNTY', models.IntegerField(max_length=2)),
                ('SITE_LATITUDE', models.FloatField(max_length=5)),
                ('SITE_LONGITUDE', models.FloatField(max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
