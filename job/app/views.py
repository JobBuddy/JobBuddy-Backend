from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import companyInfo,recruiterCompany,candidateInfo,recruiterInfo,studentJobs,Job,JobId


def candidate_register(request):
    if(request.method == 'POST'):
        name=request.POST['name']
        email=request.POST['email']
        mobile=request.POST['mobile']
        clgname=request.POST['clgname']
        percentage=request.POST['percentage']
        workexp=request.POST['workexp']
        location=request.POST['location']
        password=request.POST['password']
        q=User.objects.filter(email=email)
        if(len(q)>=1):
            return render(request,'app/candidate/candidateRegistration.html')


        user=User.objects.create_user(email=email,password=password,username=email,first_name='candidate')

        c=candidateInfo(email=email,name=name,mobile=mobile,workexp=workexp,location=location,percentage=percentage,clgname=clgname)

        auth_login(request,user)
        c.save()
        return render(request,'app/candidate/candidateDashboard.html')
    else:
        return render(request,'app/candidate/candidateRegistration.html')



def company_register(request):
    if(request.method == 'POST'):
        cn=request.POST['company_name']
        sector=request.POST['sector']
        website=request.POST['website']
        ac=request.POST['about_company']
        email=request.POST['email']
        password=request.POST['password']
        q=User.objects.filter(email=email)
        if(len(q)>=1):
            return render(request,'app/company/companyRegistration.html')

        te=email
        te=te.split('@')
        domain=te[1]
        user=User.objects.create_user(email=email,password=password,username=email,first_name='company')

        c=companyInfo(company_name=cn,sector=sector,website=website,email=email,about_company=ac,domain=domain)

        auth_login(request,user)
        c.save()
        return render(request,'app/company/companyDashboard.html')
    else:
        return render(request,'app/company/companyRegistration.html')



def recruiter_register(request):
    if(request.method == 'POST'):
        name=request.POST['name']
        mobile=request.POST['mobile']
        pan=request.POST['pan']
        qualification=request.POST['qualification']
        location=request.POST['location']
        email=request.POST['email']
        password=request.POST['password']
        q=User.objects.filter(email=email)
        if(len(q)>=1):
            return render(request,'app/recruiter/recruiterRegistration.html')

        te=email
        te=te.split('@')
        domain=te[1]

        li=companyInfo.objects.all()
        arr=[]
        for i in li:
            arr.append(i.domain)
        if(domain not in arr):
            return render(request,'app/recruiter/recruiterRegistration.html')

        for i in li:
            if(i.domain==domain):
                name=i.company_name
                break

        obj=recruiterCompany(company_name=name,rec_email=email)

        user=User.objects.create_user(email=email,password=password,username=email,first_name='recruiter')

        c=recruiterInfo(email=email,name=name,mobile=mobile,qualification=qualification,location=location,pan=pan)

        auth_login(request,user)
        c.save()
        return render(request,'app/recruiter/recruiterDashboard.html')
    else:
        return render(request,'app/recruiter/recruiterRegistration.html')




def login(request):
    if(request.user.is_authenticated):
        if(request.user.first_name=='company'):
            return render(request,'app/company/companyDashboard.html')
        if(request.user.first_name=='recruiter'):
            return render(request,'app/recruiter/recruiterDashboard.html')
        if(request.user.first_name=='candidate'):
            return render(request,'app/candidate/candidateDashboard.html')

    if(request.method=='POST'):
        email=request.POST['email']
        password=request.POST['password']
        q=User.objects.filter(email=email)

        if(len(q)==0):
            return render(request,'app/login.html',{"error_msg":"EMAIL DOESNOT EXIST!"})
        else:
            uname=q[0].username
            user=authenticate(username=email,password=password)
        if(user is None):
            return render(request,'app/login.html',{"error_msg":"INVALID CREDENTIALS!"})

        auth_login(request,user)

        if(request.user.first_name=='company'):
            return render(request,'app/company/companyDashboard.html')
        if(request.user.first_name=='recruiter'):
            return render(request,'app/recruiter/recruiterDashboard.html')
        if(request.user.first_name=='candidate'):
            return render(request,'app/candidate/candidateDashboard.html')

    return render(request,'app/login.html')



def logout(request):
    auth_logout(request)
    return render(request,'app/login.html')



def candidate_dashboard(request):
    if(request.user.is_authenticated):
        # see all the jobs available and the jobs applied
        j=Job.objects.all()
        q=studentJobs.objects.filter(student_email=request.user.email)
        q=q.job_id
        q=q.split(',')
        q=q[:-1]
        for i in range(len(q)):
            q[i]=int(q[i])
        applied=[]
        notapplied=[]

        for i in j:
            if(i.job_id in q):
                applied.append(i)
            else:
                notapplied.append(i)
        return render(request,'app/candidate/candidateDashboard.html'{'applied':applied,'notapplied':notapplied})

    else:
        return render(request,'app/login.html')

def company_dashboard(request):
    if(request.user.is_authenticated):
        # see the recruiters info if any
        #see the jobs posted by him
        #see the candidates applied to each job
        c=companyInfo.objects.filter(email=request.user.email)
        c=c[0].company_name

        j=Job.objects.filter(company_name=c)
        return render(request,'app/company/companyDashboard',{'j':j})

    else:
        return render(request,'app/login.html')

def recruiter_dashboard(request):
    if(request.user.is_authenticated):
        # should be able to post a job
        q=recruiterCompany.objects.all()
        for i in q:
            if(i.rec_email==request.user.email):
                company_name=i.company_name
                break
        j=Job.objects.all()
        same_company=[]
        other_company=[]
        for i in j:
            if(i.company_name==company_name):
                same_company.append(i)
            else:
                other_company.append(i)

        return render(request,'app/recruiter/recruiterDashboard.html',{'same_company':same_company,'other_company':other_company})

    else:
        return render(request,'app/login.html')

def recruiter_post_a_job(request):
    if(request.user.is_authenticated):
        if(request.method=='POST'):
            job_title=request.POST['job_title']
            job_type=request.POST['job_type']
            qualification=request.POST['qualification']
            location=request.POST['location']
            salary=request.POST['salary']
            work_exp=request.POST['work_exp']
            start_date=request.POST['start_date']
            openings=request.POST['openings']
            description=request.POST['description']
            q=recruiterCompany.objects.all()
            for i in q:
                if(i.rec_email==request.user.email):
                    company_name=i.company_name
                    break
            q=JobId.objects.get(name='job')
            if(len(q)==0):
                j=JobId(name='job',id=1)
                j.save()
                q=[j]

            q=q[0]
            idd=q.id
            q.id+=1
            q.save()
            j=Job(company_name=company_name,job_id=idd,job_title=job_title,job_type=job_type,qualification=qualification,location=location,salary=salary,work_exp=work_exp,start_date=start_date,openings=openings,description=description)
            j.save()
            q=recruiterCompany.objects.all()
            for i in q:
                if(i.rec_email==request.user.email):
                    company_name=i.company_name
                    break
            j=Job.objects.all()
            same_company=[]
            other_company=[]
            for i in j:
                if(i.company_name==company_name):
                    same_company.append(i)
                else:
                    other_company.append(i)

            return render(request,'app/recruiter/recruiterDashboard.html',{'same_company':same_company,'other_company':other_company})
        else:
            return render(request,'app/recruiter/postajob.html')


    else:
        return render(request,'app/login.html')

    
