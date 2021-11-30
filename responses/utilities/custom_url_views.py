from django.urls import path
from django.views.generic.base import View
from django.shortcuts import render

from shiftbid.models import Shiftbid
from responses.forms import ResponseForm
from responses.views import ResponseCollectionView

urlpatterns = []

report_name_list = []


# class ResponseCollectionView(View):
#     template_name = 'response/response_collection.html'

#     def __init__(self, report_name, **kwargs):
#         super().__init__(**kwargs)
#         self.report_name = report_name

#     def get(self, request, *args, **kwargs):
#         form = ResponseForm(report_name=self.report_name)
#         context = {'form': form}
#         return render(request, self.template_name, context)

#     def post(self, request, *args, **kwargs):
#         form = ResponseForm(data=request.POST,
#                             report_name=self.report_name)
#         context = {'form': form}
#         if form.is_valid():
#             print(form)
#             form = ResponseForm(report_name=self.report_name)
#             return render(request, 'response/thanks.html', context)
#         return render(request, 'response/response_collection.html', context)


def get_report_names():
    shiftbid_objects = Shiftbid.objects.all()

    for shiftbid in shiftbid_objects:
        report_name_list.append(shiftbid.report_name)


def create_custom_views_url():
    get_report_names()

    for report_name in report_name_list:
        the_view = ResponseCollectionView(report_name=report_name)
        urlpatterns.append(
            path(f'response_collection/{report_name}', the_view.as_view()))
