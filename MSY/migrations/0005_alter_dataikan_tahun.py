# Generated by Django 4.1.2 on 2022-12-10 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("MSY", "0004_alter_dataikan_tahun"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dataikan", name="tahun", field=models.IntegerField(null=True),
        ),
    ]