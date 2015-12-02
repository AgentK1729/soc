# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0003_auto_20151202_0614'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease',
            name='ozone',
            field=models.FloatField(default=0.0, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='disease',
            name='pm',
            field=models.FloatField(default=0.0, max_length=5),
            preserve_default=False,
        ),
    ]
