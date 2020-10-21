# Generated by Django 3.1.2 on 2020-10-17 17:19

import acknowledge.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acknowledge', '0014_ack_subnavy_orderssmenu_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='ack_subguidelinesmenu',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='guidelines/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'PDF', 'png', 'jpg', 'JPEG']), acknowledge.models.newvalidate_image]),
        ),
    ]
