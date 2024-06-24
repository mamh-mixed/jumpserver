# Generated by Django 4.1.10 on 2023-10-25 02:45

from django.db import migrations, models

import perms.models.asset_permission


class Migration(migrations.Migration):

    dependencies = [
        ('perms', '0034_auto_20230525_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetpermission',
            name='protocols',
            field=models.JSONField(default=perms.models.asset_permission.default_protocols, verbose_name='Protocols'),
        ),
    ]