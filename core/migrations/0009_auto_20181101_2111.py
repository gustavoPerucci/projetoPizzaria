# Generated by Django 2.1.2 on 2018-11-02 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20181101_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='codigo_pizza',
            field=models.CharField(max_length=100),
        ),
    ]
