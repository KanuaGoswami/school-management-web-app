from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from home import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('about',views.about,name="about"),
    path('clas',views.clas,name="clas"),
    path('contact',views.contact,name="contact"),
    path('blog',views.blog,name="blog"),
    path('gallery',views.gallery,name="gallery"),
    path('teacher',views.teacher,name="teacher"),
    path('login',views.login,name="login"),

    path('register',views.register,name="register"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('professor',views.professor,name="professor"),
    path('add-professor',views.addProfessor,name="add-professor"),
    path('courses',views.courses,name="courses"),
    path('add-course',views.addCourse,name="add-course"),
    path('add-student',views.addStudent,name="add-student"),
    path('logout',views.logout,name="logout"),
    path('picture',views.picture,name="picture"),
    path('add-picture',views.addPicture,name='add-picture'),
    # path('add-course',views.addCourse,name="add-course"),
    path('contactQuery',views.contactQuery,name="contactQuery"),
    path('events',views.events,name="events"),
    path('deposit-fees',views.depositFees,name="deposit-fees"),
    path('transaction',views.transaction,name="transaction"),
    path('contactQuery/delete/<int:id>',views.deleteContact,name="delteContact"),
    path('add-result',views.addResult,name="add-result"),
    path('students',views.students,name='students'),
    path('results',views.results,name='results'),
    path('delete-professor/<int:id>',views.deleteProfessor,name='deleteProfessor'),
    path('delete-student/<int:id>',views.deleteStudent,name='delete-student'),
    path('delete-picture/<int:id>',views.deletePicture,name='delete-picture'),



    

   
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
