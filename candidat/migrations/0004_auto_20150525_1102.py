# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidat', '0003_auto_20150524_2259'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('formation', models.CharField(blank=True, max_length=100, null=True, db_column='Formation')),
                ('etablissement', models.CharField(blank=True, max_length=100, null=True, db_column='Etablissement')),
                ('millesime', models.CharField(blank=True, max_length=15, null=True, db_column='Millesime')),
            ],
        ),
        migrations.CreateModel(
            name='Cursus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('Annee', models.ForeignKey(to='candidat.Annee')),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.IntegerField(db_column='Id', serialize=False, primary_key=True)),
                ('nom', models.CharField(blank=True, max_length=25, null=True, db_column='Nom')),
                ('prenom', models.CharField(blank=True, max_length=28, null=True, db_column='Prenom')),
                ('date_naissance', models.IntegerField(blank=True, db_column='date_naissance', null=True)),
                ('adresse', models.CharField(blank=True, max_length=100, null=True, db_column='adresse')),
                ('email', models.EmailField(blank=True, unique=True, max_length=254, null=True, db_column='email')),
            ],
        ),
        migrations.CreateModel(
            name='Ncandidature',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('millesime', models.CharField(blank=True, max_length=9, null=True, db_column='Millesime')),
                ('formation', models.CharField(blank=True, max_length=30, null=True, db_column='Formation')),
                ('reponse', models.CharField(blank=True, max_length=10, null=True, db_column='Reponse')),
                ('responsable', models.CharField(blank=True, max_length=30, null=True, db_column='Responsable')),
                ('confirmation', models.CharField(blank=True, max_length=30, null=True, db_column='Confirmation')),
            ],
        ),
        migrations.AddField(
            model_name='cursus',
            name='Etudiant',
            field=models.ForeignKey(to='candidat.Etudiant'),
        ),
    ]
