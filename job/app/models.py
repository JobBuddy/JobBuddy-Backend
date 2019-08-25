from django.db import models

# Create your models here.
class companyInfo(models.Model):
    email=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100000,default='')
    sector=models.CharField(max_length=1000)
    website=models.CharField(max_length=1000)
    about_company=models.CharField(max_length=1000)
    domain=models.CharField(max_length=1000)


class candidateInfo(models.Model):
    email=models.CharField(max_length=100)
    name=models.CharField(max_length=100000,default='')
    mobile=models.CharField(max_length=1000)
    clgname=models.CharField(max_length=1000)
    percentage=models.CharField(max_length=1000)
    workexp=models.CharField(max_length=1000)
    location=models.CharField(max_length=1000)


class recruiterInfo(models.Model):
    email=models.CharField(max_length=100)
    name=models.CharField(max_length=100000,default='')
    mobile=models.CharField(max_length=1000)
    pan=models.CharField(max_length=1000)
    qualification=models.CharField(max_length=1000)
    location=models.CharField(max_length=1000)


class recruiterCompany(models.Model):
    rec_email=models.CharField(max_length=1000)
    company_name=models.CharField(max_length=1000)



class JobId(models.Model):
    id=models.IntegerField()
    name=models.CharField(max_length=1000)

class Job(models.Model):
    job_title=models.CharField(max_length=1000)
    job_type=models.CharField(max_length=1000)
    qualification=models.CharField(max_length=1000)
    location=models.CharField(max_length=1000)
    salary=models.CharField(max_length=1000)
    work_exp=models.CharField(max_length=1000)
    start_date=models.CharField(max_length=1000)
    openings=models.CharField(max_length=1000)
    description=models.CharField(max_length=1000)
    company_name=models.CharField(max_length=1000)
    job_id=models.IntegerField()

class studentJobs(models.Model):
    student_email=models.CharField(max_length=1000)
    job_id=models.CharField(max_length=1000)
