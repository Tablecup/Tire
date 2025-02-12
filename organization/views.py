from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import UpdateView, CreateView, TemplateView, ListView
from . import models as m
from django.contrib import messages
from organization import forms as f
from authentication import models as um
from authentication import forms as fu
from django.utils import timezone
import datetime
# Для создания отчётов
# from django.http import HttpResponse
# from docx import *
# from io import BytesIO
# from datetime import datetime, date
# import locale




class DirectorHomeView(TemplateView):
    template_name = 'director/home.html'


class DirectorOrdersView(ListView):
    model = m.OrderStorage
    template_name = 'director/orders.html'
    context_object_name = 'orders'
    paginate_by = 7

    def get_date_range_default(self):
        date1 = timezone.now()
        date2 = timezone.now()
        return date1, date2

    def get_date_range(self):
        strptime = datetime.datetime.strptime
        try:
            date1 = (strptime(self.request.GET.get('date_from'), r'%Y-%m-%d'))
            date2 = (strptime(self.request.GET.get('date_until'), r'%Y-%m-%d'))
        except TypeError:
            date1, date2 = self.get_date_range_default()

        if date1 > date2:
            date1, date2 = date2, date1
        return date1, date2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date1, date2 = self.get_date_range()
        context['date_from'], context['date_until'] = (
            date1.strftime(r'%Y-%m-%d'), date2.strftime(r'%Y-%m-%d'))
        context['today'] = timezone.now()
        return context

    def get_queryset(self):
        queryset = m.OrderStorage.objects.all().order_by('-pk')
        date_from, date_until = self.get_date_range()
        queryset = queryset.filter(
            created_at__gte=datetime.datetime.combine(date_from, datetime.time.min),
            created_at__lte=datetime.datetime.combine(date_until, datetime.time.max)
        )
        return queryset



class DetailOrderViewDir(UpdateView):
    template_name = "director/order_detail_dir.html"
    model = m.OrderStorage
    form_class = f.UpdateOrderDir

    def get_queryset(self):
        return m.OrderStorage.objects.filter(pk=self.kwargs['pk'])

    def form_valid(self, form):
        messages.success(self.request, "The task was updated successfully.")
        return super(DetailOrderViewDir, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('directorOrdersDetail', kwargs={'pk': self.kwargs['pk']})


class CreateOrder(CreateView):
    success_url = reverse_lazy('directorOrders')
    template_name = "director/create_order.html"
    form_class = f.OrderCreate
    queryset = m.OrderStorage.objects.all()

    def form_valid(self, form):
        size = int(str(form.cleaned_data['size']))
        period = int(str(form.cleaned_data['period']))
        price = size * period
        form.instance.price = price
        form.instance.status = m.OrderStatus.CREATE
        return super().form_valid(form)

    def get_form_kwargs(self, ):
        ret = super().get_form_kwargs()
        print(ret)
        ret['initial'] = {
            'status': m.OrderStatus.CREATE,
        }
        return ret

class CreateUser(CreateView):
    template_name = 'director/create_user.html'
    success_url = reverse_lazy('create_user')
    form_class = fu.RegisterForm

class DirectorUsersView(TemplateView):
    template_name = 'director/users.html'


class DirectorStuffView(TemplateView):
    template_name = 'director/stuff.html'


class DirectorClientsView(TemplateView):
    template_name = 'director/clients.html'


class DirectorStatisticsView(TemplateView):
    template_name = 'director/statistics.html'


class ManagerHomeView(TemplateView):
    template_name = 'manager/home.html'


class ManagerOrdersView(TemplateView):
    template_name = 'manager/orders.html'


class ManagerEdit(UpdateView):
    template_name = 'manager/edit_profile_manager.html'
    form_class = f.SettingsProfile
    success_url = reverse_lazy('manager_edit')

    def get_object(self, **kwargs):
        return self.request.user


class PassChange(UpdateView):
    form_class = f.CustomPasswordChangeForm
    template_name = 'manager/pass_change.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


# def TestDocument(request):
#     locale.setlocale(
#         category=locale.LC_ALL,
#         locale="Russian"  # Note: do not use "de_DE" as it doesn't work
#     )
#     current_datetime = datetime.now()
#     str_current_datetime = str(current_datetime)
#     document = Document()
#     docx_title = "report" + str_current_datetime + ".docx"
#     # ---- Cover Letter ----
#     document.add_paragraph()
#     document.add_paragraph("%s" % date.today().strftime('%B %d, %Y'))
#
#     document.add_paragraph('Отчёт о заказах')
#     qs2 = m.OrderStorage.objects.all().order_by('pk')
#     qs2count = qs2.count() + 1
#     table = document.add_table(rows=qs2count, cols=8)
#     table.style = 'Table Grid'
#     table.cell(0, 0).text = 'Номер заказа'
#     table.cell(0, 1).text = 'Клиент'
#     table.cell(0, 2).text = 'Размер шины'
#     table.cell(0, 3).text = 'Период хранения'
#     table.cell(0, 4).text = 'Адрес сервиса'
#     table.cell(0, 5).text = 'Статус заказа'
#     table.cell(0, 6).text = 'Стоимость заказа'
#     table.cell(0, 7).text = 'Оплачен'
#
#     # Creating a table object
#
#     for order in m.OrderStorage.objects.all().order_by('pk'):
#
#         qs2 = m.OrderStorage.objects.all().order_by('pk')
#         row = qs2.count()
#         table.cell(row, 0).text = str(order.pk)
#         table.cell(row, 1).text = str(order.user)
#         table.cell(row, 2).text = str(order.size)
#         table.cell(row, 3).text = str(order.period)
#         if order.adress == None:
#             order.adress = "---"
#         table.cell(row, 4).text = str(order.adress)
#         table.cell(row, 5).text = str(order.get_status_display())
#         table.cell(row, 6).text = str(order.price)
#         if order.is_payed == True:
#             order.is_payed = "Да"
#         else:
#             order.is_payed = "Нет"
#         table.cell(row, 7).text = str(order.is_payed)
#
#     document.add_page_break()
#
#     # Prepare document for download
#     # -----------------------------
#     f = BytesIO()
#     document.save(f)
#     length = f.tell()
#     f.seek(0)
#     response = HttpResponse(
#         f.getvalue(),
#         content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
#     )
#     response['Content-Disposition'] = 'attachment; filename=' + docx_title
#     response['Content-Length'] = length
#     return response
