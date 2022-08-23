# Generated by Django 4.1 on 2022-08-12 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='newBindata',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Binid', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('muncipality', models.CharField(max_length=100)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('distance', models.IntegerField()),
                ('place', models.CharField(max_length=100)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]