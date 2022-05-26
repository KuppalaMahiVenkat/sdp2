# Generated by Django 3.1.7 on 2021-05-12 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DEMOAPP', '0014_signup1'),
    ]

    operations = [
        migrations.CreateModel(
            name='personalbanking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.CharField(max_length=9)),
                ('AN', models.CharField(max_length=16)),
                ('CN', models.CharField(max_length=11)),
                ('Amt', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'personal',
            },
        ),
    ]