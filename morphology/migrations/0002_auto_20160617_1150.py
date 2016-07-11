# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-17 09:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('morphology', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dialect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('abbreviation', models.CharField(max_length=5)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=30)),
                ('annotation', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('abbreviation', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Lemma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=30)),
                ('POS', models.CharField(max_length=10)),
                ('to_language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='morphology.Language')),
            ],
            options={
                'verbose_name_plural': 'Lemmata',
            },
        ),
        migrations.CreateModel(
            name='NormalizationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examples', models.TextField(blank=True)),
                ('exceptions', models.TextField(blank=True)),
                ('to_additional_language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='morphology.Language')),
                ('to_dialect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='morphology.Dialect')),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transcription', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TokenToForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField()),
                ('to_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='morphology.Form')),
                ('to_token', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='morphology.Token')),
            ],
        ),
        migrations.AddField(
            model_name='token',
            name='to_forms',
            field=models.ManyToManyField(through='morphology.TokenToForm', to='morphology.Form'),
        ),
        migrations.AddField(
            model_name='form',
            name='to_lemma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='morphology.Lemma', verbose_name='to lemma(ta)'),
        ),
        migrations.AddField(
            model_name='dialect',
            name='to_language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='morphology.Language'),
        ),
    ]