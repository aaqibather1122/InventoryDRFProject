# Generated by Django 5.1.4 on 2025-01-30 08:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(choices=[('credit_card', 'Credit Card'), ('cash', 'Cash')], max_length=50)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount_received', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount_return', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('payment_status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed'), ('refunded', 'Refunded')], max_length=20)),
                ('transaction_id', models.CharField(blank=True, max_length=100, null=True)),
                ('stripe_payment_intent_id', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='order.order')),
            ],
        ),
    ]
