# Generated by Django 3.1.4 on 2021-01-28 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmt', '0010_auto_20210127_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='reorder_level',
            field=models.IntegerField(default='0', null=True),
        ),
    ]
