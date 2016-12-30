# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('isbn', models.CharField(max_length=20)),
                ('language', models.CharField(default=b'kh', max_length=2, choices=[(b'kh', b'Khmer'), (b'en', b'English')])),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]
