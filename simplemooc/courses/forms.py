from django import forms

class ContactCourse(forms.Form):
    name = forms.CharField(label = 'Nome', max_length=100)
    email =  forms.EmailField(label = "E-mail")
    menssage = forms.CharField(
        label = 'Mensagens/Dúvida', widget=forms.Textarea
    )
