
from django.core.exceptions import FieldDoesNotExist
from django.shortcuts import render_to_response, render
import daohang.ops.daohangapi as daohangapi


def index_view(request):
    try:
        origin_dict=daohangapi.address_to_point('太阳宫地铁')
        destination_dict=daohangapi.address_to_point('团结湖地铁')
        origin= origin_dict.geocodes[0].location if origin_dict.status==1 else ''
        destination= destination_dict.geocodes[0].location if destination_dict.status==1 else ''
    except FieldDoesNotExist:
        raise(u"位置转换坐标失败！")
    usetime=daohangapi.get_usetime(origin,destination)
    return render(request,'daohang/index.html',{"usetime":usetime})
