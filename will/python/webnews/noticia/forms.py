from django.forms import ModelForm
from .models import Autor

class AutorForm(ModelForm):
    class Meta:
        model_class = Autor
        fields = '__all__'


# class FilmeForm(ModelForm):
#     class Meta:
#         model_class = Filme
#         fields = '__all__'
