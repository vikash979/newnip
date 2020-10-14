# Generated by Django 3.1.2 on 2020-10-10 16:05

import acknowledge.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ack_guidelinesname',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('submenu_name', models.CharField(max_length=200, unique=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='guidelines/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'PDF', 'png', 'jpg', 'JPEG']), acknowledge.models.newvalidate_image])),
            ],
        ),
        migrations.CreateModel(
            name='ack_NavyInstructionname',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('submenu_name', models.CharField(max_length=200, unique=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='navy_instruction/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'PDF', 'png', 'jpg', 'JPEG']), acknowledge.models.validate_image])),
            ],
        ),
        migrations.CreateModel(
            name='ack_Navyname',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('submenu_name', models.CharField(max_length=200, unique=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='navy_orders/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'PDF', 'png', 'jpg', 'JPEG']), acknowledge.models.validate_image])),
            ],
        ),
        migrations.CreateModel(
            name='ack_policyname',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('policy_name', models.CharField(max_length=200, unique=True)),
                ('folder_type', models.SmallIntegerField(choices=[(1, 'One'), (2, 'Two')], default=2)),
                ('menu_type', models.SmallIntegerField(choices=[(1, 'One'), (2, 'Two')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='ack_policypolicyfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateField(auto_now_add=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='policy/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'PDF'])])),
                ('updated_on', models.DateField(auto_now=True, null=True)),
                ('policies_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ack_publicationfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateField(auto_now_add=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='publication/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'PDF'])])),
                ('updated_on', models.DateField(auto_now=True, null=True)),
                ('publication_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ack_publicationname',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('submenu_name', models.CharField(max_length=200, unique=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='publicattion/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'PDF'])])),
                ('publication_file', models.ImageField(blank=True, null=True, upload_to='pub_image/', validators=[acknowledge.models.ack_publicationname.validate_image, django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'JPEG'])], verbose_name='public_image')),
            ],
        ),
        migrations.CreateModel(
            name='ack_Standardsname',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('submenu_name', models.CharField(max_length=200, unique=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='standards_file/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'PDF', 'png', 'jpg', 'JPEG']), acknowledge.models.validate_image])),
                ('folder_title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ack_subGuidelinesmenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_type', models.SmallIntegerField(choices=[(1, 'One'), (2, 'Two')], default=1)),
                ('folder_type', models.SmallIntegerField(choices=[(1, 'One'), (2, 'Two')], default=2)),
                ('added_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('submenu_name', models.CharField(max_length=200, unique=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='guidelines/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'JPEG']), acknowledge.models.newvalidate_image])),
                ('file_type', models.SmallIntegerField(choices=[(1, 'pb'), (2, 'mat'), (3, 'sb1'), (4, 'sb2'), (5, 'misl')], default=5)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Ack_submenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateField(auto_now=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('submenu_name', models.CharField(max_length=200)),
                ('menu_type', models.SmallIntegerField(choices=[(1, 'One'), (2, 'Two')], default=1)),
                ('folder_type', models.SmallIntegerField(choices=[(1, 'One'), (2, 'Two')], default=2)),
                ('status', models.SmallIntegerField(choices=[(1, 'one '), (2, 'two')], default=2)),
                ('file_type', models.SmallIntegerField(choices=[(1, 'pb'), (2, 'mat'), (3, 'sb1'), (4, 'sb2'), (5, 'misl')], default=5)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ack_subMenuPolicyFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateField(auto_now=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('submenu_name', models.CharField(max_length=200)),
                ('file', models.FileField(blank=True, null=True, upload_to='policy/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'PDF'])])),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ack_subNavy_Instructionssmenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('submenu_name', models.CharField(max_length=200, unique=True)),
                ('menu_type', models.SmallIntegerField(choices=[(1, 'One'), (2, 'Two')], default=1)),
                ('folder_type', models.SmallIntegerField(choices=[(1, 'One'), (2, 'Two')], default=2)),
                ('file', models.FileField(blank=True, null=True, upload_to='navy_instructionfile/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'PDF', 'png', 'jpg', 'JPEG']), acknowledge.models.validate_image])),
                ('file_type', models.SmallIntegerField(choices=[(1, 'pb'), (2, 'mat'), (3, 'sb1'), (4, 'sb2'), (5, 'misl')], default=5)),
            ],
        ),
        migrations.CreateModel(
            name='ack_subNavy_Orderssmenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('submenu_name', models.CharField(max_length=200, unique=True)),
                ('menu_type', models.SmallIntegerField(choices=[(1, 'One'), (2, 'Two')], default=1)),
                ('folder_type', models.SmallIntegerField(choices=[(1, 'One'), (2, 'Two')], default=2)),
                ('file', models.FileField(blank=True, null=True, upload_to='navy_ordersfile/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'PDF', 'png', 'jpg', 'JPEG']), acknowledge.models.validate_image])),
                ('file_type', models.SmallIntegerField(choices=[(1, 'pb'), (2, 'mat'), (3, 'sb1'), (4, 'sb2'), (5, 'misl')], default=5)),
            ],
        ),
        migrations.CreateModel(
            name='ack_subNHQe_Librarylinesmenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('submenu_name', models.CharField(max_length=200, unique=True)),
                ('menu_type', models.SmallIntegerField(choices=[(1, 'One'), (2, 'Two')], default=1)),
                ('folder_type', models.SmallIntegerField(choices=[(1, 'One'), (2, 'Two')], default=2)),
                ('file', models.FileField(blank=True, null=True, upload_to='elibraryfiles/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'PDF', 'png', 'jpg', 'JPEG']), acknowledge.models.validate_image])),
                ('folder_title', models.CharField(max_length=200)),
                ('navyinstructionfile', models.FileField(blank=True, null=True, upload_to='elibrary/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'PDF', 'png', 'jpg', 'JPEG']), acknowledge.models.validate_image])),
            ],
        ),
        migrations.CreateModel(
            name='ack_subpublicationmenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('submenu_name', models.CharField(max_length=200, unique=True)),
                ('menu_type', models.SmallIntegerField(choices=[(1, 'One'), (2, 'Two')], default=1)),
                ('folder_type', models.SmallIntegerField(choices=[(1, 'One'), (2, 'Two')], default=2)),
                ('publicationicon', models.FileField(blank=True, null=True, upload_to='publicattion/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'JPEG'])])),
                ('file_type', models.SmallIntegerField(choices=[(1, 'pb'), (2, 'mat'), (3, 'sb1'), (4, 'sb2'), (5, 'misl')], default=5)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ack_subStandardsmenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('submenu_name', models.CharField(max_length=200, unique=True)),
                ('menu_type', models.SmallIntegerField(choices=[(1, 'One'), (2, 'Two')], default=1)),
                ('folder_type', models.SmallIntegerField(choices=[(1, 'One'), (2, 'Two')], default=2)),
                ('file', models.FileField(blank=True, null=True, upload_to='standards_file/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'PDF', 'png', 'jpg', 'JPEG']), acknowledge.models.validate_image])),
                ('file_type', models.SmallIntegerField(choices=[(1, 'pb'), (2, 'mat'), (3, 'sb1'), (4, 'sb2'), (5, 'misl')], default=5)),
            ],
        ),
        migrations.CreateModel(
            name='acknoledge_menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('menu_name', models.CharField(max_length=200, unique=True)),
                ('url_link', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='BRsmenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('submenu_name', models.CharField(max_length=200, unique=True)),
                ('menu_type', models.SmallIntegerField(choices=[(1, 'One'), (2, 'Two')], default=1)),
                ('folder_type', models.SmallIntegerField(choices=[(1, 'One'), (2, 'Two')], default=2)),
                ('file', models.FileField(blank=True, null=True, upload_to='brsfiles/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'PDF', 'png', 'jpg', 'JPEG']), acknowledge.models.validate_image])),
                ('folder_title', models.CharField(max_length=200)),
                ('navyinstructionfile', models.FileField(blank=True, null=True, upload_to='brsfoldermenus/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'PDF', 'png', 'jpg', 'JPEG']), acknowledge.models.validate_image])),
            ],
        ),
        migrations.CreateModel(
            name='graphDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateField(auto_now=True)),
                ('updated_on', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='graphDetailUsed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateField(auto_now=True)),
                ('updated_on', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='GuideLinesUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='InstructionUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='KnowledgeUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='NavyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='parent_menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('menu_name', models.CharField(max_length=200, unique=True)),
                ('menu_url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PublicationUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='StandardUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
