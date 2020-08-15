# Generated by Django 3.1 on 2020-08-11 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=8)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=8)),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='complaint',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='complaints', to='comp.image'),
        ),
    ]
