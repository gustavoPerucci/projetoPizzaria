# Generated by Django 2.1.2 on 2018-11-04 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_remove_item_pedido_valor'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
            preserve_default=False,
        ),
    ]
