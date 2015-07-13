# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squashapp', '0005_auto_20150713_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_primary_sqa',
            field=models.CharField(default=b'PM', max_length=30, choices=[('hafizul.azeez', 'hafizul.azeez'), ('pratik.ravani', 'pratik.ravani'), ('sharmila.subramani', 'sharmila.subramani'), ('chandrasekhar.paramanantham', 'chandrasekhar.paramanantham'), ('obi.ravi', 'obi.ravi'), ('kedar.chaudhari', 'kedar.chaudhari'), ('rahatul.huda', 'rahatul.huda'), ('nerissa.rodrigues', 'nerissa.rodrigues'), ('suniel.prabu', 'suniel.prabu'), ('amit.parte', 'amit.parte'), ('priyanka.pandey', 'priyanka.pandey'), ('sunanda.mishra', 'sunanda.mishra'), ('nayana.siddappa', 'nayana.siddappa'), ('tripti.prasad', 'tripti.prasad'), ('prasanna.jain', 'prasanna.jain')]),
        ),
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_secondary_sqa',
            field=models.CharField(default=b'none', max_length=30, blank=True, choices=[('hafizul.azeez', 'hafizul.azeez'), ('pratik.ravani', 'pratik.ravani'), ('sharmila.subramani', 'sharmila.subramani'), ('chandrasekhar.paramanantham', 'chandrasekhar.paramanantham'), ('obi.ravi', 'obi.ravi'), ('kedar.chaudhari', 'kedar.chaudhari'), ('rahatul.huda', 'rahatul.huda'), ('nerissa.rodrigues', 'nerissa.rodrigues'), ('suniel.prabu', 'suniel.prabu'), ('amit.parte', 'amit.parte'), ('priyanka.pandey', 'priyanka.pandey'), ('sunanda.mishra', 'sunanda.mishra'), ('nayana.siddappa', 'nayana.siddappa'), ('tripti.prasad', 'tripti.prasad'), ('prasanna.jain', 'prasanna.jain')]),
        ),
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_tertiary_sqa',
            field=models.CharField(default=b'none', max_length=30, blank=True, choices=[('hafizul.azeez', 'hafizul.azeez'), ('pratik.ravani', 'pratik.ravani'), ('sharmila.subramani', 'sharmila.subramani'), ('chandrasekhar.paramanantham', 'chandrasekhar.paramanantham'), ('obi.ravi', 'obi.ravi'), ('kedar.chaudhari', 'kedar.chaudhari'), ('rahatul.huda', 'rahatul.huda'), ('nerissa.rodrigues', 'nerissa.rodrigues'), ('suniel.prabu', 'suniel.prabu'), ('amit.parte', 'amit.parte'), ('priyanka.pandey', 'priyanka.pandey'), ('sunanda.mishra', 'sunanda.mishra'), ('nayana.siddappa', 'nayana.siddappa'), ('tripti.prasad', 'tripti.prasad'), ('prasanna.jain', 'prasanna.jain')]),
        ),
    ]
