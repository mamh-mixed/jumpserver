# Generated by Django 3.1.14 on 2022-03-08 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0023_auto_20220308_1917'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={'default_permissions': [], 'ordering': ('-date_created',), 'permissions': {('add_ticket', 'Can add ticket'), ('view_ticket', 'Can view ticket')}, 'verbose_name': 'Ticket'},
        ),
    ]
