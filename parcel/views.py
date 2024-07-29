import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from parcel import models


@login_required()
def parcels_view(request):
    user = request.user
    parcels = models.Parcel.objects.filter(recipient=user)
    context = {
        'parcels': [{'id': c_parcel.id, 'sender': c_parcel.sender, 'size': c_parcel.size, 'status': c_parcel.status,
                     'locker': c_parcel.locker, 'open_datetime': c_parcel.open_datetime} for c_parcel in parcels]}
    return render(request, 'parcels.html', context=context)


@login_required()
def parcel_view(request, parcel_id):
    if request.method == 'POST':
        parcel = models.Parcel.objects.get(pk=request.POST['parcel_id'])
        parcel.status = True
        parcel.open_datetime = datetime.datetime.now()
        if parcel.order_datetime is None:
            parcel.order_datetime = datetime.datetime.now()
        parcel.save()

        parcel.locker.status = True
        parcel.locker.save()
        return redirect('/parcel')

    parcel = models.Parcel.objects.get(pk=parcel_id)
    context = {'id': parcel.id, 'sender': parcel.sender, 'size': parcel.size, 'status': parcel.status,
               'locker': parcel.locker, 'open_datetime': parcel.open_datetime}
    return render(request, 'parcel.html', context=context)
