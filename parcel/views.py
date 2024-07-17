from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from parcel import models


@login_required()
def parcels_view(request):
    user = request.user
    parcels = models.Parcel.objects.filter(recipient=user)
    context = {
        'parcels': [{'id': c_parcel.id, 'sender': c_parcel.sender, 'size': c_parcel.size, 'status': c_parcel.status} for
                    c_parcel in parcels]}
    return render(request, 'parcels.html', context=context)


@login_required()
def parcel_view(request, parcel_id):
    parcel = models.Parcel.objects.get(pk=parcel_id)
    context = {'id': parcel.id, 'sender': parcel.sender, 'size': parcel.size, 'status': parcel.status }
    return render(request, 'parcel.html', context=context)
