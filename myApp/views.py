from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from .models import Company
from .forms import ApplicantForm


class HomePageView(ListView):
    model = Company
    template_name = "home.html"


def form_view(request):
    if request.method == "POST":
        form = ApplicantForm(request.POST)
        if form.is_valid():
            print("form is checked")
            return HttpResponse("Got it - thanks")
            # return HttpResponseRedirect("/Got_it_page/")
    else:
        form = ApplicantForm()
        # context = {'form': ApplicantForm()}
    return render(request, "form.html", {"form": form})
