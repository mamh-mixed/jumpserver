# Generated by Django 3.1.14 on 2022-03-08 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0021_auto_20220308_1910'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticketstep',
            options={'default_permissions': [], 'verbose_name': 'Ticket step'},
        ),
    ]
