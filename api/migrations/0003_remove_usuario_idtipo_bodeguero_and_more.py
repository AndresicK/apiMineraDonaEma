# Generated by Django 4.1.3 on 2022-12-02 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_usuario_idtipo_bodeguero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='idTipo_bodeguero',
        ),
        migrations.AddField(
            model_name='usuario',
            name='idTipo_bodeguero_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.tipo_bodeguero'),
        ),
    ]
