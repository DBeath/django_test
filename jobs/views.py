from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic

from jobs.models import Job

# def index(request):
# 	jobs_list = Job.objects.all()
# 	context = {'jobs_list': jobs_list}
# 	return render(request, 'jobs/index.html', context)

# def detail(request, job_id):
# 	return HttpResponse("You're looking at job %s." % job_id)

class IndexView(generic.ListView):
	template_name = 'jobs/index.html'
	context_object_name = 'jobs_list'

	def get_queryset(self):
		return Job.objects.all()


class DetailView(generic.DetailView):
	model = Job
	template_name = 'jobs/detail.html'
