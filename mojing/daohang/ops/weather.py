#获取天气
import urllib
from quopri import quote

from mojing.settings import weather_key


def get_weather(city):
    urlstring="http://api.jisuapi.com/weather/query?appkey="+weather_key+"&city="+city
    jsonstring=urllib.request.urlopen(quote(urlstring,safe='/:?&')).read()
    return jsonstring