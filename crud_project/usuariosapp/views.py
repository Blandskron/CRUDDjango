from django.shortcuts import render, redirect
from .models import Usuarios
from .forms import UsuariosForm


# CREATE
def usuarios_create(request):
    if request.method == 'POST':
        form = UsuariosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios_list')
    else:
        form = UsuariosForm()
    return render(request, 'usuariosapp/usuario_form.html', {'form': form})

# READ
def usuarios_list(request):
    usuarios = Usuarios.objects.all()
    return render(request, 'usuariosapp/usuario_list.html', {'usuarios': usuarios})

# UPDATE
def usuarios_update(request, pk):
    usuarios = Usuarios.objects.get(pk=pk)
    if request.method == 'POST':
        form = UsuariosForm(request.POST, instance=usuarios)
        if form.is_valid():
            form.save()
            return redirect('usuarios_list')
    else:
        form = UsuariosForm(instance=usuarios)
    return render(request, 'usuariosapp/usuario_form.html', {'form': form})

# DELETE
def usuarios_delete(request, pk):
    usuario = Usuarios.objects.get(pk=pk)
# DELETE
def item_delete(request, pk):
    item = Item.objects.get(pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'crud_app/item_confirm_delete.html', {'item': item})

    if request.method == 'POST':
        usuario.delete()
        return redirect('usuarios_list')
    return render(request, 'usuariosapp/usuario_delete.html', {'usuario': usuario})

