# Generated by Django 3.1.7 on 2021-05-07 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DEMOAPP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='password',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterModelTable(
            name='post',
            table='userlogin',
        ),
    ]