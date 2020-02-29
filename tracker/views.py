from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .index import Tracker
from .models import Tracker_incident
# Create your views here.
#function based view

def Tracker_log(request):
    if request.method == "POST":
        date          = request.POST.get("date")
        issue         = request.POST.get("issue")
        description   = request.POST.get("description")
        reporter      = request.POST.get("reporter")
        owner         = request.POST.get("owner")
        occ           = request.POST.get("occ")
        severity      = request.POST.get("severity")
        status        = request.POST.get("status")
        obj = Tracker_incident.objects.create(
                date        = date,
                issue       = issue,
                description = description,
                reporter    = reporter,
                owner       = owner,
                occ         = occ,
                severity    = severity,
                status      = status
            )
    # if request.method == "POST":
    #     form = Tracker(request.POST)
    #     if form.is_valid():
    #         obj = Tracker_incident.objects.create(
    #                 date        = form.cleand_data.get('date'),
    #                 issue       = form.cleand_data.get('issue'),
    #                 description = form.cleand_data.get('description'),
    #                 reporter    = form.cleand_data.get('reporter'),
    #                 owner       = form.cleand_data.get('owner'),
    #                 occ         = form.cleand_data.get('occ'),
    #                 severity    = form.cleand_data.get('severity'),
    #                 status      = form.cleand_data.get('status')
    #             )
        return HttpResponseRedirect("/success")
    template_name = 'log.html'
    context = {}
    return render(request, template_name, context)

class Success(TemplateView):
    template_name = 'success.html'


def Tracker_search(request):
    global date_track
    template_name = 'track.html'
    if request.method == "POST":
        date_track = request.POST.get("date_track")
        print(date_track)
        return HttpResponseRedirect("/t_queryset")
    template_name = 'track.html'
    context = {}
    return render(request, template_name, context)



def Tracker_view(request):
    template_name = 'track_incident_view.html'
    queryset = Tracker_incident.objects.all()
    context = {
        "object_list": queryset.filter(date=date_track)
    }
    return render(request, template_name, context)

class IndexView(TemplateView):
    template_name = 'index.html'





# class IndexView(TemplateView):
#     template_name = 'index.html'
