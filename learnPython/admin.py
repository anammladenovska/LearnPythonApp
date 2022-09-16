from django.contrib import admin

from .models import Lesson, Materials, Forum

# Register your models here.


class LessonAdmin(admin.ModelAdmin):
    list_display = ("name",)
    exclude = ("user",)


admin.site.register(Lesson)


class MaterialsAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True

    # def get_queryset(self, request):
    #     qs = super(MaterialsAdmin, self).get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(user=request.user)


admin.site.register(Materials)

admin.site.register(Forum)