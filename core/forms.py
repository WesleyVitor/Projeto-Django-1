from django import forms
from django.core.mail import EmailMessage

from .models import Produto

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f"Nome:{nome}\nEmail:{email}\nAssunto:{assunto}\nMensagem:{mensagem}"

        mail = EmailMessage(
            subject=assunto,
            body=conteudo,
            from_email="contato@gmail.com",
            to=[email,],
            headers={
                'Replay-To': "contato@gmail.com"
            }
        )

        mail.send()

class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ["nome","preco","estoque","imagem"]




