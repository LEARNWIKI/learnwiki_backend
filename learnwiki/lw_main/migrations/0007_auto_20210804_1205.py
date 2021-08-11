# Generated by Django 3.2.5 on 2021-08-04 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lw_main', '0006_auto_20210803_2231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='edge',
            name='direction',
        ),
        migrations.RemoveField(
            model_name='edge',
            name='node_1',
        ),
        migrations.RemoveField(
            model_name='edge',
            name='node_2',
        ),
        migrations.AddField(
            model_name='edge',
            name='is_bidirectional',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='edge',
            name='node_in',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='edges_in', to='lw_main.node'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='edge',
            name='node_out',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='edges_out', to='lw_main.node'),
            preserve_default=False,
        ),
    ]