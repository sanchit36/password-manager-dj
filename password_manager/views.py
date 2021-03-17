from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .form import AddSiteForm
from .models import Site
from .utils import decrypt_user_data, encrypt_user_data

import json


@login_required()
def pass_list_view(request):
    sites = Site.objects.filter(user=request.user)
    form = AddSiteForm()
    if request.method == "POST":
        data = json.loads(request.body)
        site = Site.objects.get(id=data['site_id'])
        print(site)
        msg = ''
        try:
            msg = decrypt_user_data(request.user.username,
                                    request.user.password, site.password)
        except:
            msg = "error"
        return JsonResponse({"msg": msg})
    return render(request, 'index.html', {'sites': sites, "form": form})


def add_site(request):
    if request.method == "POST":
        form = AddSiteForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
    return redirect('/')


def delete_site(request, pk):
    site = get_object_or_404(Site, id=pk, user=request.user)
    site.delete()
    return redirect('/')


def edit_site(request, pk):
    site = get_object_or_404(Site, id=pk, user=request.user)
    if request.method == "POST":
        print(request.POST['password'])
        site.password = request.POST['password']
        site.save()
        return redirect('/')
    return render(request, 'edit_site.html', {"site": site, "title": "Edit Site"})
