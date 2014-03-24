from django.views import generic
from traceability.models.customer import Customer


class CustomerDetail(generic.DetailView):
    model = Customer


class CustomerList(generic.ListView):
    model = Customer
    paginate_by = 25


class CustomerCreate(generic.CreateView):
    model = Customer


class CustomerUpdate(generic.UpdateView):
    model = Customer
