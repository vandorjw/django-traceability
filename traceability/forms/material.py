from django.forms import ModelForm
from traceability.models.material import Material

class MaterialCreateForm(ModelForm):
    class Meta:
        model = Material
        exclude = ('incidents', )

class MaterialUpdateForm(ModelForm):
    class Meta:
        model = Material
        fields = ['incidents', ]
