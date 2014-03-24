from django.views import generic
from traceability.models.customer import Customer


class CustomerDetail(generic.DetailView):
    template_name = 'traceability/customer/customer_detail.html'
    model = Customer


class CustomerList(generic.ListView):
    template_name = 'traceability/customer/customer_list.html'
    model = Customer
    paginate_by = 25


class CustomerCreate(generic.CreateView):
    template_name = 'traceability/customer/customer_form.html'
    model = Customer


class CustomerUpdate(generic.UpdateView):
    template_name = 'traceability/customer/customer_form.html'
    model = Customer
