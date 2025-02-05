# Generated by Django 5.1.5 on 2025-01-31 04:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacionapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PagoStripe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_payment_id', models.CharField(max_length=100, unique=True)),
                ('monto_pagado', models.FloatField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('factura', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pago_stripe', to='facturacionapp.factura')),
            ],
        ),
    ]
