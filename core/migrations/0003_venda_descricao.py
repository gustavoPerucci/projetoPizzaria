# Generated by Django 2.1.2 on 2018-10-20 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20181020_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='descricao',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
