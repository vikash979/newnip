# Generated by Django 3.1.2 on 2020-10-17 12:02

import acknowledge.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acknowledge', '0011_ack_submenu_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='ack_subpublicationmenu',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='publicattion/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'PDF'])]),
        ),
        migrations.AddField(
            model_name='ack_subpublicationmenu',
            name='publication_file',
            field=models.ImageField(blank=True, null=True, upload_to='pub_image/', validators=[acknowledge.models.validate_image, django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'JPEG'])]),
        ),
    ]