# Generated by Django 4.0.2 on 2022-02-17 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('alter_ego', models.CharField(max_length=250)),
                ('primary_ability', models.CharField(max_length=250)),
                ('secondary_ability', models.CharField(max_length=250)),
                ('catchphrase', models.CharField(max_length=250)),
            ],
        ),
    ]