# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-27 13:34
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django_hstore.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_anuncio', models.IntegerField()),
                ('year', models.IntegerField()),
                ('datos_registrales', models.CharField(max_length=70)),
                ('actos', django_hstore.fields.SerializedDictionaryField()),
            ],
        ),
        migrations.CreateModel(
            name='Borme',
            fields=[
                ('cve', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('url', models.URLField()),
                ('from_reg', models.IntegerField()),
                ('until_reg', models.IntegerField()),
                ('province', models.CharField(max_length=100)),
                ('section', models.CharField(max_length=20)),
                ('anuncios', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=list, size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('name', models.CharField(db_index=True, max_length=260)),
                ('nif', models.CharField(max_length=10)),
                ('slug', models.CharField(max_length=260, primary_key=True, serialize=False)),
                ('date_creation', models.DateField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('type', models.CharField(choices=[('AEIE', 'Agrupación Europea de Interés Económico'), ('AIE', 'Agrupación de Interés Económico'), ('BV', 'Besloten vennootschap met beperkte aansprakelijkheid'), ('BVBA', 'Besloten vennootschap met beperkte aansprakelijkheid'), ('COOP', 'Cooperativa'), ('FP', 'Fondo de Pensiones'), ('NV', 'Naamloze Vennootschap'), ('SA', 'Sociedad Anónima'), ('SAD', 'Sociedad Anónima Deportiva'), ('SAL', 'Sociedad Anónima Laboral'), ('SAP', 'Sociedad Anónima P?'), ('SAS', 'Sociedad por Acciones Simplificada'), ('SAU', 'Sociedad Anónima Unipersonal'), ('SC', 'Sociedad Comanditaria'), ('SCP', 'Sociedad Civil Profesional'), ('SL', 'Sociedad Limitada'), ('SLL', 'Sociedad Limitada Laboral'), ('SLLP', 'Sociedad Limitada Laboral P?'), ('SLNE', 'Sociedad Limitada Nueva Empresa'), ('SLP', 'Sociedad Limitada Profesional'), ('SLU', 'Sociedad Limitada Unipersonal'), ('SRL', 'Sociedad de Responsabilidad Limitada'), ('SRLL', 'Sociedad de Responsabilidad Limitada Laboral'), ('SRLP', 'Sociedad de Responsabilidad Limitada Profesional')], max_length=50)),
                ('date_updated', models.DateField(db_index=True)),
                ('in_bormes', django.contrib.postgres.fields.ArrayField(base_field=django_hstore.fields.DictionaryField(), default=list, size=None)),
                ('anuncios', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=list, size=None)),
                ('cargos_actuales_p', django.contrib.postgres.fields.ArrayField(base_field=django_hstore.fields.DictionaryField(), default=list, size=None)),
                ('cargos_actuales_c', django.contrib.postgres.fields.ArrayField(base_field=django_hstore.fields.DictionaryField(), default=list, size=None)),
                ('cargos_historial_p', django.contrib.postgres.fields.ArrayField(base_field=django_hstore.fields.DictionaryField(), default=list, size=None)),
                ('cargos_historial_c', django.contrib.postgres.fields.ArrayField(base_field=django_hstore.fields.DictionaryField(), default=list, size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_modified', models.DateTimeField()),
                ('version', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('in_companies', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=260), default=list, size=None)),
                ('in_bormes', django.contrib.postgres.fields.ArrayField(base_field=django_hstore.fields.DictionaryField(), default=list, size=None)),
                ('date_updated', models.DateField(db_index=True)),
                ('cargos_actuales', django.contrib.postgres.fields.ArrayField(base_field=django_hstore.fields.DictionaryField(), default=list, size=None)),
                ('cargos_historial', django.contrib.postgres.fields.ArrayField(base_field=django_hstore.fields.DictionaryField(), default=list, size=None)),
            ],
        ),
        migrations.CreateModel(
            name='BormeLog',
            fields=[
                ('borme', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='borme.Borme')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_parsed', models.DateTimeField(blank=True, null=True)),
                ('parsed', models.BooleanField(default=False)),
                ('errors', models.IntegerField(default=0)),
                ('path', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='anuncio',
            name='borme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='borme.Borme'),
        ),
        migrations.AddField(
            model_name='anuncio',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='borme.Company'),
        ),
        migrations.AlterIndexTogether(
            name='anuncio',
            index_together=set([('id_anuncio', 'year')]),
        ),
    ]
