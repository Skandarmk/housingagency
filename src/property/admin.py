from django.contrib import admin

# Register your models here.
from .models import Property , Category , Reserve , PropertyImages , Neighborhood



class PhotoInline(admin.StackedInline):
    model = PropertyImages
    extra = 2

class PropAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]

    def save_model(self, request, obj, form, change):
        obj.save()

        for afile in request.FILES.getlist('photos_multiple'):
            obj.photos.create(image=afile)




class PropertyImagesAdmin(admin.ModelAdmin):
  pass


class PropertyAdmin(admin.ModelAdmin):
    list_display = ['name', 'type' , 'category' , 'area' , 'rooms_number' , 'beds_number' , 'furnished' , 'purpose']
    search_fields = ['name' , 'type' , 'category']
    list_filter = ['category', 'type']

admin.site.register(Property , PropAdmin)
admin.site.register(PropertyImages , PropertyImagesAdmin)
admin.site.register(Category)
admin.site.register(Neighborhood)
admin.site.register(Reserve)
