# Generated by Django 3.1.2 on 2020-10-21 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acknowledge', '0018_auto_20201017_1759'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadPdf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resumes', models.FileField(blank=True, null=True, upload_to='policy/')),
            ],
        ),
    ]