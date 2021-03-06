# Generated by Django 3.1.2 on 2020-10-10 16:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('acknowledge', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='standarduser',
            name='menu_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='standarduser',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Standard_user', to='acknowledge.ack_substandardsmenu'),
        ),
        migrations.AddField(
            model_name='publicationuser',
            name='menu_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='publicationuser',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='public_user', to='acknowledge.ack_subpublicationmenu'),
        ),
        migrations.AddField(
            model_name='navyuser',
            name='menu_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='navyuser',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Navy_user', to='acknowledge.ack_subnavy_orderssmenu'),
        ),
        migrations.AddField(
            model_name='knowledgeuser',
            name='menu_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='knowledgeuser',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='menu_user', to='acknowledge.ack_submenu'),
        ),
        migrations.AddField(
            model_name='instructionuser',
            name='menu_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='instructionuser',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Instruction_user', to='acknowledge.ack_subnavy_instructionssmenu'),
        ),
        migrations.AddField(
            model_name='guidelinesuser',
            name='menu_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='guidelinesuser',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Guide_user', to='acknowledge.ack_subguidelinesmenu'),
        ),
        migrations.AddField(
            model_name='graphdetailused',
            name='menu_detail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='graph_detail', to='acknowledge.graphdetail'),
        ),
        migrations.AddField(
            model_name='graphdetailused',
            name='menu_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='graphdetail',
            name='menu_detail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ask_submenudetail', to='acknowledge.acknoledge_menu'),
        ),
        migrations.AddField(
            model_name='brsmenu',
            name='parent_ob',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acknowledge.brsmenu'),
        ),
        migrations.AddField(
            model_name='acknoledge_menu',
            name='parent',
            field=models.ForeignKey(blank=True, limit_choices_to={'id': 2}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='main_menu', to='acknowledge.parent_menu'),
        ),
        migrations.AddField(
            model_name='ack_substandardsmenu',
            name='parent',
            field=models.ForeignKey(blank=True, limit_choices_to={'id': 6}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ask_substandardsmenues', to='acknowledge.acknoledge_menu'),
        ),
        migrations.AddField(
            model_name='ack_substandardsmenu',
            name='parent_ob',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acknowledge.ack_substandardsmenu'),
        ),
        migrations.AddField(
            model_name='ack_subpublicationmenu',
            name='parent',
            field=models.ForeignKey(blank=True, limit_choices_to={'id': 2}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ask_subpublicationmenues', to='acknowledge.acknoledge_menu'),
        ),
        migrations.AddField(
            model_name='ack_subpublicationmenu',
            name='parent_ob',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acknowledge.ack_subpublicationmenu'),
        ),
        migrations.AddField(
            model_name='ack_subnhqe_librarylinesmenu',
            name='parent_ob',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acknowledge.ack_subnhqe_librarylinesmenu'),
        ),
        migrations.AddField(
            model_name='ack_subnavy_orderssmenu',
            name='parent',
            field=models.ForeignKey(blank=True, limit_choices_to={'id': 3}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ask_subnavy_ordersmenues', to='acknowledge.acknoledge_menu'),
        ),
        migrations.AddField(
            model_name='ack_subnavy_orderssmenu',
            name='parent_ob',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acknowledge.ack_subnavy_orderssmenu'),
        ),
        migrations.AddField(
            model_name='ack_subnavy_instructionssmenu',
            name='parent',
            field=models.ForeignKey(blank=True, limit_choices_to={'id': 4}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ask_subnavy_instructionmenues', to='acknowledge.acknoledge_menu'),
        ),
        migrations.AddField(
            model_name='ack_subnavy_instructionssmenu',
            name='parent_ob',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acknowledge.ack_subnavy_instructionssmenu'),
        ),
        migrations.AddField(
            model_name='ack_submenupolicyfile',
            name='parent_ob',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ack_submenu_children', to='acknowledge.ack_submenu'),
        ),
        migrations.AddField(
            model_name='ack_submenu',
            name='parent',
            field=models.ForeignKey(blank=True, limit_choices_to={'id': 1}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ask_submenues', to='acknowledge.acknoledge_menu'),
        ),
        migrations.AddField(
            model_name='ack_submenu',
            name='parent_ob',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='acknowledge.ack_submenu'),
        ),
        migrations.AddField(
            model_name='ack_subguidelinesmenu',
            name='parent',
            field=models.ForeignKey(blank=True, limit_choices_to={'id': 5}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ask_subguidelinesmenues', to='acknowledge.acknoledge_menu'),
        ),
        migrations.AddField(
            model_name='ack_subguidelinesmenu',
            name='parent_ob',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acknowledge.ack_subguidelinesmenu'),
        ),
        migrations.AddField(
            model_name='ack_standardsname',
            name='parent_ob',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='standardFileMenues', to='acknowledge.ack_substandardsmenu'),
        ),
        migrations.AddField(
            model_name='ack_publicationname',
            name='parent_ob',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ack_publication_children', to='acknowledge.ack_subpublicationmenu'),
        ),
        migrations.AddField(
            model_name='ack_publicationfile',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ack_policypolicyfile',
            name='parent_file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ask_policyfile', to='acknowledge.ack_policyname'),
        ),
        migrations.AddField(
            model_name='ack_policypolicyfile',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ack_policyname',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='policy_name', to='acknowledge.ack_submenu'),
        ),
        migrations.AddField(
            model_name='ack_policyname',
            name='parent_ob',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acknowledge.ack_policyname'),
        ),
        migrations.AddField(
            model_name='ack_navyname',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='navyOrders_name', to='acknowledge.ack_subnavy_orderssmenu'),
        ),
        migrations.AddField(
            model_name='ack_navyname',
            name='parent_ob',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acknowledge.ack_navyname'),
        ),
        migrations.AddField(
            model_name='ack_navyinstructionname',
            name='parent_ob',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='navyinstruction_name', to='acknowledge.ack_subnavy_instructionssmenu'),
        ),
        migrations.AddField(
            model_name='ack_guidelinesname',
            name='parent_ob',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='guidelinesMenues', to='acknowledge.ack_subguidelinesmenu'),
        ),
    ]
