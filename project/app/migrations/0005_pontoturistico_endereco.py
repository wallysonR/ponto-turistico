# Generated by Django 3.1 on 2020-08-22 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0001_initial'),
        ('app', '0004_auto_20200821_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='endereco',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='endereco.endereco'),
            preserve_default=False,
        ),
    ]
