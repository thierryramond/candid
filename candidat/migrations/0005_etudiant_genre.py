# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidat', '0004_auto_20150525_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='etudiant',
            name='genre',
            field=models.CharField(null=True, db_column='genre', max_length=25, blank=True),
        ),
    ]
