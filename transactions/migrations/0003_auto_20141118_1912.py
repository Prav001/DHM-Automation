# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_auto_20141112_1808'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='transtats',
            table='cust_tran_stats_tbl',
        ),
    ]
