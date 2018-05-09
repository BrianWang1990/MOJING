import urllib

from mojing.settings import gaode_key

#通过经纬度起点、终点查找路线
def get_usetime(origin,destination):
    urlstring="http://restapi.amap.com/v3/direction/driving? key="+gaode_key+"&origin="+origin+"&destination="+destination+"&originid=&destinationid=&extensions=all&strategy=0&waypoints=&avoidpolygons=&avoidroad="
    jsonstring=urllib.request.urlopen(urlstring).read()
    print('get_usetime=========%s'%jsonstring)
    return jsonstring

#中文地点转经纬度
def address_to_point(address):
    urlstring="http://restapi.amap.com/v3/geocode/geo?address="+address+"&output=json&key="+gaode_key
    print('=================%s'%urlstring)
    jsonstring = urllib.request.urlopen(urlstring).read()
    print('address_to_point=========%s' % jsonstring)
    return jsonstring