# Generated by Django 4.1.4 on 2022-12-19 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0003_alter_expired_payments_pay_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment_user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
