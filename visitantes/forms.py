from visitantes.models import Visitante
from django import forms

class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = {
            "nome_completo", "cpf", "data_nascimento", "numero_casa", "placa_veiculo"
        }

class AutorizaVisitanteForm(forms.ModelForm):
    morador_responsavel = forms.CharField(required=True)


    class Meta:
        model = Visitante
        fields = [
            "morador_responsavel"
        ]
        error_messages = {
            "morador_responsavel":{
                "required": "Informe o morador responsável"
            }
        }
