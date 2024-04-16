# Generated by Django 4.2.4 on 2024-04-16 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_order_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Payment Initiated', 'Payment Initiated'), ('Order Placed', 'Order Placed'), ('Order Processing', 'Order Processing'), ('Packed', 'Packed'), ('Ready For Dispatch', 'Ready For Dispatch'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='Pending', max_length=20, verbose_name='Status'),
        ),
    ]
