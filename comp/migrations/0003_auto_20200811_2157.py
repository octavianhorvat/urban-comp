# Generated by Django 3.1 on 2020-08-11 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comp', '0002_auto_20200811_2152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='image',
        ),
        migrations.AddField(
            model_name='complaint',
            name='image',
            field=models.ManyToManyField(null=True, related_name='complaints', to='comp.Image'),
        ),
    ]