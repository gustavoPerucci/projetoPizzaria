# Generated by Django 2.1.2 on 2018-11-02 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20181024_1416'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='acrecimos',
        ),
        migrations.AddField(
            model_name='produto',
            name='codigo_pizza',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
            preserve_default=False,
        ),
    ]
