from django.contrib import admin
from .models import (application_menu,application_submenu,
application_parent_menu, news, staff_image, policy, publication,
 wing_commander, Article, CnsMessage)
admin.site.register(application_menu)
admin.site.register(application_submenu)
admin.site.register(application_parent_menu)
admin.site.register(news)
admin.site.register(policy)
admin.site.register(publication)
admin.site.register(wing_commander)
admin.site.register(staff_image)
admin.site.register(CnsMessage)
