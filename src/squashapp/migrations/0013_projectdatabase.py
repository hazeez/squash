# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squashapp', '0012_productdatabase'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectDatabase',
            fields=[
                ('project_release_name', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('project_uid', models.CharField(max_length=15)),
                ('project_class', models.CharField(max_length=3, choices=[('IT', 'IT'), ('IUT', 'IUT'), ('CCB', 'CCB'), ('TEM', 'TEM')])),
                ('project_products', models.CharField(max_length=15, choices=[('FCIS', 'FCIS'), ('FCUBS', 'FCUBS'), ('FCPB', 'FCPB'), ('FCR', 'FCR'), ('FCDB', 'FCDB'), ('FC@VJR', 'FC@VJR'), ('FCELCM', 'FCELCM')])),
                ('project_status', models.CharField(max_length=9, choices=[('ONG', 'Ongoing'), ('COM', 'Completed'), ('ONH', 'OnHold')])),
                ('project_primary_sqa', models.CharField(max_length=30, choices=[('hafizul.azeez', 'hafizul.azeez'), ('sunanda.mishra', 'sunanda.mishra'), ('pratik.ravani', 'pratik.ravani'), ('sharmila.subramani', 'sharmila.subramani'), ('tripti.prasad', 'tripti.prasad'), ('nayana.siddappa', 'nayana.siddappa'), ('kedar.chaudhari', 'kedar.chaudhari'), ('rahatul.huda', 'rahatul.huda'), ('obi.ravi', 'obi.ravi')])),
                ('project_secondary_sqa', models.CharField(blank=True, max_length=30, choices=[('hafizul.azeez', 'hafizul.azeez'), ('sunanda.mishra', 'sunanda.mishra'), ('pratik.ravani', 'pratik.ravani'), ('sharmila.subramani', 'sharmila.subramani'), ('tripti.prasad', 'tripti.prasad'), ('nayana.siddappa', 'nayana.siddappa'), ('kedar.chaudhari', 'kedar.chaudhari'), ('rahatul.huda', 'rahatul.huda'), ('obi.ravi', 'obi.ravi')])),
                ('project_tertiary_sqa', models.CharField(blank=True, max_length=30, choices=[('hafizul.azeez', 'hafizul.azeez'), ('sunanda.mishra', 'sunanda.mishra'), ('pratik.ravani', 'pratik.ravani'), ('sharmila.subramani', 'sharmila.subramani'), ('tripti.prasad', 'tripti.prasad'), ('nayana.siddappa', 'nayana.siddappa'), ('kedar.chaudhari', 'kedar.chaudhari'), ('rahatul.huda', 'rahatul.huda'), ('obi.ravi', 'obi.ravi')])),
                ('project_region_lead', models.CharField(max_length=30, choices=[('hafizul.azeez', 'hafizul.azeez'), ('sunanda.mishra', 'sunanda.mishra'), ('pratik.ravani', 'pratik.ravani'), ('sharmila.subramani', 'sharmila.subramani'), ('tripti.prasad', 'tripti.prasad'), ('nayana.siddappa', 'nayana.siddappa'), ('kedar.chaudhari', 'kedar.chaudhari'), ('rahatul.huda', 'rahatul.huda'), ('obi.ravi', 'obi.ravi')])),
                ('project_region', models.CharField(max_length=4, choices=[('EMEA', 'EMEA'), ('EMEA', 'EMEA'), ('EMEA', 'EMEA'), ('EMEA', 'EMEA'), ('NORE', 'No Region')])),
                ('project_subregion', models.CharField(max_length=4, choices=[('AFRI', 'Africa'), ('MIDE', 'Middle East'), ('EEUR', 'Eastern Europe'), ('WEUR', 'Western Europe'), ('NORE', 'No Region')])),
                ('project_created_date', models.DateTimeField(auto_now_add=True)),
                ('project_updated_date', models.DateTimeField(auto_now=True)),
                ('project_start_date', models.DateField(blank=True)),
                ('project_end_date', models.DateField(blank=True)),
                ('project_release_status', models.CharField(max_length=10, choices=[('PKOM', 'PKOM'), ('CUTSTART', 'CUT START'), ('CUTEND', 'CUT END'), ('IUT', 'IUT'), ('ITR1', 'ITR1'), ('ITR2START', 'ITR2 START'), ('ITR2END', 'ITR2 END'), ('PREREL', 'Pre Release'), ('RELEASED', 'Released')])),
                ('project_duration', models.IntegerField(blank=True)),
            ],
            options={
                'ordering': ('project_status',),
            },
        ),
    ]
