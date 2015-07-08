# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squashapp', '0016_optionchoice'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectDatabase',
            fields=[
                ('project_release_name', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('project_uid', models.CharField(max_length=15)),
                ('project_class', models.CharField(max_length=3, choices=[('IT', 'IT'), ('IUT', 'IUT'), ('CCB', 'CCB'), ('TEM', 'TEM')])),
                ('project_products', models.CharField(max_length=15, choices=[('FCUBS', 'FCUBS'), ('FCDB', 'FCDB'), ('FCIS', 'FCIS'), ('FCELCM', 'FCELCM'), ('FCPB', 'FCPB'), ('FCR', 'FCR'), ('FC@', 'FC@'), ('FCC', 'FCC')])),
                ('project_status', models.CharField(max_length=9, choices=[('ONG', 'Ongoing'), ('COM', 'Completed'), ('ONH', 'OnHold'), ('DRP', 'Dropped')])),
                ('project_primary_sqa', models.CharField(max_length=30, choices=[('hafizul.azeez', 'hafizul.azeez'), ('pratik.ravani', 'pratik.ravani'), ('sharmila.subramani', 'sharmila.subramani'), ('chandrasekhar.paramanantham', 'chandrasekhar.paramanantham'), ('obi.ravi', 'obi.ravi'), ('kedar.chaudhari', 'kedar.chaudhari'), ('rahatul.huda', 'rahatul.huda'), ('nerissa.rodrigues', 'nerissa.rodrigues'), ('suniel.prabu', 'suniel.prabu'), ('amit.parte', 'amit.parte'), ('priyanka.pandey', 'priyanka.pandey'), ('sunanda.mishra', 'sunanda.mishra'), ('nayana.siddappa', 'nayana.siddappa'), ('tripti.prasad', 'tripti.prasad'), ('prasanna.jain', 'prasanna.jain')])),
                ('project_secondary_sqa', models.CharField(blank=True, max_length=30, choices=[('hafizul.azeez', 'hafizul.azeez'), ('pratik.ravani', 'pratik.ravani'), ('sharmila.subramani', 'sharmila.subramani'), ('chandrasekhar.paramanantham', 'chandrasekhar.paramanantham'), ('obi.ravi', 'obi.ravi'), ('kedar.chaudhari', 'kedar.chaudhari'), ('rahatul.huda', 'rahatul.huda'), ('nerissa.rodrigues', 'nerissa.rodrigues'), ('suniel.prabu', 'suniel.prabu'), ('amit.parte', 'amit.parte'), ('priyanka.pandey', 'priyanka.pandey'), ('sunanda.mishra', 'sunanda.mishra'), ('nayana.siddappa', 'nayana.siddappa'), ('tripti.prasad', 'tripti.prasad'), ('prasanna.jain', 'prasanna.jain')])),
                ('project_tertiary_sqa', models.CharField(blank=True, max_length=30, choices=[('hafizul.azeez', 'hafizul.azeez'), ('pratik.ravani', 'pratik.ravani'), ('sharmila.subramani', 'sharmila.subramani'), ('chandrasekhar.paramanantham', 'chandrasekhar.paramanantham'), ('obi.ravi', 'obi.ravi'), ('kedar.chaudhari', 'kedar.chaudhari'), ('rahatul.huda', 'rahatul.huda'), ('nerissa.rodrigues', 'nerissa.rodrigues'), ('suniel.prabu', 'suniel.prabu'), ('amit.parte', 'amit.parte'), ('priyanka.pandey', 'priyanka.pandey'), ('sunanda.mishra', 'sunanda.mishra'), ('nayana.siddappa', 'nayana.siddappa'), ('tripti.prasad', 'tripti.prasad'), ('prasanna.jain', 'prasanna.jain')])),
                ('project_region_lead', models.CharField(max_length=30, choices=[('hafizul.azeez', 'hafizul.azeez'), ('pratik.ravani', 'pratik.ravani'), ('sharmila.subramani', 'sharmila.subramani'), ('chandrasekhar.paramanantham', 'chandrasekhar.paramanantham'), ('obi.ravi', 'obi.ravi'), ('kedar.chaudhari', 'kedar.chaudhari'), ('rahatul.huda', 'rahatul.huda'), ('nerissa.rodrigues', 'nerissa.rodrigues'), ('suniel.prabu', 'suniel.prabu'), ('amit.parte', 'amit.parte'), ('priyanka.pandey', 'priyanka.pandey'), ('sunanda.mishra', 'sunanda.mishra'), ('nayana.siddappa', 'nayana.siddappa'), ('tripti.prasad', 'tripti.prasad'), ('prasanna.jain', 'prasanna.jain')])),
                ('project_region', models.CharField(max_length=4, choices=[('EMEA', 'EMEA'), ('AMER', 'Americas'), ('JAPC', 'Japan Asia Pac')])),
                ('project_subregion', models.CharField(max_length=4)),
                ('project_created_date', models.DateTimeField(auto_now_add=True)),
                ('project_updated_date', models.DateTimeField(auto_now=True)),
                ('project_start_date', models.DateField(blank=True)),
                ('project_end_date', models.DateField(blank=True)),
                ('project_release_status', models.CharField(max_length=10, choices=[('PKOM', 'PKOM'), ('CUTSTART', 'CUT START'), ('CUTEND', 'CUT END'), ('ITR1START', 'ITR1 START'), ('ITR2START', 'ITR2 START'), ('ITR2END', 'ITR2 END'), ('PREREL', 'Pre Release'), ('RELEASED', 'Released')])),
                ('project_duration', models.IntegerField(blank=True)),
                ('project_is_pm_managed', models.BooleanField(default=False)),
                ('project_description', models.CharField(max_length=1000, blank=True)),
            ],
            options={
                'ordering': ('project_status',),
            },
        ),
    ]
