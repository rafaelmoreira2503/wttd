from django.core import mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from eventex.subscriptions.forms import SubscriptionForm


def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST) # vem da view

        if not form.is_valid():


            #context = dict(name='Henrique Bastos',cpf='12345678901',email='henrique@bastos.net',phone='21-9874-5367')

            body = render_to_string('subscriptions/subscription_email.txt', form.cleaned_data)
            mail.send_mail('Confirmação de Inscrição', body, 'contato@eventex.com.br', ['contato@eventex.com.br',form.cleaned_data['email']])

            return HttpResponseRedirect('/inscricao/')
        else:

            return render(request,'subscriptions/subscription_form.html', form)
    else:
        context = {'form': SubscriptionForm()}
        return render(request,'subscriptions/subscription_form.html', context)