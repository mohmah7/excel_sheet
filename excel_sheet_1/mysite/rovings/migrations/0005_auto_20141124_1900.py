# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rovings', '0004_auto_20141124_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='admission_date',
            field=models.DateField(default=datetime.date(2014, 11, 24), verbose_name=b'Admission Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='app_doctor',
            field=models.CharField(default=b'Dr. Mohamed Mahmoud', max_length=20),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patient',
            name='benefit_lower_limit',
            field=models.CharField(default=b'Nil', max_length=15),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patient',
            name='benefit_upper_limit',
            field=models.CharField(default=b'Nil', max_length=15),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patient',
            name='benifit',
            field=models.CharField(default=b'Nil', max_length=15),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patient',
            name='discharge_date',
            field=models.DateField(default=datetime.date(2014, 11, 24), verbose_name=b'Discharge Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='initiator',
            field=models.CharField(default=b'RC UP', max_length=20),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patient',
            name='justified',
            field=models.CharField(default=datetime.date(2014, 11, 24), max_length=15, choices=[(b'JS', b'Justified'), (b'UNJ', b'UnJusitfied')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='notes',
            field=models.TextField(default=datetime.date(2014, 11, 24), max_length=2000, blank=True),
            preserve_default=False,
        ),
    ]
