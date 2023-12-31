from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .models import Userprofile

def vendor_detail(request, pk):
    user = User.objects.get(pk=pk)

    return render(request, 'userprofile/vendor_detail.html', {
        'user': user
    })