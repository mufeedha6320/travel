# Generated by Django 4.2.3 on 2023-08-03 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel1app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='table_team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='my_pics')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
