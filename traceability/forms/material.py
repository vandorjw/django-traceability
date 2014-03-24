from django.forms import ModelForm
from traceability.models.material import Material

class MaterialCreate(ModelForm):
    class Meta:
        model = Material
        exclude = ('incidents', )

class MaterialUpdate(ModelForm):
    class Meta:
        model = Material
        fields = ['incidents', ]
