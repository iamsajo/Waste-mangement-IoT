# Generated by Django 4.1 on 2022-08-12 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muncipality', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newbindata',
            name='Binid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='newbindata',
            name='capacity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='newbindata',
            name='distance',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='newbindata',
            name='latitude',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='newbindata',
            name='longitude',
            field=models.FloatField(default=0),
        ),
    ]
