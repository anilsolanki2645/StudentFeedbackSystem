# Generated by Django 4.0.5 on 2022-07-05 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_delete_faculties'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField()),
                ('subject1', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'lecturer',
            },
        ),
    ]
