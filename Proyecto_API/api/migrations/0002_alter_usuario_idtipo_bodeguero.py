# Generated by Django 4.1.3 on 2022-12-02 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='idTipo_bodeguero',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.tipo_bodeguero'),
        ),
    ]
