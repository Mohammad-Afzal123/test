# Generated by Django 5.0.9 on 2024-12-13 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_remove_serviceindexpage_services_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicecollectionspage',
            name='botton_text',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='serviceindexpage',
            name='botton_text',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='serviceindividualpage',
            name='botton_text',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='servicepage',
            name='botton_text',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='serviceseparatepage',
            name='botton_text',
            field=models.TextField(blank=True, max_length=255),
        ),
    ]
