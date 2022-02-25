from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.views import generic
from .models import (
		User,
		Skill,
		Testimonial,
		Certificate,
		Interested,
		Academic,
		Job,
		Publication,
		Portfolio,
		ContactProfile,
	)
from personalinfo.forms import ContactForm
from django.http import HttpResponseRedirect
from django.utils.translation import activate

# Create your views here.


class IndexView(generic.TemplateView):
	template_name = "index.html"
	form_class = ContactForm
	

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		userprofile = User.objects.first()
		skills = Skill.objects.filter(is_key_skill=True)
		testimonials = Testimonial.objects.filter(is_active=True)
		certificates = Certificate.objects.filter(is_active=True)
		interested = Interested.objects.filter(active=True)
		academics = Academic.objects.all()
		publications = Publication.objects.all()
		jobs = Job.objects.all()
		projects = Portfolio.objects.all()
		

		context["userprofile"] = userprofile
		context["testimonials"] = testimonials
		context["certificates"] = certificates
		context["skills"] = skills
		context["interestes"] = interested
		context["academics"] = academics
		context["jobs"] = jobs
		context["publications"] = publications
		context["projects"] = projects
		
		context["form"] = ContactForm()

		return context


	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			new_contact = form.save()
			
			return HttpResponseRedirect('/')



class CertificateView(generic.DetailView):
	template_name = "certificate-details.html"

	def get_object(self):
		pk = self.kwargs.get('pk')
		certificate = get_object_or_404(Certificate, pk=pk)
		return certificate


class PortfolioView(generic.DetailView):
	template_name = "portfolio-details.html"

	def get_object(self):
		pk = self.kwargs.get('pk')
		portfolio = get_object_or_404(Portfolio, pk=pk)
		return portfolio


def change_lang(request):
	activate(request.GET.get('lang'))
	
	return redirect(request.GET.get('next'))

	


	


