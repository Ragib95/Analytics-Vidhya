from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from models import *
import csv
# Create your views here.


def index(request):
    return render_to_response("jobs/nav.html")


def jobs(request):
    candidates = Candidates.objects.all()
    return render_to_response('jobs/index.html', {'candidates': candidates})


def candidate(request, candidate_name):
    candidate_detail = Candidates.objects.get(name=candidate_name)
    return render_to_response('jobs/candidate.html', {'candidate': candidate_detail})


def search(request):
    total = 0
    candidate_list = {}
    loc = ' '
    skills = ' '
    if 'location' in request.GET and request.GET['location'] and 'skills' in request.GET and request.GET['skills']:
        loc = request.GET['location']
        skills = request.GET['skills']
        candidate_list = Candidates.objects.filter(skills__icontains=skills, preferred_loc__icontains=loc)
        total = candidate_list.count()
    if 'location' in request.GET and request.GET['location']:
        loc = request.GET['location']
        candidate_list = Candidates.objects.filter(preferred_loc__icontains=loc)
        total = candidate_list.count()
    if 'skills' in request.GET and request.GET['skills']:
        skills = request.GET['skills']
        candidate_list = Candidates.objects.filter(skills__icontains=skills)
        total = candidate_list.count()

    return render_to_response('jobs/search.html', {'query': '', 'total': total, 'candidates': candidate_list, 'location': loc, 'skills': skills})


def some_view(request, location, skills):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="candidateslist.csv"'

    writer = csv.writer(response)
    writer.writerow(['serial_no', 'resume', 'name', 'mobile', 'email', 'work_experience', 'analytics_experience', 'current_loc', 'corrected_loc', 'nearest_city', 'preferred_loc', 'ctc', 'current_employer', 'current_designation', 'skills', 'ug_course', 'ug_institute', 'ug_tier1', 'ug_passing', 'pg_course', 'pg_institute', 'pg_passing', 'post_pg'])
    if location != ' ' and skills != ' ':
        for cand in Candidates.objects.filter(skills__icontains=skills, preferred_loc__icontains=location):
            writer.writerow([cand.serial_no, cand.resume, cand.name, cand.mobile, cand.email, cand.work_experience, cand.analytics_experience, cand.current_loc, cand.corrected_loc, cand.nearest_city, cand.preferred_loc, cand.ctc, cand.current_employer, cand.current_designation, cand.skills, cand.ug_course, cand.ug_institute, cand.ug_tier1, cand.ug_passing, cand.pg_course, cand.pg_institute, cand.pg_passing, cand.post_pg])
    if location == ' ':
        for cand in Candidates.objects.filter(skills__icontains=skills):
            writer.writerow([cand.serial_no, cand.resume, cand.name, cand.mobile, cand.email, cand.work_experience, cand.analytics_experience, cand.current_loc, cand.corrected_loc, cand.nearest_city, cand.preferred_loc, cand.ctc, cand.current_employer, cand.current_designation, cand.skills, cand.ug_course, cand.ug_institute, cand.ug_tier1, cand.ug_passing, cand.pg_course, cand.pg_institute, cand.pg_passing, cand.post_pg])

    if skills == ' ':
        for cand in Candidates.objects.filter(preferred_loc__icontains=location):
            writer.writerow([cand.serial_no, cand.resume, cand.name, cand.mobile, cand.email, cand.work_experience, cand.analytics_experience, cand.current_loc, cand.corrected_loc, cand.nearest_city, cand.preferred_loc, cand.ctc, cand.current_employer, cand.current_designation, cand.skills, cand.ug_course, cand.ug_institute, cand.ug_tier1, cand.ug_passing, cand.pg_course, cand.pg_institute, cand.pg_passing, cand.post_pg])
    return response

