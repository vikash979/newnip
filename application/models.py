from django.db import models
from django.conf import settings

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
#from users.models import CustomUser
from django.conf import settings
from acknowledge.models import parent_menu

class application_parent_menu(models.Model):
    application_nav = models.ForeignKey(parent_menu,null=True, related_name ="app_menu" ,limit_choices_to={'id': 1}, blank=True, on_delete=models.SET_NULL)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    menu_name =  models.CharField(max_length=200,unique=True)
    def __str__(self):
        return self.menu_name








from django.core.validators import FileExtensionValidator
class application_menu(models.Model):
    menu_choice = (
        (1, "One"),
        (2, "Two"),
    )
    folder_choice = (
        (1, "One"),
        (2, "Two"),
    )
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    menu_name =  models.CharField(max_length=200,unique=True)
    parent = models.ForeignKey(application_parent_menu,null=True, related_name ="application_menu" , blank=True, on_delete=models.SET_NULL)
    ###############################late
    parent_ob  = models.ForeignKey("self",null=True, blank=True, on_delete=models.SET_NULL)
    menu_type = models.SmallIntegerField(choices=menu_choice, default=1)
    file = models.FileField(upload_to='study_material/notes/',blank=True,null=True,validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    folder_type = models.SmallIntegerField(choices=folder_choice, default=2)
    def __str__(self):
    	return self.menu_name


    def css_class(self):
        name, extension = os.path.splitext(self.file.name)
        if extension == 'pdf':
            return 'pdf'
        if extension == 'doc':
            return 'word'
        return 'other'




class application_submenu(models.Model):
	folder_choice = (
        (1, "One"),
        (2, "Two"),
    )

	added_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	parent = models.ForeignKey("self",null=True, blank=True, on_delete=models.SET_NULL)
	submenu_name = models.CharField(max_length=200,unique=True)
	menu_id = models.ForeignKey(application_menu,related_name ="application_submenu" , null=True,on_delete=models.SET_NULL)
	parent  = models.ForeignKey("self",null=True, blank=True, on_delete=models.SET_NULL)
	content = models.SmallIntegerField(choices=folder_choice, default=1)

	def __str__(self):
		return self.submenu_name

class news(models.Model):
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by =  models.ForeignKey(settings.AUTH_USER_MODEL, null=True,on_delete=models.SET_NULL)
    news_heading = models.CharField(max_length=200,unique=True)

class staff_image(models.Model):
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by =  models.ForeignKey(settings.AUTH_USER_MODEL, null=True,on_delete=models.SET_NULL)
    file = models.FileField(upload_to='staff/',blank=True,null=True,validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','JPG','JPEG','png','PNG'])])
    staff_name =  models.CharField(max_length=200,unique=True)
    rank_name =  models.CharField(max_length=200,unique=True)

class policy(models.Model):
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by =  models.ForeignKey(settings.AUTH_USER_MODEL, null=True,on_delete=models.SET_NULL)
    file = models.FileField(upload_to='policy/',blank=True,null=True,validators=[FileExtensionValidator(allowed_extensions=['pdf','PDF'])])
    policy_name =  models.CharField(max_length=200,unique=True)


class publication(models.Model):
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by =  models.ForeignKey(settings.AUTH_USER_MODEL, null=True,on_delete=models.SET_NULL)
    file = models.FileField(upload_to='publication/',blank=True,null=True,validators=[FileExtensionValidator(allowed_extensions=['pdf','PDF'])])
    ppublication_name =  models.CharField(max_length=200,unique=True)


class wing_commander(models.Model):
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by =  models.ForeignKey(settings.AUTH_USER_MODEL, null=True,on_delete=models.SET_NULL)
    file = models.FileField(upload_to='wing_commander/',blank=True,null=True,validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','JPG','JPEG','png','PNG'])])
    #wing_zone =  models.CharField(max_length=200)
    #wing_commander_name =  models.CharField(max_length=200)
    #wing_commander_rank=  models.CharField(max_length=200)

    # def __str__(self):
    #     return self.wing_commander_name.capitalize()


class log_data(models.Model):
    added_on =  models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by =  models.ForeignKey(settings.AUTH_USER_MODEL, null=True,on_delete=models.SET_NULL)
    url_name = models.CharField(max_length=200)



class Article(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


    def shortenText(self):
        return self.body[:100]




class CnsMessage(models.Model):
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    cns_message = models.TextField(blank=True, null=True)
