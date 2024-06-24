# Generated by Django 4.1.10 on 2023-12-13 11:07

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('settings', '0010_alter_setting_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatPrompt',
            fields=[
                ('created_by', models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by')),
                ('updated_by', models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('comment', models.TextField(blank=True, default='', verbose_name='Comment')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Name')),
                ('content', models.TextField(verbose_name='Content')),
                ('builtin', models.BooleanField(default=False, verbose_name='Builtin')),
            ],
            options={
                'verbose_name': 'Chat prompt',
            },
        ),
    ]