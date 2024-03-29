from django.shortcuts import render, redirect
from django.views import View
from .forms import ThirdPartyForm
from car.models import ThirdPartyModel
from django.contrib.auth.mixins import LoginRequiredMixin
from car.forms_choices import cars
from datetime import datetime
from django.contrib import messages

class RegisterView(LoginRequiredMixin, View):
    form_class = ThirdPartyForm
    template_name = 'car/ThirdPartyRegister.html'
    http_method_names =  ['get','post']

    def http_method_not_allowed(self, request, *args, **kwargs):
        return super().http_method_not_allowed(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        
        if form.is_valid():
            cl = form.cleaned_data
            ThirdPartyModel.objects.create(user=request.user, vehicle_type=cl["vehicle_type"],
                                           car_type=cars[cl["car_type_name"]
                                                         ], used=cl["used"],
                                           car_type_name=cl["car_type_name"],
                                           year_of_manufacture=cl["year_of_manufacture"],
                                           third_discount=cl["third_discount"],
                                           accident_discounts=cl["accident_discounts"],
                                           number_of_accidents=cl["number_of_accidents"],
                                           number_of_incidents=cl["number_of_incidents"],
                                           expiration_date=datetime.now().date(),
                                           face_image=request.FILES["face_image"],
                                           back_image=request.FILES["back_image"],
                                           image_insurance_policy=request.FILES["image_insurance_policy"],
                                           )
            messages.success(request, "بیمه شما ثبت شد همکاران ما با شما تماس میگیرند", "success")
            return redirect("home:home")
        messages.error(request, "اظلاعات را با دقت وارد کنید", "danger")
        return render(request, self.template_name, {"form": form})

