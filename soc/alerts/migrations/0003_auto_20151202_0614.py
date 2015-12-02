# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0002_disease'),
    ]

    operations = [
        migrations.CreateModel(
            name='Affliction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=30)),
                ('disease', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='disease',
            name='id',
        ),
        migrations.RemoveField(
            model_name='disease',
            name='user',
        ),
        migrations.AddField(
            model_name='disease',
            name='aqi',
            field=models.IntegerField(default=0, max_length=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='disease',
            name='disease',
            field=models.CharField(max_length=30, serialize=False, primary_key=True),
        ),
    ]
