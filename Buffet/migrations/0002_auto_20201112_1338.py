# Generated by Django 2.2 on 2020-11-12 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Buffet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acompaniante',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Bebida',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Platillo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='mesa',
            name='status',
            field=models.CharField(choices=[('LB', 'Libre'), ('RS', 'Reservada'), ('OP', 'Ocupada'), ('NO', 'No Disponible')], default='Libre', max_length=2),
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('num_trj', models.CharField(max_length=20)),
                ('fechaV', models.DateField()),
                ('codSeg', models.CharField(max_length=5)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Buffet.Cliente')),
            ],
        ),
    ]
