# Generated by Django 2.2 on 2020-11-19 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buffet', '0004_auto_20201118_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='qr_code',
            field=models.ImageField(blank=True, upload_to='media/qr'),
        ),
    ]