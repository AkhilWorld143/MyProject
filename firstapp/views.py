from django.shortcuts import render, redirect
# for working on registration and login
from django.contrib import messages
from django.contrib.auth.models import User, auth
from firstapp.models import Employee # importing model classs for showing the student from the Database
# Import QuerySet to use the group_by
from django.db.models.query import QuerySet

# Create your views here.
def home(request):
    return render(request, 'firstapp/home.html')


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        u_name = request.POST['uname']
        gender = request.POST['gender']
        cities = request.POST['cities']
        image = request.FILES['image']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        student = Employee.objects.create(name=name, username=u_name, gender=gender,
        cities=cities, image=image, email=email, password=password, status=0)
                    # student.save();
        print("Student is Saved")
        return redirect('/showstudents')

    else:
        return render(request, 'firstapp/register.html')


def login(request):
    if request.method == 'POST':

        emp = Employee.objects.filter(email=request.POST['email'], password=request.POST['password'])
        if emp:
            request.session['email'] = request.POST['email']
            # request.session['name'] = request.POST['name']
            return redirect('/showstudents')
        else:
            return render(request, 'firstapp/login.html', {'message': 'Invalid Credentials'})
    else:
        return render(request, 'firstapp/login.html', {'message': 'No input values are provided by user'})


def showstudents(request):
    if request.session.has_key('email'):
        # query = Employee.objects.all().query
        # query.group_by = ['cities']
        # employees = QuerySet(query=query, model=Employee)
        employees = Employee.objects.filter(email=request.session['email'])

    # employees = Employee.objects.raw(SELECT * FROM firstapp_employee)
        return render(request, 'firstapp/showstudent.html', {'employees':employees, 'emp_name':request.session['email']})
    else:
        return redirect('/login')


def update(request, id):
        student = Employee.objects.get(id = id)
        student.save()
        return render(request, 'firstapp/update.html', {'student': student})

        # request.session['id'] = student.id
        # name = request.POST['name']
        # u_name = request.POST['uname']
        # gender = request.POST['gender']
        # cities = request.POST['cities']
        # image = request.FILES['image']
        # email = request.POST['email']
        # password = request.POST['password']
        # student = Employee.objects.create(name=name, username=u_name, gender=gender,
        #             cities=cities, image=image, email=email, password=password)
        # print("Record is Updated Successfully
        # return redirect('showstudents')

    # else:
    #     print("Sorry no data are matching to Update")


def delete(request, id):
    student = Employee.objects.get(id=id)
    student.delete()
    return redirect('/showstudents')


def change_pass(request):
    # student = Employee.objects.all()
    # print(student)
    # student.create()
    return render(request, 'firstapp/change_pass.html')
    # pass
    # if request.method == 'POST':
    #     currentPassword = request.POST['currentPassword']
    #     newPassword = request.POST['newPassword']
    #     confirmPassword = request.POST['newPassword']
    #
    #     employees = Employee.objects.all()
    #
    #     user = auth.authenticate(email=email, password=password)
    #
    #     if newPassword == confirmPassword:


def logout(request):
    request.session.flush()
    return render(request, 'firstapp/login.html')
