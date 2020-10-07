# Generated by Django 3.1.1 on 2020-10-07 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20201004_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='stock10',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stock',
            name='stock2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stock',
            name='stock3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stock',
            name='stock4',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stock',
            name='stock5',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stock',
            name='stock6',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stock',
            name='stock7',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stock',
            name='stock8',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stock',
            name='stock9',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='trade',
            name='stock',
            field=models.CharField(choices=[('stock1', 'stock1'), ('stock2', 'stock2'), ('stock3', 'stock3'), ('stock4', 'stock4'), ('stock5', 'stock5'), ('stock6', 'stock6'), ('stock7', 'stock7'), ('stock8', 'stock8'), ('stock9', 'stock9'), ('stock10', 'stock10')], max_length=100),
        ),
        migrations.AlterField(
            model_name='trade',
            name='userbalance',
            field=models.FloatField(default=1000000.0),
        ),
    ]
