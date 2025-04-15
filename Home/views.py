# Create your views here.

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import  login,logout, authenticate
from django.contrib.auth.hashers  import make_password
from Home.models import  Course,  Classroom, EnrolledCourse, Content, Assignment,Note,UploadAssignment
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'Homepage.html')



def Signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        
        password = make_password(password)
        user = User.objects.create(username = username,password = password,email =email)
        user.save()
        return redirect('Home')
    return render(request, 'Signup.html')



def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)


        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('/classroom')
        
        else:
            return render(request, "Login.html")
    
    return render(request, 'Login.html')

def classroom(request):
    classroom = Classroom.objects.all()
    return render(request, 'Classroom.html', {'classroom':classroom})


@login_required(login_url='/login')
def filter(request,id):
    if(Classroom.objects.filter(id = id)):
        courses =  Course.objects.filter(classroom_id = id)
        context = {'courses':courses}
        return render(request, 'Filter.html', context)
    else:
        messages.warning(request, "No such classroom is found")
        return redirect('classroom')


  
def courses(request,id):   
    course_id = Course.objects.get(course_id= id)
    try:
        check_enrollment = EnrolledCourse.objects.get(user = request.user, course = course_id)
    except EnrolledCourse.DoesNotExist:
        check_enrollment = None

    course = Course.objects.filter(course_id = id)
    return render(request, 'Course.html',{'course': course[0], 'check_enrollment': check_enrollment})



def checkout( request,id):
    course = Course.objects.get(course_id = id)

    if request.user.is_authenticated:
        user = request.user
        print(user)


        courses = EnrolledCourse(
        user = request.user,
        course = course
        )
    
        courses.save()
        return redirect('Mycourses')
    

def mycourses(request):
    course = EnrolledCourse.objects.filter(user = request.user)
    context = {
        'course' :course
    }
    return render(request, 'Mycourses.html', context)


def contents(request, id):
   
    content = Content.objects.filter(course_id = id)
    return render(request, 'Contents.html',{'content': content})


def watchcourse(request, id):
    video = Content.objects.filter(content_id = id)
    return render(request, 'Watch.html', {'video': video[0]})



def assignments(request,id):
    if(Course.objects.filter(course_id = id)):
        assignments =  Assignment.objects.filter(course_id = id)
        context = {'assignments': assignments}
        return render(request, 'Assignments.html', context)
    else:
        messages.warning(request, "No such classroom is found")
        return redirect('classroom')
    


def notes(request,id):
    if(Course.objects.filter(course_id = id)):
        notes =  Note.objects.filter(course_id = id)
        context = {'notes': notes}
        return render(request, 'Notes.html', context)
    else:
        messages.warning(request, "No such classroom is found")
        return redirect('classroom')


def upload(request):
    assignments = Classroom.objects.all()
    context = {'assignments': assignments}
    if request.method == "POST":
        name = request.POST.get('name')
        roll_no = request.POST.get('roll_no')
        classroom = request.POST.get('classroom')
        file = request.POST.get('file')
        link = request.POST.get('link')

        upload = UploadAssignment(name = name, roll_no = roll_no, Classroom = classroom, file = file, link = link)
        upload.save()
        return redirect('upload')
    return render(request, 'UploadAssignment.html', context)




def logoutuser(request):
    logout(request)
    return render(request, 'Homepage.html')                

