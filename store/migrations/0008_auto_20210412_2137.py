# Generated by Django 2.2 on 2021-04-12 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='Admin Place', max_length=200),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.IntegerField(default='45645645'),
        ),
    ]
