from django.contrib import admin, messages
from .models import Category, Post
from django.utils.translation import ngettext



# actions

@admin.action(description='انتشار پست‌های انتخاب شده')
def make_published(modeladmin, request, queryset):
    updated=queryset.update(status='p')
    modeladmin.message_user(request, ngettext(
            '%d post was successfully marked as published.',
            '%d posts were successfully marked as published.',
            updated,
        ) % updated, messages.SUCCESS)
@admin.action(description='پیش نویس شدن پست‌های انتخاب شده')
def make_draft(modeladmin, request, queryset):
    updated=queryset.update(status='d')
    modeladmin.message_user(request, ngettext(
            '%d post was successfully marked as drafted.',
            '%d posts were successfully marked as drafted.',
            updated,
        ) % updated, messages.SUCCESS)
@admin.action(description='فعال شدن دسته‌بندی انتخاب شده')
def make_active(modeladmin, request, queryset):
    updated=queryset.update(status=True)
    modeladmin.message_user(request, ngettext(
            '%d category was successfully marked as actived.',
            '%d categories were successfully marked as actived.',
            updated,
        ) % updated, messages.SUCCESS)
@admin.action(description='غیر فعال شدن دسته‌بندی انتخاب شده')
def make_deactive(modeladmin, request, queryset):
    updated=queryset.update(status=False)
    modeladmin.message_user(request, ngettext(
            '%d category was successfully marked as dactivated.',
            '%d categories were successfully marked as dactivated.',
            updated,
        ) % updated, messages.SUCCESS)

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position','title','slug','status')
    list_filter = (['status'])
    search_fields = ('title','slug')
    prepopulated_fields = {'slug':('title',)}
    actions = [make_active,make_deactive]


admin.site.register(Category,CategoryAdmin)



class PostAdmin(admin.ModelAdmin):
    list_display = ('title','thumbnail_tag','author','slug','jpublish','status','category_to_str')
    list_filter = ('status','publish')
    search_fields = ('description','title')
    prepopulated_fields = {'slug':('title',)}
    ordering = ['-status','-publish']
    actions = [make_published,make_draft]

    def category_to_str(self,obj):
        return ", ".join([category.title for category in obj.category_published()])
    category_to_str.short_description = "دسته‌بندی"

admin.site.register(Post,PostAdmin)

