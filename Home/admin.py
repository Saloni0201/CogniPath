# Register your models here.
from django.contrib import admin
from Home.models import Classroom, Content, Course,EnrolledCourse,Assignment,Note, UploadAssignment
from django.contrib.auth.models import User

admin.site.register(EnrolledCourse)
admin.site.register(Assignment)
admin.site.register(Note)

class classroomAdmin(admin.ModelAdmin):
    list_display = ['id', 'classroom','full_name']
    ordering = ['id']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(classroom = request.user)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "classroom":
            kwargs["queryset"] = User.objects.filter(username = request.user.username)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
        
admin.site.register(Classroom, classroomAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_id', 'name', 'classroom', 'description', 'published_at']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(classroom__classroom=request.user)  # Corrected to use the ForeignKey field name

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "classroom":
            kwargs["queryset"] = Classroom.objects.filter(classroom=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Course, CourseAdmin)

class ContentAdmin(admin.ModelAdmin):
    list_display = ['content_id', 'name', 'course', 'video', 'title']
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "course":
            # Get the IDs of classrooms associated with the current user
            classroom_ids = Classroom.objects.filter(classroom=request.user).values_list('id', flat=True)
            # Filter courses based on classrooms associated with the user
            kwargs["queryset"] = Course.objects.filter(classroom__in=classroom_ids)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Content, ContentAdmin)



class UploadAssignmentAdmin(admin.ModelAdmin):
    list_display = [  'name','roll_no', 'link' , 'file', 'classroom']
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(classroom=request.user.username )
admin.site.register(UploadAssignment, UploadAssignmentAdmin)
