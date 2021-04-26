from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.http import HttpResponse , JsonResponse
from .models import Student, Resume, Certificate
from company.models import Company, Internship, InternshipAppliedDB
from django.contrib import messages
 
 

def home(request):
    return render(request, 'index.html')

def internships(request):
    if request.user.is_authenticated:
        try:
            if (request.user.student.isStudent == True):
                posts = Internship.objects.order_by('-id')
                std = Student.objects.get(email=request.user.student.email)
                return render(request, 'StudentHomePage.html', {'posts':posts, 'student':std})
            else:
                messages.info(request, 'Please sign in as a student')
                return redirect(auth_student)
        except:
            messages.info(request, 'Some error occured. Please signin again')
            return redirect(auth_student)
    else:
        messages.info(request, 'Please signin to proceed')
        return redirect(auth_student)

def signin(request):
    password =  request.POST.get('password')
    username =  request.POST.get('username')
    if (request.POST.get('formtype') =='signupform'):
        username =  request.POST.get('email')

    user = auth.authenticate(username=username,password=password)

    
    if user is not None :
        try:
            if (user.student.isStudent == True ) :
                auth.login(request,user)
                print(user.student.name, 'logged in')
                return True
            else:
                return False

        except :
            return False

    else:
        return False


def auth_student(request):

    if request.method == 'POST':
        if (request.POST.get('formtype') =='signupform'):
            username = request.POST.get('email')
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password1 = request.POST.get('confpassword')
            fullname = name.split()
            firstname = fullname[0]
            lastname = fullname[-1]


            if password == password1:
                    if User.objects.filter(username=username).exists():
                        messages.info(request, 'User name already exists')
                        return redirect(auth_student)
                        # return HttpResponse('id exists')

                    else:
                        user = User.objects.create_user(username=username,first_name=firstname, last_name=lastname, password=password, email=email)
                        user.save()

                        newStudent = Student(user=user, name=name, email=email)
                        newStudent.save()
                        stdResume = Resume(student=newStudent)
                        stdResume.save()
                        # messages.info(request, 'User Created Successfully')
                        signin(request)
                        messages.info(request, 'Sucessfully Registered and signed in.')
                        return redirect('internships')

            # return redirect('login')

        elif (request.POST.get('formtype')=='signinform'):
            if signin(request):
                messages.info(request, "Signed in successfully")
                return redirect('internships')
            else:
                messages.info(request, "invlid credentials")
                return redirect(auth_student)


    else:
        return render(request,'Student.html')

@login_required
def profile(request):
    std = request.user.student
    resume = std.resume
    certificate = Certificate.objects.filter(std_id = request.user.pk).order_by('-id')
    return render(request, 'StudentProfile.html', {'resume':resume, 'student':std, 'certificate': certificate})

@login_required
def profileEdit(request):

    std = request.user.student
    resume = std.resume
    if request.method == 'POST':
        email = request.POST.get('email')
        if email != std.email:
            if User.objects.filter(username=email).exists():
                messages.info(request, "This email is already in use")
            else:
                std.email = email
                request.user.email = email
                request.user.username = email         
            

        std.name = request.POST.get('name')
        fullname = std.name.split()
        request.user.first_name = fullname[0]
        request.user.last_name = fullname[-1]

        std.save()
        request.user.save()

        if 'image' in request.FILES:
            std.resume.pic = request.FILES['image']  

        if 'resume_file' in request.FILES:
            std.resume.resume_file = request.FILES['resume_file']

        std.resume.mob = request.POST.get('mob')
        std.resume.address = request.POST.get('address')
        std.resume.skills = request.POST.get('skills')
        std.resume.college = request.POST.get('college')
        std.resume.degree= request.POST.get('degree')
        std.resume.grad_year = request.POST.get('grad_year')
        std.resume.cgpa = request.POST.get('cgpa')
        std.resume.save()
        return redirect('profile')

    print(std.name)    
    return render(request, 'StudentProfileEdit.html', {'resume':resume, 'student':std})
    
@login_required
def dashboard(request):
    return render(request, 'StudentDashboard.html')

@login_required
def detail(request, post_id):
    if (request.user.student.isStudent == True):
        std = Student.objects.get(email=request.user.student.email)
        post = Internship.objects.get(id=post_id)

        status = InternshipAppliedDB.objects.filter(internship_id=post_id, student_id=std.id)

        print("status: ", len(status))

        return render(request, 'StudentCompanyViewDetails.html',
                      {'post': post, 'student': std, 'status': len(status)})

    else:
        messages.info(request, 'Please sign in as a student')
        return redirect(auth_student)



def Jaccard(x, y):
    """returns the jaccard similarity between two lists """
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    return intersection_cardinality / float(union_cardinality)

def internshipApplied(request, post_id):
    std = Student.objects.get(email=request.user.student.email)
    post = Internship.objects.get(id=post_id)

    student_id = std.pk
    internship_id = post.pk

    student_name = std.name
    student_email = std.email
    student_mob = std.resume.mob

    # Add Jacard Similarity Here
    matching = 0
    x = list(std.resume.skills) #student skills
    y=  post.skills   #comp skills

    print("the skills of the company internship are: ",y)

    ans = Jaccard(x, y)
    matching=ans*100;


    status = "pending"

    new_apply = InternshipAppliedDB(internship_id=internship_id, student_id=student_id, student_name = student_name, student_email = student_email, student_mob = student_mob, matching = matching, status=status)
    new_apply.save()

    # return redirect('/internships')
    return redirect('detail', post_id=post_id)

def StudentCertificateAdd(request):
    if request.method == "POST":
        title = request.POST.get('title')
        company = request.POST.get('company')
        cyear = request.POST.get('cyear')
        credential = request.POST.get('credential')

        print(title)
        print(company)
        print(cyear)
        print(credential)
        print(request.user.pk)

        new_certificate = Certificate(std_id = request.user.pk, title = title, company_name= company, complition_year= cyear, credential= credential )
        new_certificate.save()

        if 'Certificate_file' in request.FILES:
            new_certificate.certificate_file = request.FILES['Certificate_file']
            new_certificate.save()

        return redirect("profile")

    else:
        return render(request, 'StudentCertificateAdd.html')