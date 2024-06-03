from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm


# CREATE
def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'crud_app/item_form.html', {'form': form})

# READ
def item_list(request):
    items = Item.objects.all()
    return render(request, 'crud_app/item_list.html', {'items': items})

# UPDATE
def item_update(request, pk):
    item = Item.objects.get(pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'crud_app/item_form.html', {'form': form})

# DELETE
def item_delete(request, pk):
    item = Item.objects.get(pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'crud_app/item_confirm_delete.html', {'item': item})

