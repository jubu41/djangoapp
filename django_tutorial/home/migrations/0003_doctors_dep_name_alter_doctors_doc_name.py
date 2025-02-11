 # Generated by Django 4.2.7 on 2024-11-08 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_doctors'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctors',
            name='dep_name',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='home.departments'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doctors',
            name='doc_name',
            field=models.CharField(max_length=255),
        ),
    ]
