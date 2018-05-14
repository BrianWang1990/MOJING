import urllib

from mojing.settings import gaode_key,weather_key
from urllib.parse import quote
#quote 为了解决url中英文混排的问题

#通过经纬度起点、终点查找路线
def get_usetime(origin,destination):
    #strategy:19  高速优先
    urlstring="http://restapi.amap.com/v3/direction/driving?key="+gaode_key+"&origin="+origin+"&destination="+destination+"&originid=&destinationid=&extensions=all&strategy=19&waypoints=116.623062,40.022059,&avoidpolygons=&avoidroad="
    jsonstring=urllib.request.urlopen(quote(urlstring, safe='/:?=&')).read()
    print('get_usetime=========%s'%quote(urlstring, safe='/:?=&'))
    return jsonstring

#中文地点转经纬度
def address_to_point(address,city):
    urlstring="http://restapi.amap.com/v3/geocode/geo?address="+address+"&city="+city+"&output=json&key="+gaode_key
    jsonstring = urllib.request.urlopen(quote(urlstring, safe='/:?=&')).read()
    # print('address_to_point=========%s' % quote(urlstring, safe='/:?=&'))
    return jsonstring

#获取天气
def get_weather(city):
    urlstring="http://api.jisuapi.com/weather/query?appkey="+weather_key+"&city="+city
    jsonstring=urllib.request.urlopen(quote(urlstring,safe='/:?&')).read()
    return jsonstring

