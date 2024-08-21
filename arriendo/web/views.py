from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Usuario

# Create your views here.
@login_required
def index(request):
    usuario = Usuario.objects.filter(user_id=request.user.id).first()
    tu = usuario.tu.tu_id

    if tu == 2:
        return render(request,"index.html",{'usuario':usuario})
    else:
        return render(request,"index.html",{'usuario':usuario})