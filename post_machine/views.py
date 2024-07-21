from django.shortcuts import render
from django.http import HttpResponse

from post_machine import models


def post_machines_view(request):
    pms = models.PostMachine.objects.all()
    context = {'post_machines': [{'id': pm.id, 'address': pm.address, 'city': pm.city} for pm in pms]}
    return render(request, 'post_machines.html', context=context)


def post_machine_view(request, pm_id):
    curr_pm = models.PostMachine.objects.get(id=pm_id)
    lockers = models.Locker.objects.filter(post_machine=curr_pm)

    # template = f'PostMachine [{curr_pm.id}]:<br/>'
    # for curr_locker in lockers:
    #     template += f'<br/> LockerID: [{curr_locker.id}] Size: {curr_locker.size} Status: {curr_locker.status}'
    # return HttpResponse(template)

    context = {'post_machine': {'id': curr_pm.id, 'address': curr_pm.address, 'city': curr_pm.city},
               'lockers': [{'id': curr_locker.id, 'size': curr_locker.size, 'status': curr_locker.status} for
                           curr_locker in lockers]}
    return render(request, 'post_machine.html', context=context)


def post_machine_locker_view(request, pm_id, locker_id):
    curr_locker = models.Locker.objects.get(post_machine=pm_id, pk=locker_id)
    template = f'Locker [{curr_locker.id}]:<br/>'
    template += f'<br/> Size: [{curr_locker.size}] Status: {curr_locker.status}'
    return HttpResponse(template)
