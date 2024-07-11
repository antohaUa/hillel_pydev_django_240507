from django.http import HttpResponse
from parcel import models


def parcels_view(request):
    parcels = models.Parcel.objects.all()
    template = 'Parcels View:<br/>'
    for curr_parcel in parcels:
        template += f'<br/> [{curr_parcel.id}] Recipient: {curr_parcel.recipient} -> Sender: {curr_parcel.sender}'
    return HttpResponse(template)


def parcel_view(request, parcel_id):
    parcel = models.Parcel.objects.get(pk=parcel_id)
    template = f'Parcel [{parcel.id}]:<br/>'
    template += f'<br/> Size: [{parcel.size}] Recipient: {parcel.recipient}'
    return HttpResponse(template)
