from django.core.exceptions import FieldDoesNotExist
import json
from django.shortcuts import render
from numpy import unicode

import daohang.ops.daohangapi as daohangapi



def index_view(request):
    try:
        origin_dict=json.loads((daohangapi.address_to_point('星河皓月小区','廊坊市')).decode("utf-8"))
        destination_dict=json.loads((daohangapi.address_to_point('三元桥地铁C1口','北京市')).decode("utf-8"))
        origin= origin_dict.get("geocodes",[])[0].get("location",'') if (origin_dict.get('status',"0") =="1") else ''#获取开始地点坐标
        destination= destination_dict.get("geocodes",[])[0].get("location", '') if (destination_dict.get('status',"0") == "1") else ''#获取结束地点坐标
    except FieldDoesNotExist:
        raise(u"位置转换坐标失败！")
    print("=========origin,destination:%s,%s"%(origin,destination))
    daohang_result=json.loads((daohangapi.get_usetime(origin,destination)).decode("utf-8"))
    if daohang_result.get("status","0")=="1":
        distance=daohang_result.get("route",{}).get("paths",[])[0].get("distance","")#两地之间距离 米
        usetime = daohang_result.get("route", {}).get("paths", [])[0].get("duration", "")#开车花费时间 秒
        taxi_cost = daohang_result.get("route", {}).get("taxi_cost", "")#打车花费 元
    return render(request,'daohang/index.html',{"distance":distance,"usetime":usetime,"taxi_cost":taxi_cost})
