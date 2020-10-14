from django.db import models
from django.conf import settings

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import User
from django.conf import settings
from datetime import date, datetime
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.core.validators import FileExtensionValidator
import datetime



# class Comment_policy(models.Model):
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.CharField(max_length=50)
#     content_object = GenericForeignKey('content_type', 'object_id')
#     #text = models.TextField(blank=True)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,on_delete=models.SET_NULL)
#     added_on = models.DateTimeField(auto_now_add=True, null=True)
#     file = models.FileField(upload_to='policy/',blank=True,null=True,validators=[FileExtensionValidator(allowed_extensions=['pdf','PDF'])])
#     updated_on = models.DateTimeField(auto_now=True,null=True)




class acknowledge_parent_menu(models.Model):
    added_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    menu_name =  models.CharField(max_length=200,unique=True)
    def __str__(self):
        return self.menu_name

class acknoledge_menu(models.Model):
    menu_choice = (
        (1, "One"),
        (2, "Two"),
    )

    added_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    menu_name =  models.CharField(max_length=200,unique=True)
   # parent = models.ForeignKey(acknowledge_parent_menu,null=True, related_name ="acknoledge_menues" , blank=True, on_delete=models.SET_NULL)
    ###############################late
    #parent_ob  = models.ForeignKey("self",null=True, blank=True, on_delete=models.SET_NULL)
    #menu_type = models.SmallIntegerField(choices=menu_choice, default=1)
   # file = models.FileField(upload_to='study_material/notes/',blank=True,null=True,validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    #folder_type = models.SmallIntegerField(choices=folder_choice, default=2)
    url_link= models.URLField(max_length = 200, blank=True)

    def __str__(self):
    	return self.menu_name


class ack_submenu(models.Model):
    menu_choice = (
        (1, "One"),
        (2, "Two"),
    )
    folder_choice = (
        (1, "One"),
        (2, "Two"),
    )

    added_on = models.DateField(auto_now=True)
    updated_on = models.DateField(auto_now=True)
    submenu_name =  models.CharField(max_length=200)
    parent_ob  = models.ForeignKey("self",null=True, blank=True, related_name='children',  on_delete=models.SET_NULL)
    menu_type = models.SmallIntegerField(choices=menu_choice, default=1)

    folder_type = models.SmallIntegerField(choices=folder_choice, default=2)
    folder_title =  models.CharField(max_length=200)
    file = models.FileField(upload_to='policy/',blank=True,null=True,validators=[FileExtensionValidator(allowed_extensions=['pdf','PDF'])])
    parent = models.ForeignKey(acknoledge_menu,null=True, related_name ="ask_submenues" , limit_choices_to={'id': 1}, blank=True, on_delete=models.SET_NULL)
    ##############################late



    def __str__(self):
        return self.submenu_name


    class Meta:
        ordering = ['-id']



class ack_subMenuPolicyFile(models.Model):
    # menu_choice = (
    #     (1, "One"),
    #     (2, "Two"),
    # )
    # folder_choice = (
    #     (1, "One"),
    #     (2, "Two"),
    # )

    added_on = models.DateField(auto_now=True)
    updated_on = models.DateField(auto_now=True)
    submenu_name =  models.CharField(max_length=200)
    parent_ob  = models.ForeignKey(ack_submenu,null=True, blank=True,related_name='ack_submenu_children', on_delete=models.SET_NULL)
  #  menu_type = models.SmallIntegerField(choices=menu_choice, default=1)

   # folder_type = models.SmallIntegerField(choices=folder_choice, default=2)
    folder_title =  models.CharField(max_length=200)
    file = models.FileField(upload_to='policy/',blank=True,null=True,validators=[FileExtensionValidator(allowed_extensions=['pdf','PDF'])])
    #parent = models.ForeignKey(acknoledge_menu,null=True, related_name ="ask_submenues" , limit_choices_to={'id': 1}, blank=True, on_delete=models.SET_NULL)
    ##############################late



    def __str__(self):
        return self.submenu_name


    class Meta:
        ordering = ['-id']


class graphDetail(models.Model):
    added_on = models.DateField(auto_now=True)
    updated_on = models.DateField(auto_now=True)
    menu_detail =models.ForeignKey(acknoledge_menu,null=True, related_name ="ask_submenudetail" , blank=True, on_delete=models.SET_NULL)
#    menu_user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,on_delete=models.SET_NULL)


class graphDetailUsed(models.Model):
    added_on = models.DateField(auto_now=True)
    updated_on = models.DateField(auto_now=True)
    menu_detail =models.ForeignKey(graphDetail,null=True, related_name ="graph_detail" , blank=True, on_delete=models.SET_NULL)
    menu_user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,on_delete=models.SET_NULL)



from django.core.exceptions import ValidationError

def validate_image(image):
    file_size = image.file.size
    limit_kb =1600000000
    max_height = 50000
    max_width = 5000




    if (file_size > limit_kb * 50):
        raise ValidationError("Max size of file is %s KB" % limit_kb)



def newvalidate_image(image):
    file_size = image.file.size
    limit_kb =700000
    max_height = 100
    max_width = 100




    if (file_size > limit_kb * 50):
        raise ValidationError("Max size of file is %s KB" % limit_kb)

    #limit_mb = 8
    #if file_size > limit_mb * 1024 * 1024:
    #    raise ValidationError("Max size of file is %s MB" % limit_mb)

class ack_subpublicationmenu(models.Model):
    menu_choice = (
        (1, "One"),
        (2, "Two"),
    )
    folder_choice = (
        (1, "One"),
        (2, "Two"),
    )
    added_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    submenu_name =  models.CharField(max_length=200,unique=True)
    parent_ob  = models.ForeignKey("self",null=True, blank=True, on_delete=models.SET_NULL)
    menu_type = models.SmallIntegerField(choices=menu_choice, default=1)
    folder_type = models.SmallIntegerField(choices=folder_choice, default=2)
    publicationicon = models.FileField(upload_to='publicattion/',blank=True,null=True,validators=[FileExtensionValidator(allowed_extensions=['png','jpg','JPEG'])])

    publicationfile = models.FileField(upload_to='publicattion/',blank=True,null=True,validators=[FileExtensionValidator(allowed_extensions=['png','jpg','JPEG','pdf','PDF'])])
    folder_title =  models.CharField(max_length=200)
    parent = models.ForeignKey(acknoledge_menu,null=True, related_name ="ask_subpublicationmenues" , limit_choices_to={'id': 2}, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.submenu_name
    class Meta:
        ordering = ['-id']



class ack_publicationname(models.Model):

    added_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    submenu_name =  models.CharField(max_length=200,unique=True)
    parent_ob  = models.ForeignKey(ack_subpublicationmenu,null=True, related_name='ack_publication_children',  blank=True, on_delete=models.SET_NULL)


    file = models.FileField(upload_to='publicattion/',blank=True,null=True,validators=[FileExtensionValidator(allowed_extensions=['png','jpg','JPEG','pdf','PDF'])])
    folder_title =  models.CharField(max_length=200)

class ack_subGuidelinesmenu(models.Model):
    menu_choice = (
        (1, "One"),
        (2, "Two"),
    )
    folder_choice = (
        (1, "One"),
        (2, "Two"),
    )
    parent_ob  = models.ForeignKey("self",null=True, blank=True, on_delete=models.SET_NULL)
    menu_type = models.SmallIntegerField(choices=menu_choice, default=1)
    folder_type = models.SmallIntegerField(choices=folder_choice, default=2)
    folder_title =  models.CharField(max_length=200)
    added_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    submenu_name =  models.CharField(max_length=200,unique=True)
    file = models.FileField(upload_to='guidelines/',blank=True,null=True,validators=[FileExtensionValidator(allowed_extensions=['png','jpg','JPEG']),newvalidate_image])
    parent = models.ForeignKey(acknoledge_menu,null=True, related_name ="ask_subguidelinesmenues" , limit_choices_to={'id': 3}, blank=True, on_delete=models.SET_NULL)
    guidelinefile = models.FileField(upload_to='guidelLines/',blank=True,null=True,validators=[FileExtensionValidator(allowed_extensions=['pdf','PDF','png','jpg','JPEG']),validate_image])

    def __str__(self):
        return self.submenu_name

    class Meta:
        ordering = ['-id']


class ack_guidelinesname(models.Model):


    parent_ob  = models.ForeignKey(ack_subGuidelinesmenu, related_name ="guidelinesMenues" , null=True, blank=True, on_delete=models.SET_NULL)

    folder_title =  models.CharField(max_length=200)
    added_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    submenu_name =  models.CharField(max_length=200,unique=True)
    file = models.FileField(upload_to='guidelines/',blank=True,null=True,validators=[FileExtensionValidator(allowed_extensions=['pdf','PDF','png','jpg','JPEG']),newvalidate_image])




class ack_subStandardsmenu(models.Model):
    menu_choice = (
        (1, "One"),
        (2, "Two"),
    )
    folder_choice = (
        (1, "One"),
        (2, "Two"),
    )
    added_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    submenu_name =  models.CharField(max_length=200,unique=True)
    parent_ob  = models.ForeignKey("self",null=True, blank=True, on_delete=models.SET_NULL)
    menu_type = models.SmallIntegerField(choices=menu_choice, default=1)
    folder_type = models.SmallIntegerField(choices=folder_choice, default=2)
    file = models.FileField(upload_to='standards_file/',blank=True,null=True,validators=[FileExtensionValidator(allowed_extensions=['pdf','PDF','png','jpg','JPEG']),validate_image])
    folder_title =  models.CharField(max_length=200)
    standardfile = models.FileField(upload_to='standards/',blank=True,null=True,validators=[FileExtensionValidator(allowed_extensions=['pdf','PDF','png','jpg','JPEG']),validate_image])

    parent = models.ForeignKey(acknoledge_menu,null=True, related_name ="ask_substandardsmenues" , limit_choices_to={'id': 4}, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.submenu_name


class ack_Standardsname(models.Model):
    added_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    submenu_name =  models.CharField(max_length=200,unique=True)
    parent_ob  = models.ForeignKey(ack_subStandardsmenu,  related_name ="standardFileMenues" , null=True, blank=True, on_delete=models.SET_NULL)

    file = models.FileField(upload_to='standards_file/',blank=True,null=True,validators=[FileExtensionValidator(allowed_extensions=['pdf','PDF','png','jpg','JPEG']),validate_image])
    folder_title =  models.CharField(max_length=200)



class ack_subNavy_Orderssmenu(models.Model):
    menu_choice = (
        (1, "One"),
        (2, "Two"),
    )
    folder_choice = (
        (1, "One"),
        (2, "Two"),
        )
    added_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    submenu_name =  models.CharField(max_length=200,unique=True)
    parent_ob  = models.ForeignKey("self",null=True, blank=True, on_delete=models.SET_NULL)
    menu_type = models.SmallIntegerField(choices=menu_choice, default=1)
    folder_type = models.SmallIntegerField(choices=folder_choice, default=2)
    file = models.FileField(upload_to='navy_ordersfile/',blank=True,null=True,validators=[FileExtensionValidator(allowed_extensions=['pdf','PDF','png','jpg','JPEG']),validate_image])
    folder_title =  models.CharField(max_length=200)
    navyfile = models.FileField(upload_to='navy_orders/',blank=True,null=True,validators=[FileExtensionValidator(allowed_extensions=['pdf','PDF','png','jpg','JPEG']),validate_image])
    parent = models.ForeignKey(acknoledge_menu,null=True, related_name ="ask_subnavy_ordersmenues" , limit_choices_to={'id': 5}, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.submenu_name




class ack_Navyname(models.Model):

    added_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    publiction_name = models.CharField(max_length=200,unique=True)
    parent = models.ForeignKey(ack_subNavy_Orderssmenu,null=True, related_name ="navyOrders_name" , blank=True, on_delete=models.SET_NULL)
    #policy_file =  GenericRelation(Comment_policy,related_query_name='blog_model')
    file = models.FileField(upload_to='navy_orders/',blank=True,null=True,validators=[FileExtensionValidator(allowed_extensions=['pdf','PDF','png','jpg','JPEG']),validate_image])
    parent_ob  = models.ForeignKey("self",null=True, blank=True, on_delete=models.SET_NULL)




class ack_subNavy_Instructionssmenu(models.Model):
    menu_choice = (
        (1, "One"),
        (2, "Two"),
    )
    folder_choice = (
        (1, "One"),
        (2, "Two"),
    )
    added_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    submenu_name =  models.CharField(max_length=200,unique=True)
    parent_ob  = models.ForeignKey("self",null=True, blank=True, on_delete=models.SET_NULL)
    menu_type = models.SmallIntegerField(choices=menu_choice, default=1)
    folder_type = models.SmallIntegerField(choices=folder_choice, default=2)
    file = models.FileField(upload_to='navy_instructionfile/',blank=True,null=True,validators=[FileExtensionValidator(allowed_extensions=['pdf','PDF','png','jpg','JPEG']),validate_image])
    folder_title =  models.CharField(max_length=200)
    navyinstructionfile = models.FileField(upload_to='navy_instruction/',blank=True,null=True,validators=[FileExtensionValidator(allowed_extensions=['pdf','PDF','png','jpg','JPEG']),validate_image])

    parent = models.ForeignKey(acknoledge_menu,null=True, related_name ="ask_subnavy_instructionmenues" , limit_choices_to={'id': 6}, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.submenu_name



class ack_subNHQe_Librarylinesmenu(models.Model):
    menu_choice = (
        (1, "One"),
        (2, "Two"),
    )
    folder_choice = (
        (1, "One"),
        (2, "Two"),
    )
    added_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    submenu_name =  models.CharField(max_length=200,unique=True)
    parent_ob  = models.ForeignKey("self",null=True, blank=True, on_delete=models.SET_NULL)
    menu_type = models.SmallIntegerField(choices=menu_choice, default=1)
    folder_type = models.SmallIntegerField(choices=folder_choice, default=2)
    file = models.FileField(upload_to='elibraryfiles/',blank=True,null=True,validators=[FileExtensionValidator(allowed_extensions=['pdf','PDF','png','jpg','JPEG']),validate_image])
    folder_title =  models.CharField(max_length=200)
    navyinstructionfile = models.FileField(upload_to='elibrary/',blank=True,null=True,validators=[FileExtensionValidator(allowed_extensions=['pdf','PDF','png','jpg','JPEG']),validate_image])

    parent = models.ForeignKey(acknoledge_menu,null=True, related_name ="ask_subnohqsmenues" , limit_choices_to={'id': 7}, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.submenu_name


class BRsmenu(models.Model):
    menu_choice = (
        (1, "One"),
        (2, "Two"),
    )
    folder_choice = (
        (1, "One"),
        (2, "Two"),
    )
    added_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    submenu_name =  models.CharField(max_length=200,unique=True)
    parent_ob  = models.ForeignKey("self",null=True, blank=True, on_delete=models.SET_NULL)
    menu_type = models.SmallIntegerField(choices=menu_choice, default=1)
    folder_type = models.SmallIntegerField(choices=folder_choice, default=2)
    file = models.FileField(upload_to='brsfiles/',blank=True,null=True,validators=[FileExtensionValidator(allowed_extensions=['pdf','PDF','png','jpg','JPEG']),validate_image])
    folder_title =  models.CharField(max_length=200)
    navyinstructionfile = models.FileField(upload_to='brsfoldermenus/',blank=True,null=True,validators=[FileExtensionValidator(allowed_extensions=['pdf','PDF','png','jpg','JPEG']),validate_image])

    parent = models.ForeignKey(acknoledge_menu,null=True, related_name ="brsmenues" , limit_choices_to={'id': 8}, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.submenu_name






class ack_policyname(models.Model):
    menu_choice = (
        (1, "One"),
        (2, "Two"),
    )
    folder_choice = (
        (1, "One"),
        (2, "Two"),
    )
    added_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    policy_name = models.CharField(max_length=200,unique=True)
    parent = models.ForeignKey(ack_submenu,null=True, related_name ="policy_name" , blank=True, on_delete=models.SET_NULL)
    #policy_file =  GenericRelation(Comment_policy,related_query_name='blog_model')
    parent_ob  = models.ForeignKey("self",null=True, blank=True, on_delete=models.SET_NULL)
    folder_type = models.SmallIntegerField(choices=folder_choice, default=2)
    menu_type = models.SmallIntegerField(choices=menu_choice, default=1)

    def __str__(self):
        return self.policy_name





class ack_NavyInstructionname(models.Model):
    menu_choice = (
        (1, "One"),
        (2, "Two"),
    )
    folder_choice = (
        (1, "One"),
        (2, "Two"),
    )
    added_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    publiction_name = models.CharField(max_length=200,unique=True)
    parent = models.ForeignKey(ack_subNavy_Instructionssmenu,null=True, related_name ="navyinstruction_name" , blank=True, on_delete=models.SET_NULL)
    #policy_file =  GenericRelation(Comment_policy,related_query_name='blog_model')
    file = models.FileField(upload_to='navy_instruction/',blank=True,null=True,validators=[FileExtensionValidator(allowed_extensions=['pdf','PDF','png','jpg','JPEG']),validate_image])
    parent_ob  = models.ForeignKey("self",null=True, blank=True, on_delete=models.SET_NULL)
    folder_type = models.SmallIntegerField(choices=folder_choice, default=2)
    menu_type = models.SmallIntegerField(choices=menu_choice, default=1)



    # @property
    # def get_parent(self):
    #     pass



class ack_policypolicyfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,on_delete=models.SET_NULL)
    added_on = models.DateField(auto_now_add=True, null=True)
    file = models.FileField(upload_to='policy/',blank=True,null=True,validators=[FileExtensionValidator(allowed_extensions=['pdf','PDF'])])
    updated_on = models.DateField(auto_now=True,null=True)
    parent_file = models.ForeignKey(ack_policyname,null=True, related_name ="ask_policyfile" , blank=True, on_delete=models.SET_NULL)
    policies_name = models.CharField(max_length=200)

    def policy_name(self,request):
        pass



class ack_publicationfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,on_delete=models.SET_NULL)
    added_on = models.DateField(auto_now_add=True, null=True)
    file = models.FileField(upload_to='publication/',blank=True,null=True,validators=[FileExtensionValidator(allowed_extensions=['pdf','PDF'])])
    updated_on = models.DateField(auto_now=True,null=True)
    #parent_file = models.ForeignKey(ack_policyname,null=True, related_name ="ask_policyfile" , blank=True, on_delete=models.SET_NULL)
    publication_name = models.CharField(max_length=200)




class Country(models.Model):
    name = models.CharField(max_length=30)

class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    population = models.PositiveIntegerField()
