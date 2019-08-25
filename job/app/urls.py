from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
path('company/companyRegistration',views.company_register),
path('company/companyDashboard',views.company_dashboard),

path('recruiter/recruiterRegistration',views.recruiter_register),
path('recruiter/recruiterDashboard',views.recruiter_dashboard),
path('recruiter/postaJob',views.recruiter_post_a_job),

path('candidate/candidateRegistration',views.candidate_register),
path('candidate/candidateDashboard',views.candidate_dashboard),




path('login',views.login),
path('logout',views.logout),


]
