from django.shortcuts import render, get_object_or_404

from .models import Msg


def afficherMig(request, id):
    msg = get_object_or_404(Msg, id=id)
    return render(request, "communication/afficherMig.html", {"msg": msg})
