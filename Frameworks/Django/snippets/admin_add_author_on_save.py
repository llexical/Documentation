from django.contrib import admin

class BaseAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        if not hasattr(obj, 'id'):
            obj.author = request.user
        super(BaseAdmin, self).save_model(request, obj, form, change)