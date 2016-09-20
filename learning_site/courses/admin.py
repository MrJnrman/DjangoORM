from django.contrib import admin

from . import models

from datetime import date

#  globally disable delete in admin
#  admin.site.disable_action('delete_selected')

def make_published(modeladmin, request, queryset):  # create action
    queryset.update(status='p', is_live=True)

make_published.short_description =' Make Published'

class QuizAdmin(admin.ModelAdmin):
    fields = ['course', 'title', 'description', 'order', 'total_questions']

    search_fields = ['title']

    list_display = ['title', 'course']

    list_editable = ['course']  # only works when list_diplay is set, allow editing of lists straight from view

    radio_fields = {'course': admin.HORIZONTAL}  # dropdown changes to horizontal radio buttons

class YearListFilter(admin.SimpleListFilter):
    title = 'year created'  # title of filter on page

    parameter_name = 'year'  # parameter name thast shows up in url

    def lookups(self, request, model_admin):
        return (
            ('2015', '2015'),  # first element shows up in url
            ('2016', '2016')  # second element shows up in sidebar
        )

    def queryset(self, request, queryset):
        if self.value():
            year = self.value()
            return queryset.filter(created_at__gte=date(int(year), 1,1),
                                   created_at__lte=date(int(year), 12, 31))



class CourseAdmin(admin.ModelAdmin):
    fields = ['subject', 'title', 'description', 'teacher', 'published']

    search_fields = ['title', 'description']  # creates a search box that searches for the fields specified

    list_filter = ['title', 'created_at', YearListFilter]  # allows items to be filtered

    list_display = ['title', 'created_at', 'time_to_complete', 'is_live', 'status']  # how courses are displayed

    list_editable = ['status']

    class Media:
        js = ('js/vendor/markdown.js', 'js/preview.js')
        css = {
            'all': ('css/preview.css',),
        }

    actions = [make_published]

class TextAdmin(admin.ModelAdmin):
    fieldsets = (  # group fields together
        (None, {
            'fields' :('course', 'title', 'order', 'description')
        }),
        ('Add content', {
            'fields': ('content',),
            'classes': ('collapse',)  # hide/show
        }),
    )


admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.Text, TextAdmin)
admin.site.register(models.Quiz, QuizAdmin)
admin.site.register(models.MultipleChoiceQuestion)
admin.site.register(models.TrueFalseQuestion)
admin.site.register(models.Answer)