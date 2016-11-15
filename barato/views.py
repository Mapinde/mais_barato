from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Produto, Fornecedor, Marca
from django.utils import timezone
import datetime
from django.template.response import TemplateResponse
from .forms import SearchForm, ContactForm
from django.core.mail import send_mail
from django.template import loader
from django.http import HttpResponse

def produto_lista(request):
    produtos = Produto.objects.all()
    paginator = Paginator(produtos,6)

    page = request.GET.get('page')
    try:
        produto_lista = paginator.page(page)
    except PageNotAnInteger:
        produto_lista = paginator.page(1)
    except EmptyPage:
        produto_lista = paginator.page(paginator.num_pages)

    template = loader.get_template('barato/produto_lista.html')
    context = {
        'produto_lista': produto_lista,
        'produtos': produtos
    }
    return HttpResponse(template.render(context, request))


def sobre_nos(request):
    return render(request, 'barato/sobre_nos.html', {})


def produto_detalhe(request, pro_nome,pk):
    endereco_cliente = request.META['REMOTE_ADDR']
    produto = Produto.objects.filter(pk=pk)
    produto_relacionados = Produto.objects.filter(nome__contains=pro_nome)
    dia = datetime.date.today()
    with open("barato/logs/" + (str(dia)) + ".txt", "a") as myfile:
        myfile.write((str(pro_nome)) + " -------------------- IP: " + (
        str(endereco_cliente)) + " -------------------- DATA: " + (str(datetime.datetime.now())) + " \n")
        myfile.close()

    template = loader.get_template('barato/produto_detalhe.html')
    context = {
        'produto_relacionados': produto_relacionados,
        'produto':produto,
    }
    return HttpResponse(template.render(context, request))


def ver_fornecedor(request):
    fornecedores = Fornecedor.objects.all()
    template = loader.get_template('barato/fornecedores.html')
    context = {
        'fornecedores': fornecedores,
    }
    return HttpResponse(template.render(context, request))

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['onelio.mapinde@gmail.com']
            if cc_myself:
                recipients.append(sender)
            send_mail(subject, message, sender, recipients)
    else:
        form = ContactForm()

	template = loader.get_template('barato/contact.html')
	context = {
		'form': form,
	}
	return HttpResponse(template.render(context, request))

