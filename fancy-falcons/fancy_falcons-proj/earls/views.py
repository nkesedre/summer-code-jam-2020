from django.shortcuts import render
from account.models import Account


def earl_list_view(request):
    queryset = Account.objects.all()
    context = {
        "earl_list": queryset
    }
    return render(request, "earls/earllist.html", context)


def earl_grid_view(request):
    queryset = Account.objects.all()
    context = {
        "earl_list": queryset
    }
    return render(request, "earls/earlgrid.html", context)
