# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidat', '0005_etudiant_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiant',
            name='date_naissance',
            field=models.DateField(null=True, blank=True, db_column='date_naissance'),
        ),
    ]
