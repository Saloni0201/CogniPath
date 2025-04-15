# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Classroom(models.Model):
    id = models.AutoField(primary_key= True)
    classroom = models.ForeignKey(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.classroom.username
 
class Course(models.Model):
    course_id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=100)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    description = models.CharField(max_length=700)
    published_at = models.DateField()
    
    def __str__(self):
        return self.name

class EnrolledCourse(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    date = models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return self.user.username+"-"+self.course.name
  

class Content(models.Model):
    content_id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    video =models.FileField(upload_to="lectures")
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.name
        
class Assignment(models.Model):
    name = models.CharField(max_length= 100)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    file = models.FileField(upload_to="assignments")

    def __str__(self):
        return self.name
        
       
class Note(models.Model):
    name = models.CharField(max_length= 100)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    file = models.FileField(upload_to="notes")

    def __str__(self):
        return self.name
        

class UploadAssignment(models.Model):
    name = models.CharField(max_length=122)
    roll_no =models.CharField(max_length=122, primary_key=True)
    link = models.URLField(max_length=200)
    file = models.FileField(upload_to="submissions")
    classroom = models.CharField(max_length=122)

    def __str__(self):
        return self.name
