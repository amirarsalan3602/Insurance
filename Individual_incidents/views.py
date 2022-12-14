from django.shortcuts import render, redirect
from django.views import View

from Individual_incidents.forms import IndividualIncidentsForm
from Individual_incidents.models import IndividualIncidentsModel
from django.contrib.auth.mixins import LoginRequiredMixin

class Individual_Incidents(LoginRequiredMixin,View):
    template_name = 'Individual_incidents/Individual_incidents.html'
    form_class = IndividualIncidentsForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cl = form.cleaned_data
            IndividualIncidentsModel.objects.create(user = request.user,
                                                    number_people=cl['number_people'],
                                                    limit_time=cl['limit_time'],
                                                    job_category=cl['job_category'])

            return redirect('home:home')
        return render(request, self.template_name, {'form': form})
