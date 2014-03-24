from django.views import generic
from traceability.models.material import Material
from traceability.forms.material import MaterialCreate, MaterialUpdate


class MaterialDetail(generic.DetailView):
    template_name = 'traceability/material/material_detail.html'
    model = Material


class MaterialList(generic.ListView):
    template_name = 'traceability/material/material_list.html'
    model = Material
    paginate_by = 25


class MaterialCreate(generic.CreateView):
    template_name = 'traceability/material/material_form.html'
    model = Material
    form_class = MaterialCreate


class MaterialUpdate(generic.UpdateView):
    template_name = 'traceability/material/material_form.html'
    model = Material
    form_class = MaterialUpdate
