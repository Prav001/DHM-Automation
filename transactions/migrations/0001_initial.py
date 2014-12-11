# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TranStats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('BPC', models.CharField(max_length=200)),
                ('tran_date', models.DateField()),
                ('tran_desc', models.CharField(max_length=800)),
                ('status', models.CharField(max_length=200)),
                ('count', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Transactions Statistics',
            },
            bases=(models.Model,),
        ),
    ]
