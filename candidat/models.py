# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.

from django.db import models

class Etudiant(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)
    genre = models.CharField(db_column='genre',max_length=25, blank=True, null=True)
    nom = models.CharField(db_column='Nom', max_length=25, blank=True, null=True)
    prenom = models.CharField(db_column='Prenom', max_length=28, blank=True, null=True)
    date_naissance =  models.IntegerField(db_column="date_naissance",blank=True, null=True)
    adresse = models.CharField(db_column='adresse', max_length=100, blank=True, null=True)
    email = models.EmailField(db_column='email', unique=True, blank=True, null=True)

    def __str__(self):
        return '{0} {1}'.format(self.prenom, self.nom)

    def get_value(self):
        return [(field.value(self)) for field in Etudiant._meta.get_fields(include_hidden=False)]


class Annee(models.Model):
    formation = models.CharField(db_column='Formation', max_length=100, blank=True, null=True)
    etablissement  = models.CharField(db_column='Etablissement', max_length=100, blank=True, null=True)
    millesime = models.CharField(db_column='Millesime', max_length=15, blank=True, null=True)

class Cursus(models.Model):
    Etudiant= models.ForeignKey(Etudiant)
    Annee = models.ForeignKey(Annee)


class Ncandidature(models.Model):
    millesime = models.CharField(db_column='Millesime', max_length=9, blank=True, null=True)
    formation = models.CharField(db_column='Formation', max_length=30, blank=True, null=True)
    reponse = models.CharField(db_column='Reponse', max_length=10, blank=True, null=True)
    responsable = models.CharField(db_column='Responsable', max_length=30, blank=True, null=True)
    confirmation = models.CharField(db_column='Confirmation', max_length=30, blank=True, null=True)

class Candidature(models.Model):
    admission20082009 = models.CharField(db_column='Admission20082009', max_length=24, blank=True, null=True)  # Field name made lowercase.
    admission20092010 = models.CharField(db_column='Admission20092010', max_length=14, blank=True, null=True)  # Field name made lowercase.
    admission20102011 = models.CharField(db_column='Admission20102011', max_length=20, blank=True, null=True)  # Field name made lowercase.
    admission20112012 = models.CharField(db_column='Admission20112012', max_length=16, blank=True, null=True)  # Field name made lowercase.
    admission20122013 = models.CharField(db_column='Admission20122013', max_length=10, blank=True, null=True)  # Field name made lowercase.
    admission20132014 = models.CharField(db_column='Admission20132014', max_length=10, blank=True, null=True)  # Field name made lowercase.
    admission20142015 = models.CharField(db_column='Admission20142015', max_length=10, blank=True, null=True)  # Field name made lowercase.
    admission20152016 = models.CharField(db_column='Admission20152016', max_length=10, blank=True, null=True)  # Field name made lowercase.
    admission20162017 = models.CharField(db_column='Admission20162017', max_length=10, blank=True, null=True)  # Field name made lowercase.
    admission20172018 = models.CharField(db_column='Admission20172018', max_length=10, blank=True, null=True)  # Field name made lowercase.
    admission20182019 = models.CharField(db_column='Admission20182019', max_length=10, blank=True, null=True)  # Field name made lowercase.
    admission20192020 = models.CharField(db_column='Admission20192020', max_length=10, blank=True, null=True)  # Field name made lowercase.
    algant = models.CharField(db_column='Algant', max_length=1, blank=True, null=True)  # Field name made lowercase.
    algant2 = models.CharField(db_column='Algant2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    algant3 = models.CharField(db_column='Algant3', max_length=10, blank=True, null=True)  # Field name made lowercase.
    algant4 = models.CharField(db_column='Algant4', max_length=10, blank=True, null=True)  # Field name made lowercase.
    algant5 = models.CharField(db_column='Algant5', max_length=10, blank=True, null=True)  # Field name made lowercase.
    année = models.CharField(db_column='Année', max_length=9, blank=True, null=True)  # Field name made lowercase.
    année2 = models.CharField(db_column='Année2', max_length=9, blank=True, null=True)  # Field name made lowercase.
    année3 = models.CharField(db_column='Année3', max_length=9, blank=True, null=True)  # Field name made lowercase.
    année4 = models.CharField(db_column='Année4', max_length=9, blank=True, null=True)  # Field name made lowercase.
    année5 = models.CharField(db_column='Année5', max_length=9, blank=True, null=True)  # Field name made lowercase.
    anneeentrée = models.CharField(db_column='anneeEntrée', max_length=4, blank=True, null=True)  # Field name made lowercase.
    anneesortie = models.CharField(db_column='anneeSortie', max_length=4, blank=True, null=True)  # Field name made lowercase.
    annéevisualisée = models.CharField(db_column='annéeVisualisée', max_length=9, blank=True, null=True)  # Field name made lowercase.
    avis_2_donné_le = models.CharField(db_column='Avis 2 donné le', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    avis_2_donné_le2 = models.CharField(db_column='Avis 2 donné le2', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    avis_2_donné_le3 = models.CharField(db_column='Avis 2 donné le3', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    avis_2_donné_le4 = models.CharField(db_column='Avis 2 donné le4', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    avis_2_donné_le5 = models.CharField(db_column='Avis 2 donné le5', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    avis_2_donné_par = models.CharField(db_column='Avis 2 donné par', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    avis_2_donné_par2 = models.CharField(db_column='Avis 2 donné par2', max_length=14, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    avis_2_donné_par3 = models.CharField(db_column='Avis 2 donné par3', max_length=14, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    avis_2_donné_par4 = models.CharField(db_column='Avis 2 donné par4', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    avis_2_donné_par5 = models.CharField(db_column='Avis 2 donné par5', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    avis_donné_le = models.CharField(db_column='Avis donné le', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    avis_donné_le2 = models.CharField(db_column='Avis donné le2', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    avis_donné_le3 = models.CharField(db_column='Avis donné le3', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    avis_donné_le4 = models.CharField(db_column='Avis donné le4', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    avis_donné_le5 = models.CharField(db_column='Avis donné le5', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    avis_donné_par = models.CharField(db_column='Avis donné par', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    avis_donné_par2 = models.CharField(db_column='Avis donné par2', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    avis_donné_par3 = models.CharField(db_column='Avis donné par3', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    avis_donné_par4 = models.CharField(db_column='Avis donné par4', max_length=14, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    avis_donné_par5 = models.CharField(db_column='Avis donné par5', max_length=14, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cdpar = models.CharField(max_length=9, blank=True, null=True)
    cdpar2 = models.CharField(max_length=10, blank=True, null=True)
    cdpar3 = models.CharField(max_length=10, blank=True, null=True)
    cdpar4 = models.CharField(max_length=10, blank=True, null=True)
    cdpar5 = models.CharField(max_length=10, blank=True, null=True)
    civilité_décompte = models.IntegerField(db_column='Civilité Décompte', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    commentaires20082009 = models.CharField(max_length=7, blank=True, null=True)
    commentaires20092010 = models.CharField(max_length=10, blank=True, null=True)
    commentaires20102011 = models.CharField(max_length=61, blank=True, null=True)
    commentaires20112012 = models.CharField(max_length=26, blank=True, null=True)
    commentaires20122013 = models.CharField(max_length=15, blank=True, null=True)
    commentaires20132014 = models.CharField(max_length=10, blank=True, null=True)
    commentaires20142015 = models.CharField(max_length=10, blank=True, null=True)
    commentaires20152016 = models.CharField(max_length=10, blank=True, null=True)
    commentaires20162017 = models.CharField(max_length=10, blank=True, null=True)
    commentaires20172018 = models.CharField(max_length=10, blank=True, null=True)
    commentaires20182019 = models.CharField(max_length=10, blank=True, null=True)
    commentaires20192020 = models.CharField(max_length=10, blank=True, null=True)
    complément_de_dossier_demandé_le = models.CharField(db_column='Complément de dossier demandé le', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    complément_de_dossier_demandé_le2 = models.CharField(db_column='Complément de dossier demandé le2', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    complément_de_dossier_demandé_le3 = models.CharField(db_column='Complément de dossier demandé le3', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    complément_de_dossier_demandé_le4 = models.CharField(db_column='Complément de dossier demandé le4', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    complément_de_dossier_demandé_le5 = models.CharField(db_column='Complément de dossier demandé le5', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    confirmation = models.CharField(db_column='Confirmation', max_length=22, blank=True, null=True)  # Field name made lowercase.
    confirmation_décompte = models.IntegerField(db_column='Confirmation Décompte', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    confirmation_décompte_cumulé = models.IntegerField(db_column='Confirmation Décompte cumulé', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    confirmation2 = models.CharField(db_column='Confirmation2', max_length=16, blank=True, null=True)  # Field name made lowercase.
    confirmation3 = models.CharField(db_column='Confirmation3', max_length=11, blank=True, null=True)  # Field name made lowercase.
    confirmation4 = models.CharField(db_column='Confirmation4', max_length=7, blank=True, null=True)  # Field name made lowercase.
    confirmation5 = models.CharField(db_column='Confirmation5', max_length=6, blank=True, null=True)  # Field name made lowercase.
    date_d_arrivée_du_dossier = models.CharField(db_column="Date d'arrivée du dossier", max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_d_arrivée_du_dossier2 = models.CharField(db_column="Date d'arrivée du dossier2", max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_d_arrivée_du_dossier3 = models.CharField(db_column="Date d'arrivée du dossier3", max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_d_arrivée_du_dossier4 = models.CharField(db_column="Date d'arrivée du dossier4", max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_d_arrivée_du_dossier5 = models.CharField(db_column="Date d'arrivée du dossier5", max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    durée = models.CharField(max_length=8, blank=True, null=True)
    durée20002010 = models.CharField(max_length=8, blank=True, null=True)
    durée20082009 = models.CharField(max_length=8, blank=True, null=True)
    email = models.CharField(max_length=34, blank=True, null=True)
    email2 = models.CharField(max_length=36, blank=True, null=True)
    entré_en = models.CharField(db_column='entré en', max_length=8, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    erasmus = models.CharField(db_column='Erasmus', max_length=1, blank=True, null=True)  # Field name made lowercase.
    erasmus2 = models.CharField(db_column='Erasmus2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    erasmus3 = models.CharField(db_column='Erasmus3', max_length=10, blank=True, null=True)  # Field name made lowercase.
    erasmus4 = models.CharField(db_column='Erasmus4', max_length=10, blank=True, null=True)  # Field name made lowercase.
    erasmus5 = models.CharField(db_column='Erasmus5', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fmjh = models.CharField(db_column='FMJH', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fmjh2 = models.CharField(db_column='FMJH2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fmjh3 = models.CharField(db_column='FMJH3', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fmjh4 = models.CharField(db_column='FMJH4', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fmjh5 = models.CharField(db_column='FMJH5', max_length=10, blank=True, null=True)  # Field name made lowercase.
    formation20082009 = models.CharField(db_column='Formation20082009', max_length=60, blank=True, null=True)  # Field name made lowercase.
    formation20092010 = models.CharField(db_column='Formation20092010', max_length=69, blank=True, null=True)  # Field name made lowercase.
    formation20102011 = models.CharField(db_column='Formation20102011', max_length=69, blank=True, null=True)  # Field name made lowercase.
    formation20112012 = models.CharField(db_column='Formation20112012', max_length=88, blank=True, null=True)  # Field name made lowercase.
    formation20122013 = models.CharField(db_column='Formation20122013', max_length=57, blank=True, null=True)  # Field name made lowercase.
    formation20132014 = models.CharField(db_column='Formation20132014', max_length=55, blank=True, null=True)  # Field name made lowercase.
    formation20142015 = models.CharField(db_column='Formation20142015', max_length=32, blank=True, null=True)  # Field name made lowercase.
    formation20152016 = models.CharField(db_column='Formation20152016', max_length=10, blank=True, null=True)  # Field name made lowercase.
    formation20162017 = models.CharField(db_column='Formation20162017', max_length=10, blank=True, null=True)  # Field name made lowercase.
    formation20172018 = models.CharField(db_column='Formation20172018', max_length=10, blank=True, null=True)  # Field name made lowercase.
    formation20182019 = models.CharField(db_column='Formation20182019', max_length=10, blank=True, null=True)  # Field name made lowercase.
    formation20192020 = models.CharField(db_column='Formation20192020', max_length=10, blank=True, null=True)  # Field name made lowercase.
    genre = models.CharField(db_column='Genre', max_length=3, blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    l3_ecom = models.CharField(db_column='L3 ECOM', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    l3_ecom2 = models.CharField(db_column='L3 ECOM2', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    l3_ecom3 = models.CharField(db_column='L3 ECOM3', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    l3_ecom4 = models.CharField(db_column='L3 ECOM4', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    l3_ecom5 = models.CharField(db_column='L3 ECOM5', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    l3_map = models.CharField(db_column='L3 MAP', max_length=12, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    l3_map2 = models.CharField(db_column='L3 MAP2', max_length=12, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    l3_map3 = models.CharField(db_column='L3 MAP3', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    l3_map4 = models.CharField(db_column='L3 MAP4', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    l3_map5 = models.CharField(db_column='L3 MAP5', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    l3_mathens = models.CharField(db_column='L3 MATHENS', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    l3_mathens2 = models.CharField(db_column='L3 MATHENS2', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    l3_mathens3 = models.CharField(db_column='L3 MATHENS3', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    l3_mathens4 = models.CharField(db_column='L3 MATHENS4', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    l3_mathens5 = models.CharField(db_column='L3 MATHENS5', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    l3_mathinfo = models.CharField(db_column='L3 MATHINFO', max_length=12, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    l3_mathinfo2 = models.CharField(db_column='L3 MATHINFO2', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    l3_mathinfo3 = models.CharField(db_column='L3 MATHINFO3', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    l3_mathinfo4 = models.CharField(db_column='L3 MATHINFO4', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    l3_mathinfo5 = models.CharField(db_column='L3 MATHINFO5', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    l3_mfa = models.CharField(db_column='L3 MFA', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    l3_mfa2 = models.CharField(db_column='L3 MFA2', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    l3_mfa3 = models.CharField(db_column='L3 MFA3', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    l3_mfa4 = models.CharField(db_column='L3 MFA4', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    l3_mfa5 = models.CharField(db_column='L3 MFA5', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    l3_mint1 = models.CharField(db_column='L3 MINT1', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    l3_mint2 = models.CharField(db_column='L3 MINT2', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    l3_mint3 = models.CharField(db_column='L3 MINT3', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    l3_mint4 = models.CharField(db_column='L3 MINT4', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    l3_mint5 = models.CharField(db_column='L3 MINT5', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    l3mfaingé = models.CharField(db_column='L3MFAIngé', max_length=3, blank=True, null=True)  # Field name made lowercase.
    l3mfaingé2 = models.CharField(db_column='L3MFAIngé2', max_length=3, blank=True, null=True)  # Field name made lowercase.
    l3mfaingé3 = models.CharField(db_column='L3MFAIngé3', max_length=10, blank=True, null=True)  # Field name made lowercase.
    l3mfaingé4 = models.CharField(db_column='L3MFAIngé4', max_length=10, blank=True, null=True)  # Field name made lowercase.
    l3mfaingé5 = models.CharField(db_column='L3MFAIngé5', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m1_mfa = models.CharField(db_column='M1 MFA', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    m1_mfa2 = models.CharField(db_column='M1 MFA2', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    m1_mfa3 = models.CharField(db_column='M1 MFA3', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    m1_mfa4 = models.CharField(db_column='M1 MFA4', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    m1_mfa5 = models.CharField(db_column='M1 MFA5', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    m1mfaingé = models.CharField(db_column='M1MFAIngé', max_length=3, blank=True, null=True)  # Field name made lowercase.
    m1mfaingé2 = models.CharField(db_column='M1MFAIngé2', max_length=3, blank=True, null=True)  # Field name made lowercase.
    m1mfaingé3 = models.CharField(db_column='M1MFAIngé3', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m1mfaingé4 = models.CharField(db_column='M1MFAIngé4', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m1mfaingé5 = models.CharField(db_column='M1MFAIngé5', max_length=10, blank=True, null=True)  # Field name made lowercase.
    magistère_1 = models.CharField(db_column='Magistère 1', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    magistère_12 = models.CharField(db_column='Magistère 12', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    magistère_13 = models.CharField(db_column='Magistère 13', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    magistère_14 = models.CharField(db_column='Magistère 14', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    magistère_15 = models.CharField(db_column='Magistère 15', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    magistère_2 = models.CharField(db_column='Magistère 2', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    magistère_22 = models.CharField(db_column='Magistère 22', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    magistère_23 = models.CharField(db_column='Magistère 23', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    magistère_24 = models.CharField(db_column='Magistère 24', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    magistère_25 = models.CharField(db_column='Magistère 25', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    magistère_3 = models.CharField(db_column='Magistère 3', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    magistère_32 = models.CharField(db_column='Magistère 32', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    magistère_33 = models.CharField(db_column='Magistère 33', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    magistère_34 = models.CharField(db_column='Magistère 34', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    magistère_35 = models.CharField(db_column='Magistère 35', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nom = models.CharField(db_column='Nom', max_length=25, blank=True, null=True)  # Field name made lowercase.
    numero_etudiant = models.CharField(db_column='Numero Etudiant', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    numero_opi = models.CharField(db_column='Numero OPI', max_length=22, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    numero_opi2 = models.CharField(db_column='Numero OPI2', max_length=11, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    numero_opi3 = models.CharField(db_column='Numero OPI3', max_length=5, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    numero_opi4 = models.CharField(db_column='Numero OPI4', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    numero_opi5 = models.CharField(db_column='Numero OPI5', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    origine = models.CharField(db_column='Origine', max_length=41, blank=True, null=True)  # Field name made lowercase.
    origine2 = models.CharField(db_column='Origine2', max_length=18, blank=True, null=True)  # Field name made lowercase.
    origine3 = models.CharField(db_column='Origine3', max_length=17, blank=True, null=True)  # Field name made lowercase.
    origine4 = models.CharField(db_column='Origine4', max_length=12, blank=True, null=True)  # Field name made lowercase.
    origine5 = models.CharField(db_column='Origine5', max_length=10, blank=True, null=True)  # Field name made lowercase.
    parcours_demandé = models.CharField(db_column='Parcours demandé', max_length=41, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    parcours_demandé2 = models.CharField(db_column='Parcours demandé2', max_length=25, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    parcours_demandé3 = models.CharField(db_column='Parcours demandé3', max_length=14, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    parcours_demandé4 = models.CharField(db_column='Parcours demandé4', max_length=14, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    parcours_demandé5 = models.CharField(db_column='Parcours demandé5', max_length=6, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    prénom = models.CharField(db_column='Prénom', max_length=28, blank=True, null=True)  # Field name made lowercase.
    remarques = models.CharField(db_column='Remarques', max_length=88, blank=True, null=True)  # Field name made lowercase.
    remarques2 = models.CharField(db_column='Remarques2', max_length=41, blank=True, null=True)  # Field name made lowercase.
    remarques3 = models.CharField(db_column='Remarques3', max_length=10, blank=True, null=True)  # Field name made lowercase.
    remarques4 = models.CharField(db_column='Remarques4', max_length=9, blank=True, null=True)  # Field name made lowercase.
    remarques5 = models.CharField(db_column='Remarques5', max_length=10, blank=True, null=True)  # Field name made lowercase.
    remarquesc = models.CharField(db_column='RemarquesC', max_length=52, blank=True, null=True)  # Field name made lowercase.
    réponse = models.CharField(db_column='Réponse', max_length=48, blank=True, null=True)  # Field name made lowercase.
    réponse2 = models.CharField(db_column='Réponse2', max_length=29, blank=True, null=True)  # Field name made lowercase.
    réponse3 = models.CharField(db_column='Réponse3', max_length=11, blank=True, null=True)  # Field name made lowercase.
    réponse4 = models.CharField(db_column='Réponse4', max_length=7, blank=True, null=True)  # Field name made lowercase.
    réponse5 = models.CharField(db_column='Réponse5', max_length=6, blank=True, null=True)  # Field name made lowercase.
    résultat20082009 = models.CharField(db_column='Résultat20082009', max_length=10, blank=True, null=True)  # Field name made lowercase.
    résultat20092010 = models.CharField(db_column='Résultat20092010', max_length=10, blank=True, null=True)  # Field name made lowercase.
    résultat20102011 = models.CharField(db_column='Résultat20102011', max_length=10, blank=True, null=True)  # Field name made lowercase.
    résultat20112012 = models.CharField(db_column='Résultat20112012', max_length=10, blank=True, null=True)  # Field name made lowercase.
    résultat20122013 = models.CharField(db_column='Résultat20122013', max_length=10, blank=True, null=True)  # Field name made lowercase.
    résultat20132014 = models.CharField(db_column='Résultat20132014', max_length=10, blank=True, null=True)  # Field name made lowercase.
    résultat20142015 = models.CharField(db_column='Résultat20142015', max_length=10, blank=True, null=True)  # Field name made lowercase.
    résultat20152016 = models.CharField(db_column='Résultat20152016', max_length=10, blank=True, null=True)  # Field name made lowercase.
    résultat20162017 = models.CharField(db_column='Résultat20162017', max_length=10, blank=True, null=True)  # Field name made lowercase.
    résultat20172018 = models.CharField(db_column='Résultat20172018', max_length=10, blank=True, null=True)  # Field name made lowercase.
    résultat20182019 = models.CharField(db_column='Résultat20182019', max_length=10, blank=True, null=True)  # Field name made lowercase.
    résultat20192020 = models.CharField(db_column='Résultat20192020', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rien = models.CharField(max_length=10, blank=True, null=True)
    rubrique = models.CharField(db_column='Rubrique', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rubrique_245 = models.CharField(db_column='Rubrique 245', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    saisie_opi_le = models.CharField(db_column='Saisie OPI le', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    saisie_opi_le2 = models.CharField(db_column='Saisie OPI le2', max_length=9, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    saisie_opi_le3 = models.CharField(db_column='Saisie OPI le3', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    saisie_opi_le4 = models.CharField(db_column='Saisie OPI le4', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    saisie_opi_le5 = models.CharField(db_column='Saisie OPI le5', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sorti_en = models.CharField(db_column='Sorti en', max_length=9, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vérifié_le = models.CharField(db_column='Vérifié le', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        db_table = 'candidature'

    def __str__(self):
        return '{0} {1}'.format(self.prenom, self.nom)

