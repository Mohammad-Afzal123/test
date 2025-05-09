# Generated by Django 5.0.9 on 2024-12-23 05:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0014_servicecollectionspage_description1_and_more'),
        ('wagtailimages', '0026_delete_uploadedimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicepage',
            name='description1',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='servicepage',
            name='description2',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='servicepage',
            name='description3',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='servicepage',
            name='service_image1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='servicepage',
            name='service_image2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='servicepage',
            name='service_image3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='serviceseparatepage',
            name='description1',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='serviceseparatepage',
            name='description2',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='serviceseparatepage',
            name='description3',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='serviceseparatepage',
            name='service_image1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='serviceseparatepage',
            name='service_image2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='serviceseparatepage',
            name='service_image3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
