from django.contrib import admin
from django.contrib.admin import AdminSite

# Register your models here.
from miapp.models import Article,Post,Profile



class ArticleAdmin(admin.ModelAdmin):
    readonly_fields=('createdo_el', 'atualizado_el','user')
    list_display = ('titulo','user','createdo_el','atualizado_el')
    ordering = ('createdo_el',)    
    list_filter = ('user__username','createdo_el',)
    search_fields =('titulo','contenido','user__username')
    
    def save_model(self,request,obj,form,change):
        if not obj.user_id:
            obj.user_id =request.user.id
        obj.save()        

admin.site.register(Article,ArticleAdmin)
admin.site.register(Post)
admin.site.register(Profile)