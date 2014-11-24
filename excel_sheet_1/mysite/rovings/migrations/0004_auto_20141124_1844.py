# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rovings', '0003_auto_20141124_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='hospital_name',
            field=models.CharField(max_length=100, choices=[(b'ASTOON', b'Astoon'), (b'AL DOSSARY', b'AlDossary'), (b'FAKHRY', b'Fakhry'), (b'AL MANA', b'Al Mana'), (b'AL YOUSEF', b'Al Yousef'), (b'AL SALAMA', b'Al Salama')]),
        ),
    ]
