# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squashapp', '0013_projectdatabase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_primary_sqa',
            field=models.CharField(max_length=30, choices=[('hafizul.azeez', 'hafizul.azeez'), ('sunanda.mishra', 'sunanda.mishra'), ('pratik.ravani', 'pratik.ravani'), ('sharmila.subramani', 'sharmila.subramani'), ('tripti.prasad', 'tripti.prasad'), ('nayana.siddappa', 'nayana.siddappa'), ('kedar.chaudhari', 'kedar.chaudhari'), ('rahatul.huda', 'rahatul.huda'), ('obi.ravi', 'obi.ravi'), ('chandrasekhar.paramanantham', 'chandrasekhar.paramanantham'), ('suniel.prabu', 'suniel.prabu'), ('prasanna.jain', 'prasanna.jain')]),
        ),
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_region_lead',
            field=models.CharField(max_length=30, choices=[('hafizul.azeez', 'hafizul.azeez'), ('sunanda.mishra', 'sunanda.mishra'), ('pratik.ravani', 'pratik.ravani'), ('sharmila.subramani', 'sharmila.subramani'), ('tripti.prasad', 'tripti.prasad'), ('nayana.siddappa', 'nayana.siddappa'), ('kedar.chaudhari', 'kedar.chaudhari'), ('rahatul.huda', 'rahatul.huda'), ('obi.ravi', 'obi.ravi'), ('chandrasekhar.paramanantham', 'chandrasekhar.paramanantham'), ('suniel.prabu', 'suniel.prabu'), ('prasanna.jain', 'prasanna.jain')]),
        ),
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_secondary_sqa',
            field=models.CharField(blank=True, max_length=30, choices=[('hafizul.azeez', 'hafizul.azeez'), ('sunanda.mishra', 'sunanda.mishra'), ('pratik.ravani', 'pratik.ravani'), ('sharmila.subramani', 'sharmila.subramani'), ('tripti.prasad', 'tripti.prasad'), ('nayana.siddappa', 'nayana.siddappa'), ('kedar.chaudhari', 'kedar.chaudhari'), ('rahatul.huda', 'rahatul.huda'), ('obi.ravi', 'obi.ravi'), ('chandrasekhar.paramanantham', 'chandrasekhar.paramanantham'), ('suniel.prabu', 'suniel.prabu'), ('prasanna.jain', 'prasanna.jain')]),
        ),
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_tertiary_sqa',
            field=models.CharField(blank=True, max_length=30, choices=[('hafizul.azeez', 'hafizul.azeez'), ('sunanda.mishra', 'sunanda.mishra'), ('pratik.ravani', 'pratik.ravani'), ('sharmila.subramani', 'sharmila.subramani'), ('tripti.prasad', 'tripti.prasad'), ('nayana.siddappa', 'nayana.siddappa'), ('kedar.chaudhari', 'kedar.chaudhari'), ('rahatul.huda', 'rahatul.huda'), ('obi.ravi', 'obi.ravi'), ('chandrasekhar.paramanantham', 'chandrasekhar.paramanantham'), ('suniel.prabu', 'suniel.prabu'), ('prasanna.jain', 'prasanna.jain')]),
        ),
    ]
