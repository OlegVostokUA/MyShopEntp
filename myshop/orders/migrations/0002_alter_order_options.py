# Generated by Django 5.0.6 on 2024-06-11 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created',), 'verbose_name': 'Замовлення', 'verbose_name_plural': 'Замовлення'},
        ),
    ]
