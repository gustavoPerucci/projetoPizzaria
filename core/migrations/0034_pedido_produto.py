# Generated by Django 2.1.2 on 2018-11-04 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_remove_pedido_produto'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='produto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Produto'),
            preserve_default=False,
        ),
    ]