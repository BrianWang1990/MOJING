import json
import urllib
import datetime
from urllib.parse import quote #quote 为了解决url中英文混排的问题
from mojing.settings import baidu_key,home_coordinate, office_coordinate,caofang_subway_coordinate,guomao_subway_coordinate


def get_total_time():

    jingping_result=json.loads((get_usetime(home_coordinate,office_coordinate)).decode("utf-8"))

    caofang_result=json.loads((get_usetime(home_coordinate,caofang_subway_coordinate)).decode("utf-8"))

    guomao_result=json.loads((get_usetime(home_coordinate,guomao_subway_coordinate)).decode("utf-8"))

    jingping_car_time,caofang_car_time,guomao_car_time='0','0','0'

    if jingping_result and str(jingping_result.get("status",''))=="0":#开车到三元桥时间
        jingping_car_time=jingping_result.get("result",{}).get("routes",[])[0].get("duration",'0') if jingping_result.get("result",{}).get("routes",[]) else '0'


    if caofang_result and str(caofang_result.get("status",''))=="0":#开车到草房地铁时间
        caofang_car_time=caofang_result.get("result",{}).get("routes",[])[0].get("duration",'0') if caofang_result.get("result",{}).get("routes",[]) else '0'


    if guomao_result and str(guomao_result.get("status",''))=="0":#开车到国贸地铁时间
        guomao_car_time=guomao_result.get("result",{}).get("routes",[])[0].get("duration",'0') if guomao_result.get("result",{}).get("routes",[]) else '0'



    jingping_total_time=float(jingping_car_time)+15*60 #走京平高速从家到办公室的总时间

    caofang_total_time=float(caofang_car_time)+42*60 #经草房地铁从家到办公室的总时间

    guomao_total_time=float(guomao_car_time)+25*60 #经国贸地铁从家到办公室的总时间

    print('--------------%s-------------------%s--------------------%s' % (jingping_total_time, caofang_total_time, guomao_total_time))

    jingping_time=[convert_time(jingping_car_time),convert_time(jingping_total_time)]#格式化显示时间为 xx小时xx分xx秒

    caofang_time = [convert_time(caofang_car_time), convert_time(caofang_total_time)]#格式化显示时间为 xx小时xx分xx秒

    guomao_time = [convert_time(guomao_car_time), convert_time(guomao_total_time)]#格式化显示时间为 xx小时xx分xx秒

    now_datestring=datetime.datetime.now().strftime("%Y-%m-%d %H:%I:%S")

    return {"jingping_time":jingping_time,"caofang_time":caofang_time,"guomao_time":guomao_time,"ttime":now_datestring}


#通过经纬度起点、终点查找路线，默认经过京平高速
def get_usetime(origin,destination,waypoints='40.037369,116.569077'):
    #tactics:7  高速优先  alternatives：1 是否返回备选路线
    # 0：默认
    # 3：不走高速
    # 4：高速优先
    # 5：躲避拥堵
    # 6：少收费
    # 7：躲避拥堵 & 高速优先
    # 8：躲避拥堵 & 不走高速
    # 9：躲避拥堵 & 少收费
    # 10：躲避拥堵 & 不走高速 & 少收费
    # 11：不走高速 & 少收费
    urlstring="http://api.map.baidu.com/direction/v2/driving?origin="+origin+"&destination="+destination+"&ak="+baidu_key+"&tactics=7&output=json&alternatives=0&waypoints="+waypoints
    jsonstring=urllib.request.urlopen(quote(urlstring, safe='/:?=&')).read()
    print('get_usetime=========%s'%quote(urlstring, safe='/:?=&'))
    return jsonstring

#格式化显示时间为 xx小时xx分xx秒
def convert_time(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return ("%02d:%02d:%02d" % (h, m, s))