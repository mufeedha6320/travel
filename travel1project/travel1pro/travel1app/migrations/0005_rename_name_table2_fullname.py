# Generated by Django 4.2.3 on 2023-08-03 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel1app', '0004_table2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table2',
            old_name='name',
            new_name='fullname',
        ),
    ]
