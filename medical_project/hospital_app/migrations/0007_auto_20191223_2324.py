# Generated by Django 2.2.5 on 2019-12-23 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0006_patient_information'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_information',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='patient_information',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
