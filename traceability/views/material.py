from django.views import generic
from traceability.models.material import Material
from traceability.forms.material import MaterialCreate, MaterialUpdate


class MaterialDetail(generic.DetailView):
    model = Material


class MaterialList(generic.ListView):
    model = Material
    paginate_by = 25


class MaterialCreate(generic.CreateView):
    model = Material
    form_class = MaterialCreate


class MaterialUpdate(generic.UpdateView):
    model = Material
    form_class = MaterialUpdate
