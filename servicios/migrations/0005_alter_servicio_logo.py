# Generated by Django 4.1.4 on 2022-12-21 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0004_alter_payment_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='Logo',
            field=models.ImageField(upload_to='images'),
        ),
    ]
