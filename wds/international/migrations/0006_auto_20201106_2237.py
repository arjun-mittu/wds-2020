# Generated by Django 3.1.1 on 2020-11-06 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('international', '0005_delete_loggedinuserinternational'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='priceperstock',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]
