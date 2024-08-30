from django.contrib import admin, messages
from .models import Women, Category


class MarriedFilter(admin.SimpleListFilter):
    title = "Women's status"
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('married', 'Married'),
            ('single', 'Not married')
        ]

    def queryset(self, request, queryset):
        if self.value() == 'married':
            return queryset.filter(husband__isnull=False)
        elif self.value() == 'single':
            return queryset.filter(husband__isnull=True)


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    fields = ['title', 'content', 'slug', 'cat', 'husband', 'tags']
    # exclude = ['tags', 'is_published']
    # readonly_fields = ['slug']
    prepopulated_fields = {'slug': ('title', )}
    filter_horizontal = ['tags']
    # filter_vertical = ['tags']
    list_display = ('title', 'time_create', 'is_published', 'cat', 'brief_info')
    list_display_links = ('title',)
    ordering = ['time_create', 'title']
    list_editable = ('is_published',)
    list_per_page = 5
    actions = ['set_published', 'set_draft']
    search_fields = ['title', 'cat__name']
    list_filter = [MarriedFilter, 'cat__name', 'is_published']

    @admin.display(description='Short description', ordering='content')
    def brief_info(self, women: Women):
        return f"Description {len(women.content)} symbols."

    @admin.action(description='Publish selected posts')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Women.Status.PUBLISHED)
        self.message_user(request, f"Changed {count} posts.")

    @admin.action(description='Unpublish selected posts')
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Women.Status.DRAFT)
        self.message_user(request, f"{count} posts unpublished", messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
