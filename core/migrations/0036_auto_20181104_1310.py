# Generated by Django 2.1.2 on 2018-11-04 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0035_item_pedido_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item_pedido',
            name='quantidade',
            field=models.CharField(max_length=100),
        ),
    ]