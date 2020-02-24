# Generated by Django 2.2.5 on 2019-12-23 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0003_auto_20191222_1149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_id', models.CharField(max_length=128)),
                ('hospital_name', models.CharField(max_length=128)),
                ('location', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]