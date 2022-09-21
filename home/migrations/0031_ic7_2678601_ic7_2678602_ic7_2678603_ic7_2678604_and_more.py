# Generated by Django 4.0.5 on 2022-07-17 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_ic6_2668601_ic6_2668602_ic6_2668603_ic6_2668604_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ic7_2678601',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_id', models.IntegerField(default=None, unique=True)),
                ('pr2678601', models.IntegerField(default=None)),
                ('pe2678601', models.IntegerField(default=None)),
                ('sk2678601', models.IntegerField(default=None)),
                ('mt2678601', models.IntegerField(null=True)),
                ('ms2678601', models.IntegerField(null=True)),
                ('pa2678601', models.IntegerField(null=True)),
                ('cs2678601', models.IntegerField(null=True)),
                ('ps2678601', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'ic7_2678601',
            },
        ),
        migrations.CreateModel(
            name='Ic7_2678602',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_id', models.IntegerField(unique=True)),
                ('pr2678602', models.IntegerField(verbose_name=2)),
                ('pe2678602', models.IntegerField(verbose_name=2)),
                ('sk2678602', models.IntegerField(verbose_name=2)),
                ('mt2678602', models.IntegerField(verbose_name=2)),
                ('ms2678602', models.IntegerField(verbose_name=2)),
                ('pa2678602', models.IntegerField(verbose_name=2)),
                ('cs2678602', models.IntegerField(verbose_name=2)),
                ('ps2678602', models.IntegerField(verbose_name=2)),
            ],
            options={
                'db_table': 'ic7_2678602',
            },
        ),
        migrations.CreateModel(
            name='Ic7_2678603',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_id', models.IntegerField(unique=True)),
                ('pr2678603', models.IntegerField(verbose_name=2)),
                ('pe2678603', models.IntegerField(verbose_name=2)),
                ('sk2678603', models.IntegerField(verbose_name=2)),
                ('mt2678603', models.IntegerField(verbose_name=2)),
                ('ms2678603', models.IntegerField(verbose_name=2)),
                ('pa2678603', models.IntegerField(verbose_name=2)),
                ('cs2678603', models.IntegerField(verbose_name=2)),
                ('ps2678603', models.IntegerField(verbose_name=2)),
            ],
            options={
                'db_table': 'ic7_2678603',
            },
        ),
        migrations.CreateModel(
            name='Ic7_2678604',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_id', models.IntegerField(unique=True)),
                ('pr2678604', models.IntegerField(verbose_name=2)),
                ('pe2678604', models.IntegerField(verbose_name=2)),
                ('sk2678604', models.IntegerField(verbose_name=2)),
                ('mt2678604', models.IntegerField(verbose_name=2)),
                ('ms2678604', models.IntegerField(verbose_name=2)),
                ('pa2678604', models.IntegerField(verbose_name=2)),
                ('cs2678604', models.IntegerField(verbose_name=2)),
                ('ps2678604', models.IntegerField(verbose_name=2)),
            ],
            options={
                'db_table': 'ic7_2678604',
            },
        ),
        migrations.CreateModel(
            name='Ic7_2678605',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_id', models.IntegerField(unique=True)),
                ('pr2678605', models.IntegerField(verbose_name=2)),
                ('pe2678605', models.IntegerField(verbose_name=2)),
                ('sk2678605', models.IntegerField(verbose_name=2)),
                ('mt2678605', models.IntegerField(verbose_name=2)),
                ('ms2678605', models.IntegerField(verbose_name=2)),
                ('pa2678605', models.IntegerField(verbose_name=2)),
                ('cs2678605', models.IntegerField(verbose_name=2)),
                ('ps2678605', models.IntegerField(verbose_name=2)),
            ],
            options={
                'db_table': 'ic7_2678605',
            },
        ),
    ]
