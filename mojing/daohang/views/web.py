from django.core.exceptions import FieldDoesNotExist
import json
from django.shortcuts import render
from numpy import unicode

import daohang.ops.daohangapi as daohangapi



def index_view(request):
    try:
        print("==============%s" % "2222222222222222222222222")
        origin_dict=daohangapi.address_to_point('太阳宫地铁站C口')
        destination_dict=daohangapi.address_to_point('df')
        origin= origin_dict.geocodes[0].location if origin_dict.status==1 else ''
        print("==============%s"%origin_dict)
        # destination= destination_dict.geocodes[0].location if destination_dict.status==1 else ''
    except FieldDoesNotExist:
        raise(u"位置转换坐标失败！")
    # usetime=daohangapi.get_usetime(origin,destination)
    return render(request,'daohang/index.html',{"usetime":origin_dict})
