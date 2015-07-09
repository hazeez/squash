# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squashapp', '0002_auto_20150709_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_class',
            field=models.CharField(default=b'IUT', max_length=3, choices=[('IT', 'IT'), ('IUT', 'IUT'), ('CCB', 'CCB'), ('TEM', 'TEM')]),
        ),
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_primary_sqa',
            field=models.CharField(default=b'hafizul.azeez', max_length=30, choices=[('hafizul.azeez', 'hafizul.azeez'), ('pratik.ravani', 'pratik.ravani'), ('sharmila.subramani', 'sharmila.subramani'), ('chandrasekhar.paramanantham', 'chandrasekhar.paramanantham'), ('obi.ravi', 'obi.ravi'), ('kedar.chaudhari', 'kedar.chaudhari'), ('rahatul.huda', 'rahatul.huda'), ('nerissa.rodrigues', 'nerissa.rodrigues'), ('suniel.prabu', 'suniel.prabu'), ('amit.parte', 'amit.parte'), ('priyanka.pandey', 'priyanka.pandey'), ('sunanda.mishra', 'sunanda.mishra'), ('nayana.siddappa', 'nayana.siddappa'), ('tripti.prasad', 'tripti.prasad'), ('prasanna.jain', 'prasanna.jain')]),
        ),
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_products',
            field=models.CharField(default=b'FCUBS', max_length=15, choices=[('FCUBS', 'FCUBS'), ('FCDB', 'FCDB'), ('FCIS', 'FCIS'), ('FCELCM', 'FCELCM'), ('FCPB', 'FCPB'), ('FCR', 'FCR'), ('FC@', 'FC@'), ('FCC', 'FCC')]),
        ),
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_region',
            field=models.CharField(default=b'EMEA', max_length=4, choices=[('EMEA', 'EMEA'), ('AMER', 'Americas'), ('JAPC', 'Japan Asia Pac'), ('FCIS', 'FCIS'), ('FCPB', 'FCPB'), ('CITI', 'CITI'), ('BARC', 'Barclays')]),
        ),
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_region_lead',
            field=models.CharField(default=b'hafizul.azeez', max_length=30, choices=[('hafizul.azeez', 'hafizul.azeez'), ('pratik.ravani', 'pratik.ravani'), ('sharmila.subramani', 'sharmila.subramani'), ('chandrasekhar.paramanantham', 'chandrasekhar.paramanantham'), ('obi.ravi', 'obi.ravi'), ('kedar.chaudhari', 'kedar.chaudhari'), ('rahatul.huda', 'rahatul.huda'), ('nerissa.rodrigues', 'nerissa.rodrigues'), ('suniel.prabu', 'suniel.prabu'), ('amit.parte', 'amit.parte'), ('priyanka.pandey', 'priyanka.pandey'), ('sunanda.mishra', 'sunanda.mishra'), ('nayana.siddappa', 'nayana.siddappa'), ('tripti.prasad', 'tripti.prasad'), ('prasanna.jain', 'prasanna.jain')]),
        ),
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_release_status',
            field=models.CharField(default=b'PKOM', max_length=10, choices=[('PKOM', 'PKOM'), ('CUTSTART', 'CUT START'), ('CUTEND', 'CUT END'), ('ITR1START', 'ITR1 START'), ('ITR2START', 'ITR2 START'), ('ITR2END', 'ITR2 END'), ('PREREL', 'Pre Release'), ('RELEASED', 'Released')]),
        ),
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_secondary_sqa',
            field=models.CharField(default=b'hafizul.azeez', max_length=30, blank=True, choices=[('hafizul.azeez', 'hafizul.azeez'), ('pratik.ravani', 'pratik.ravani'), ('sharmila.subramani', 'sharmila.subramani'), ('chandrasekhar.paramanantham', 'chandrasekhar.paramanantham'), ('obi.ravi', 'obi.ravi'), ('kedar.chaudhari', 'kedar.chaudhari'), ('rahatul.huda', 'rahatul.huda'), ('nerissa.rodrigues', 'nerissa.rodrigues'), ('suniel.prabu', 'suniel.prabu'), ('amit.parte', 'amit.parte'), ('priyanka.pandey', 'priyanka.pandey'), ('sunanda.mishra', 'sunanda.mishra'), ('nayana.siddappa', 'nayana.siddappa'), ('tripti.prasad', 'tripti.prasad'), ('prasanna.jain', 'prasanna.jain')]),
        ),
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_status',
            field=models.CharField(default=b'ONG', max_length=9, choices=[('ONG', 'Ongoing'), ('COM', 'Completed'), ('ONH', 'OnHold'), ('DRP', 'Dropped')]),
        ),
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_subregion',
            field=models.CharField(default=b'AFRI', max_length=4, choices=[('LATM', 'LATAM'), ('AMER', 'Americas'), ('MIEA', 'Middle East'), ('AFRI', 'Africa'), ('WEEU', 'Western Europe'), ('EAEU', 'Eastern Europe'), ('INDI', 'India'), ('SOEA', 'SouthEast Asia'), ('CITI', 'Citi'), ('BARC', 'Barclays'), ('ROJA', 'Rest of JAPAC')]),
        ),
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_tertiary_sqa',
            field=models.CharField(default=b'hafizul.azeez', max_length=30, blank=True, choices=[('hafizul.azeez', 'hafizul.azeez'), ('pratik.ravani', 'pratik.ravani'), ('sharmila.subramani', 'sharmila.subramani'), ('chandrasekhar.paramanantham', 'chandrasekhar.paramanantham'), ('obi.ravi', 'obi.ravi'), ('kedar.chaudhari', 'kedar.chaudhari'), ('rahatul.huda', 'rahatul.huda'), ('nerissa.rodrigues', 'nerissa.rodrigues'), ('suniel.prabu', 'suniel.prabu'), ('amit.parte', 'amit.parte'), ('priyanka.pandey', 'priyanka.pandey'), ('sunanda.mishra', 'sunanda.mishra'), ('nayana.siddappa', 'nayana.siddappa'), ('tripti.prasad', 'tripti.prasad'), ('prasanna.jain', 'prasanna.jain')]),
        ),
    ]
