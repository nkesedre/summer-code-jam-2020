from django.shortcuts import render
from account.models import Account


def earl_list_view(request):
    queryset = Account.objects.all()
    context = {
        "earl_list": queryset,
        "users": queryset.filter(is_user=True),
        "ficthist": queryset.filter(is_user=False),
        "active_page": "browse",
    }
    return render(request, "earls/earllist.html", context)


def earl_grid_view(request):
    queryset = Account.objects.all()
    context = {
        "earl_list": queryset,
        "active_page": "browse",
    }
    return render(request, "earls/earlgrid.html", context)
