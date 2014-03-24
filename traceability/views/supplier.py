from django.views import generic
from traceability.models.supplier import Supplier


class SupplierDetail(generic.DetailView):
    template_name = 'traceability/supplier/supplier_detail.html'
    model = Supplier


class SupplierList(generic.ListView):
    template_name = 'traceability/supplier/supplier_list.html'
    model = Supplier
    paginate_by = 25


class SupplierCreate(generic.CreateView):
    template_name = 'traceability/supplier/supplier_form.html'
    model = Supplier


class SupplierUpdate(generic.UpdateView):
    template_name = 'traceability/supplier/supplier_form.html'
    model = Supplier
