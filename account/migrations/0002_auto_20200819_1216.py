# Generated by Django 3.1 on 2020-08-19 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.ForeignKey(max_length=200, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.address'),
        ),
    ]
