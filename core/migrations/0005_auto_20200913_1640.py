# Generated by Django 2.2 on 2020-09-13 16:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_about'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Addresses'},
        ),
        migrations.RemoveField(
            model_name='address',
            name='address',
        ),
        migrations.AddField(
            model_name='address',
            name='address_type',
            field=models.CharField(choices=[('B', 'Billing'), ('S', 'Shipping')], default=django.utils.timezone.now, max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='apartment_address',
            field=models.CharField(default=datetime.datetime(2020, 9, 13, 16, 39, 36, 591241, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='street_address',
            field=models.CharField(default=datetime.datetime(2020, 9, 13, 16, 39, 48, 514526, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
        migrations.AlterField(
            model_name='address',
            name='zip',
            field=models.CharField(max_length=100),
        ),
    ]
