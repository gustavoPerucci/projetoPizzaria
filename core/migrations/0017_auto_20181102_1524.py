# Generated by Django 2.1.2 on 2018-11-02 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20181102_1445'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='acrecimos',
            new_name='acrecimo',
        ),
    ]
