# Generated by Django 5.0.9 on 2024-12-13 17:20

import modelcluster.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_remove_servicecollectionspage_services_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviceindexpage',
            name='services',
        ),
        migrations.AddField(
            model_name='serviceindividualpage',
            name='services',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, related_name='service_index_pages', to='services.servicepage'),
        ),
    ]
