# Generated by Django 2.1.2 on 2018-10-26 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplication_1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model1',
            name='var3',
            field=models.CharField(max_length=30),
        ),
    ]
