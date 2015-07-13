# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squashapp', '0005_auto_20150713_1453'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectreviewdetails',
            old_name='release_name',
            new_name='release',
        ),
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_region',
            field=models.CharField(default=b'EMEA', max_length=4, choices=[('EMEA', 'EMEA'), ('AMER', 'Americas'), ('JAPC', 'Japan Asia Pac'), ('ALRE', 'All Regions')]),
        ),
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_subregion',
            field=models.CharField(default=b'AFRI', max_length=4, choices=[('LATM', 'LATAM'), ('AMER', 'Americas'), ('MIEA', 'Middle East'), ('AFRI', 'Africa'), ('WEEU', 'Western Europe'), ('EAEU', 'Eastern Europe'), ('INDI', 'India'), ('SOEA', 'SouthEast Asia'), ('CITI', 'Citi'), ('BARC', 'Barclays'), ('ROJA', 'Rest of JAPAC'), ('FCIS', 'FCIS'), ('FCPB', 'FCPB')]),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='applicable_utp_documents',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='itr2_atype_bugs',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='itr2_btype_bugs',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='itr2_ctype_bugs',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='itr2_dtype_bugs',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='itr2_total_bugs',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='subregiondatabase',
            name='region',
            field=models.CharField(default=b'EMEA', max_length=4, choices=[('EMEA', 'EMEA'), ('AMER', 'Americas'), ('JAPC', 'Japan Asia Pac'), ('ALRE', 'All Regions')]),
        ),
    ]
