# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0004_auto_20151202_0621'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='affliction',
            unique_together=set([('user', 'disease')]),
        ),
    ]
