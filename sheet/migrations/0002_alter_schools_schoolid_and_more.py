# Generated by Django 4.1.5 on 2023-01-19 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schools',
            name='SchoolID',
            field=models.CharField(db_column='SchoolID', max_length=3, primary_key=True, serialize=False, verbose_name='School ID'),
        ),
        migrations.RenameField(
            model_name='schools',
            old_name='SchoolID',
            new_name='school_ID',
        ),
        migrations.AlterField(
            model_name='schools',
            name='SchoolName',
            field=models.CharField(db_column='SchoolName', max_length=50, verbose_name='School Name'),
        ),
        migrations.RenameField(
            model_name='schools',
            old_name='SchoolName',
            new_name='school_name',
        ),
    ]
