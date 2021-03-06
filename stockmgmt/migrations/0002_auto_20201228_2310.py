# Generated by Django 3.1.4 on 2020-12-29 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmt', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='category',
            new_name='Bebida',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='last_updated',
            new_name='data_recebimento',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='issue_quantity',
            new_name='preco_compra',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='quantity',
            new_name='quantidade',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='issue_by',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='issue_to',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='item_name',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='receive_by',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='receive_quantity',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='reorder_level',
        ),
    ]
