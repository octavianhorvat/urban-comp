# Generated by Django 3.1 on 2020-08-11 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='LicencePlate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('licence_plate', models.CharField(max_length=60)),
                ('insurance', models.DateField()),
                ('address', models.CharField(max_length=60)),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField()),
            ],
        ),
    ]