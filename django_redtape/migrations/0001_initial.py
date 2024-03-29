# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 23:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_redtape.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='RedTape',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dts_activate', models.DateTimeField(auto_now_add=True)),
                ('dts_inserted', models.DateTimeField(auto_now_add=True)),
                ('dts_modified', models.DateTimeField(blank=True, null=True)),
                ('dts_archived', models.DateTimeField(blank=True, null=True)),
                ('ugp_delete', models.ForeignKey(default=django_redtape.models.default_group, on_delete=django.db.models.deletion.CASCADE, related_name='ugp_delete', to='auth.Group')),
                ('ugp_editor', models.ForeignKey(default=django_redtape.models.default_group, on_delete=django.db.models.deletion.CASCADE, related_name='ugp_editor', to='auth.Group')),
                ('ugp_modify', models.ForeignKey(default=django_redtape.models.default_group, on_delete=django.db.models.deletion.CASCADE, related_name='ugp_modify', to='auth.Group')),
                ('ugp_select', models.ForeignKey(default=django_redtape.models.default_group, on_delete=django.db.models.deletion.CASCADE, related_name='ugp_select', to='auth.Group')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
