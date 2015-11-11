# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20151109_1728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='docfile',
            new_name='userImage',
        ),
    ]
