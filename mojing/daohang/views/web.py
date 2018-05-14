from django.core.exceptions import FieldDoesNotExist
import json
from django.shortcuts import render
from numpy import unicode

import daohang.ops.daohang as daohang



def index_view(request):
    total_time=daohang.get_total_time()
    return render(request,'daohang/index.html',{"total_time":total_time})
