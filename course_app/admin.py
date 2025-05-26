from django.contrib import admin
from course_app.models import AnswerOption, Course, Lesson, Test

# Inline для ответов
class AnswerOptionInline(admin.TabularInline):  # или admin.StackedInline
    model = AnswerOption
    extra = 1
    max_num = 4

# Кастомный админ для тестов
class TestAdmin(admin.ModelAdmin):
    inlines = [AnswerOptionInline]

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # пример: добавь нужные поля
    filter_horizontal = ('students',)

# Регистрация моделей
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
admin.site.register(Test, TestAdmin)  # <-- используй кастомный TestAdmin
