from django.shortcuts import render, redirect
from .forms import AgendamentoForm
from django.contrib.auth.decorators import login_required

#       cbv        -         fbv
#Class based Views - Function based Views


def home(request):
    return render(request, "home.html")

@login_required
def agendar(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            agendamento = form.save(commit=False)
            agendamento.usuario = request.user
            agendamento.save()
            return redirect('sucesso')
        else:
            # Não é necessário criar um novo formulário aqui.
            # O formulário com erros será renderizado abaixo.
            pass
    else:
        form = AgendamentoForm()
    return render(request, 'agendar.html', {'form': form})

@login_required
def sucesso(request):
    return render(request, 'sucesso.html')

