# Generated by Django 3.1.7 on 2021-05-12 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DEMOAPP', '0015_personalbanking'),
    ]

    operations = [
        migrations.CreateModel(
            name='personalbanking1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AN', models.CharField(max_length=16)),
                ('CN', models.CharField(max_length=11)),
                ('Amt', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'personal1',
            },
        ),
    ]
