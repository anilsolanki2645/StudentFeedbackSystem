# Generated by Django 4.0.5 on 2022-07-06 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_ic3_2638603_ic3_2638604_ic3_2638605'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sem_serve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semserve', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'sem_serve',
            },
        ),
    ]
