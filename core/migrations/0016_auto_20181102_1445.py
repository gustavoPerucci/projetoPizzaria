# Generated by Django 2.1.2 on 2018-11-02 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20181102_1439'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='acrecimo',
        ),
        migrations.AddField(
            model_name='produto',
            name='acrecimos',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]