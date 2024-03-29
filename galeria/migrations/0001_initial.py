# Generated by Django 3.2.4 on 2021-06-14 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de categoría')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre de la categpria')),
            ],
        ),
        migrations.CreateModel(
            name='obradearte',
            fields=[
                ('nombreobra', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='nombreobra')),
                ('dimenciones', models.CharField(blank=True, max_length=15, verbose_name='dimenciones')),
                ('añocreacion', models.CharField(blank=True, max_length=6, null=True, verbose_name='año de creacion')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='galeria.categoria')),
            ],
        ),
    ]
