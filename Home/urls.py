
"""
URL configuration for LMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from Home import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('signup', views.Signup, name="Signup"),
    path('login', views.loginuser,name = "Login" ),
    path('classroom', views.classroom, name="classroom"),
    path('filter/<int:id>', views.filter, name="filter"),
    path('courses/<int:id>', views.courses, name="course"),
    path('checkout/<int:id>', views.checkout, name="checkout"),
    path('mycourses',views.mycourses, name="Mycourses"),
    path('contents/<int:id>', views.contents, name = "contents"),
    path('view/<int:id>', views.watchcourse, name="watch"),
    path('logout', views.logoutuser, name="Logout"),
    path('assignments/<int:id>', views.assignments, name="Assignment"),
    path('notes/<int:id>', views.notes, name="Notes"),
    path('upload', views.upload, name ="upload"),
]


