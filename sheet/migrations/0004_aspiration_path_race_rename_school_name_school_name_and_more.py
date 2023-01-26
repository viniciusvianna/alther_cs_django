# Generated by Django 4.1.5 on 2023-01-24 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0003_rename_schools_school'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aspiration',
            fields=[
                ('aspiration_ID', models.CharField(db_column='AspirationID', max_length=3, primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='AspirationName', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Path',
            fields=[
                ('path_ID', models.CharField(db_column='PathID', max_length=3, primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='PathName', max_length=30)),
                ('tier', models.PositiveSmallIntegerField(choices=[(1, 'Basic'), (2, 'Advanced'), (3, 'Specialist')], default=1)),
                ('requirements', models.JSONField()),
                ('master_bonus', models.CharField(db_column='MasterBonus', max_length=150)),
                ('aspiration', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sheet.aspiration')),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('race_ID', models.CharField(db_column='RaceID', max_length=3, primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='RaceName', max_length=20)),
            ],
        ),
        migrations.RenameField(
            model_name='school',
            old_name='school_name',
            new_name='name',
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='SkillName', max_length=100)),
                ('description', models.TextField()),
                ('cost', models.PositiveIntegerField()),
                ('category', models.CharField(choices=[('ITS', 'Intrínseca'), ('GEN', 'Padrão'), ('SUP', 'Suporte'), ('REA', 'Reação'), ('MOV', 'Movimento'), ('PER', 'Perfeita')], default='GEN', max_length=3)),
                ('path', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sheet.path')),
            ],
        ),
        migrations.CreateModel(
            name='RaceTrait',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('A', 'Ability'), ('P', 'Penalty')], max_length=1)),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sheet.race')),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('origin', models.CharField(max_length=30)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=6)),
                ('height', models.DecimalField(decimal_places=2, max_digits=5)),
                ('age', models.PositiveSmallIntegerField()),
                ('level', models.PositiveSmallIntegerField()),
                ('xp_total', models.PositiveIntegerField()),
                ('xp_current', models.PositiveIntegerField()),
                ('hp_total', models.IntegerField()),
                ('hp_current', models.IntegerField()),
                ('hp_temp', models.IntegerField()),
                ('unbalance', models.PositiveIntegerField()),
                ('movement_actions', models.PositiveSmallIntegerField()),
                ('main_actions', models.PositiveSmallIntegerField()),
                ('inventory', models.TextField()),
                ('annotations', models.TextField()),
                ('coin', models.CharField(max_length=200)),
                ('active_path', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sheet.path')),
                ('aspiration', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sheet.aspiration')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sheet.race')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sheet.school')),
            ],
        ),
    ]