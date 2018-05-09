import urllib

from mojing.settings import gaode_key
from urllib.parse import quote
#quote 为了解决url中英文混排的问题

#通过经纬度起点、终点查找路线
def get_usetime(origin,destination):
    urlstring="http://restapi.amap.com/v3/direction/driving?key="+gaode_key+"&origin="+origin+"&destination="+destination+"&originid=&destinationid=&extensions=all&strategy=0&waypoints=&avoidpolygons=&avoidroad="
    jsonstring=urllib.request.urlopen(quote(urlstring, safe='/:?=')).read()
    print('get_usetime=========%s'%jsonstring)
    return jsonstring

#中文地点转经纬度
def address_to_point(address):
    urlstring="http://restapi.amap.com/v3/geocode/geo?address="+address+"&output=json&key="+gaode_key
    jsonstring = urllib.request.urlopen(quote(urlstring, safe='/:?=')).read()
    print('address_to_point=========%s' % jsonstring)
    return jsonstring

