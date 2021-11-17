from django.urls.base import reverse_lazy
from django.views.generic.base import TemplateView, View
from django.views.generic.edit import FormView

from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from .forms import ResponseForm

# Create your views here.


class ResponseCollectionView(View):
    template_name = 'response/response_collection.html'

    def get(self, request, *args, **kwargs):
        form = ResponseForm(report_name='The First Shiftbid Report')
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = ResponseForm(data=request.POST,
                            report_name='The First Shiftbid Report')
        context = {'form': form}
        if form.is_valid():
            print(form)
            form = ResponseForm(report_name='The First Shiftbid Report')
            return render(request, 'response/thanks.html', context)
        return render(request, 'response/response_collection.html', context)


class ResponseThanksView(TemplateView):
    template_name = 'response/thanks.html'
