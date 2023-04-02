from django.shortcuts import render
from django import views
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.utils import timezone
import datetime
from core.mixins import ExtraContextMixin
from organization import models as m
from django.shortcuts import HttpResponseRedirect


class HomeView(generic.TemplateView, ExtraContextMixin):
    template_name = 'clientpart/home.html'
    extra_context = {
        'header_selected_index': 0
    }

from tirestorage import forms as f
class StartOrder(generic.CreateView):
    template_name = 'clientpart/order_create.html'
    success_url = reverse_lazy('home')
    form_class = f.OrderCreateForm
    queryset = m.TireStore.objects.all()

    def get_form(self, form_class=None):
        from organization.models import TireSize, PeriodOfStorage, QuantityOfTires
        if form_class is None:
            form_class = self.get_form_class()
        form = form_class(**self.get_form_kwargs())
        form.fields['size'].queryset = TireSize.objects.all()
        form.fields['period'].queryset = PeriodOfStorage.objects.all()
        form.fields['quantity'].queryset = QuantityOfTires.objects.all()
        return form

    def get_form_kwargs(self):
        ret = super().get_form_kwargs()
        ret['initial'] = {
            'user': self.request.user.pk,
        }
        return ret
    # Вывод данных на страниц