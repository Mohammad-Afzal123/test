# Generated by Django 5.0.9 on 2024-12-15 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0011_alter_servicecategory_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicecategory',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
