# Generated by Django 4.0.5 on 2022-07-06 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_ic3_2638601_pr2638601_alter_ic3_2638601_std_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ic3_2638601',
            name='pr2638601',
            field=models.PositiveIntegerField(max_length=2),
        ),
        migrations.AlterField(
            model_name='ic3_2638601',
            name='std_id',
            field=models.IntegerField(unique=True),
        ),
    ]
