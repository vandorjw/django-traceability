from django.views import generic
from supplier.models import Supplier


class SupplierDetailView(generic.DetailView):
    model = Supplier


class SupplierListView(generic.ListView):
    model = Supplier
    paginate_by = 25


class SupplierCreateView(generic.CreateView):
    model = Supplier


class SupplierUpdateView(generic.UpdateView):
    model = Supplier
