# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rovings', '0006_remove_diagnosis_votes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='patient',
            name='days_approved',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='patient',
            name='days_requested',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='patient',
            name='policy_number',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
