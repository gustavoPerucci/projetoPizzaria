# Generated by Django 2.1.2 on 2018-11-04 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_produto_valor'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='produto',
            field=models.ForeignKey(default=25, on_delete=django.db.models.deletion.CASCADE, to='core.Produto'),
            preserve_default=False,
        ),
    ]
