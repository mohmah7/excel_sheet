# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rovings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='patient',
            name='app_number',
            field=models.CharField(default=None, max_length=20),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patient',
            name='visit_date',
            field=models.DateField(default=datetime.date(2014, 11, 24), verbose_name=b'date visited'),
            preserve_default=False,
        ),
    ]
