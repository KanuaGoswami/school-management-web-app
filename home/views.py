from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from home.models import Contact as ContactModel,Result,Gallery,Student,Profile,Transaction,Teacher,Result
from home.forms import CourseForm
from django.contrib import messages

# from django.db import models


# Create your views here.
def index(request):
    # return HttpResponse('hii my app is running')
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def clas(request):
    return render(request,'class.html')

def gallery(request):
    galleryObj = Gallery.objects.all().values()


    return render(request,'gallery.html',{'pictures':galleryObj})

def contact(request):
    if(request.method == 'POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contactObj = ContactModel(name=name,email=email,subject=subject,message=message)
        contactObj.save()
        # messages.add_message(request, messages.INFO, 'Hello world.')
        messages.add_message(request,messages.SUCCESS,'Your Query is submit successfully')

    return render(request,'contact.html')

def blog(request):
    return render(request,'blog.html')

def teacher(request):
    return render(request,'team.html')

def login(request):
    if(request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if(user is not None):
            my_user = request.session['name'] = username

            return render(request,'admin/dashboard.html')
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        contactNumber = request.POST.get('mobile')
        userObj = User(username=username,password=password)
        userObj.save()
        profileObj = Profile(user = userObj,email = email,mobile = contactNumber)
        profileObj.save()

    return render(request,'register.html')

def dashboard(request):
    if(request.session.get('name')):
        
        return render(request,'admin/dashboard.html')
        
    else:
        return redirect('/login')

def logout(request):
    del request.session['name']
    return redirect('/login')

def professor(request):
    professors =Teacher.objects.all().values()

    return render(request,'admin/professor.html',{'professors':professors})

def addProfessor(request):
    if request.method == 'POST':
        name=request.POST.get('firstname')
        address=request.POST.get('address')
        mobileno=request.POST.get('mobileno')
        dob = request.POST.get('finish')
        postcode=request.POST.get('postcode')
        image= request.FILES.get('image')
        dept = request.POST.get('department')
        desc = request.POST.get('description')
        gender = request.POST.get('gender')
        qualification=request.POST.get('qualification')
        teacherobj = Teacher(name=name,address=address,mobile=mobileno,dob=dob,designation=dept,image=image,desc=desc,gender=gender,qualification=qualification)
        try:
            teacherobj.save()
            messages.add_message(request,messages.SUCCESS,'Your Query is submit successfully')
        except:

            messages.add_message(request,messages.SUCCESS,'Record Already Exists !')
        # return render(request,'admin/add-professor.html',{'messages':messages})
    return render(request,'admin/add-professor.html')

def courses(request):
    return render(request,'admin/all-courses.html')

def addCourse(request):
    form = CourseForm()
    return render(request,'admin/add-course.html',{'form':form})

def addStudent(request):
    if request.method == 'POST':
        fullname = request.POST.get('firstname')
        fname = request.POST.get('fname')
        mname = request.POST.get('mname')
        mobileno = request.POST.get('mobileno')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        postcode = request.POST.get('postcode')
        rollno = request.POST.get('rollno')
        image = request.FILES.get('image')
        cl = request.POST.get('cl')
        studentObj = Student(name = fullname,rollno = rollno,fname = fname,mname = mname,mobileno = mobileno,dob= dob,gender = gender,address = address,postcode = postcode,image=image,cl=cl)
        try:
            studentObj.save()
            messages.add_message(request,messages.SUCCESS,'Student Record Successfully Submitted')
        except:
            messages.add_message(request.messages.SUCCESS,"Record Already Exist!")
        # return render(request,'admin/add-student.html',{'messages':message})
   
    return render(request,'admin/add-student.html')
def students(request):
    students=Student.objects.all().values()
    return render(request,'admin/students.html',{'students':students})

def addPicture(request):
    if(request.method == 'POST'):
        title = request.POST.get('title')
        image = request.FILES.get('image')
        desc = request.POST.get('description')
        galleryobj = Gallery(title=title,image=image,desc=desc)
        try:
            galleryobj.save()
            messages.add_message(request,messages.SUCCESS,"Submit Successfully")
        except:
            messages.add_message(request,messages.SUCCESS,"Record Already Exist")
            # message="record already exist"
            # return render(request,'admin/add-gallery.html',{'message':message})
    return render(request,'admin/add-gallery.html')
        

    # else:        
    #     return render(request,'admin/add-gallery.html')

def picture(request):
    pictures = Gallery.objects.all().values()
    return render(request,'admin/gallery.html',{'pictures':pictures})
def deletePicture(request,id):
    pictureObj = Gallery.objects.get(id=id)
    pictureObj.delete()
    return redirect('/picture')
def events(request):
    return render(request,'admin/events.html')
def contactQuery(request):
    contactdata = ContactModel.objects.all().values()
    context = {
        'data':contactdata,
    }
    return render(request,'admin/contactQuery.html',context)
    # return HttpResponse("hii")
def deleteProfessor(request,id):
    profObj = Teacher.objects.get(id=id)
    profObj.delete()
    # messages.add_message(request,messages.SUCCESS,'Delete successfully ')
    # return render(request,'admin/professor.html')
    return redirect('professor')
def deleteStudent(request,id):
    StuObj = Student.objects.get(id= id)
    StuObj.delete()
    return redirect('/students')

def deleteContact(request,id):
    # contactObj = ContactModel.objects.get(id=id) both working
    contactObj = ContactModel(id=id)
    contactObj.delete()
    return redirect('/contactQuery')
# def editContact(request,id):
#     contactObj=ContactModel.objects.get(id=id)

def depositFees(request):
    studentObj = Student.objects.all()

    if(request.method == 'POST'):
        rollno = request.POST.get('rollno')
        name = request.POST.get('name')
        cl= request.POST.get('cl')
        amount=request.POST.get('amount')
        student = Student.objects.get(id=cl)
        # print(studentObj)
        
        # studentObj = Student.objects.get(id=studentObj[0]['id'])
        # print(studentObj[0].id)
        # studentObj = Student.objects.create(name = studentObj[0]['name'],rollno = studentObj[0]['rollno'],fname = studentObj[0]['fname'],mname = studentObj[0]['mname'],mobileno = studentObj[0]['mobileno'],dob= studentObj[0]['dob'],gender = studentObj[0]['gender'],address = studentObj[0]['address'],postcode = studentObj[0]['postcode'])

        # studentObj = Student(name=studentObj[0]['name'],rollnostudentObj[0][''])
        try:
            tobj = Transaction.objects.create(student=student,amount=amount)
            messages.add_message(request,message.SUCCESS,"Recored successfully stored");
        except:
            messages.add_message(request.messages.SUCCESS,"Record Already Exits!")
        # tobj.save() 


    return render(request,'admin/deposit-fees.html',{'students':studentObj})
def results(request):
    results=Result.objects.all().values()


    return render(request,'admin/result.html',{'results':results})
def transaction(request):
    transactions = Transaction.objects.all().values()
    # students={}
    # for transaction in transactions:
    #     students = Student.objects.get(id=transaction['student_id'])

 
    return render(request,'admin/transaction.html',{'transactions':transactions})

def addResult(request):
    students = Student.objects.all().values()
    if(request.method == 'POST'):
        data = request.POST
        
        
        studentObj = Student.objects.get(id=data['name'])
        try:
            result = Result.objects.create(student=studentObj,examname=data['exam'],english=data['English'],math=data['math'],science=data['science'],sst=data['sst'],hindi=data['hindi'])
            messages.add_message(request,messages.SUCCESS,"Submit Successfully !")
        except:
            messages.add_message(request,messages.SUCCESS,"Record already exits !")
    return render(request,'admin/add-result.html',{'students':students})


