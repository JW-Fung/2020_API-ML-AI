import pandas as pd
import requests
key_fung="668af4645e21e4a45e2005c5c4c0ba9f"
# # 1.获取地理编码
def geocode(x,address,city=None,batch=None,sig=None):
    url = 'https://restapi.amap.com/v3/geocode/geo?parameters'
    if x>=1:
        params={
            'key': key_fung,
            'address':address,
            'city':city,
            'batch':batch,
            'sig':sig,
            'output':'json'
        }
        response = requests.get(url,params=params)
        data = response.json()
        return data
    else:
        params1={
            'key': key_fung,
            'address':address,
            'city':city,
            'batch':batch,
            'sig':sig,
        }
        response1 = requests.get(url,params=params1)
        codeurl=response1.url
        return codeurl    
# 2.获取逆地理编码
def regeocode(x,location,poitype=None,radius=None,extensions="base",batch=False,roadlevel=None,sig=None,homeorcorp=None)->dict:
    """获取逆地理编码"""
    url = 'https://restapi.amap.com/v3/geocode/regeo?parameters'
    if x>=1:
        params={
            'key': key_fung,
            'location':location,
            'poitype':poitype,#返回附近POI类型,可以返回经纬度附近符合限定要求的POI内容（在 extensions 字段值为 all 时才会返回POI内容），该参数在 batch 取值为 true 时不生效。
            'radius':radius,  #radius取值范围在0~3000，默认是1000。单位：米
            'extensions':extensions,# 返回结果控制,默认取值是 base,取值为 all 时会返回基本地址信息、附近 POI 内容、道路信息以及道路交叉口信息。
            'batch':batch,#参数设置为 true 时进行批量查询操作，最多支持 20 个经纬度点进行批量地址查询操作。设置为 false 时进行单点查询
            'roadlevel':roadlevel,# 道路等级,extensions 参数为 all 时才生效,当roadlevel=0时，显示所有道路,当roadlevel=1时，过滤非主干道路，仅输出主干道路数据 
            'homeorcorp':homeorcorp,#是否优化POI返回顺序,0：不对召回的排序策略进行干扰,1：综合大数据分析将居家相关的 POI 内容优先返回，即优化返回结果中 pois 字段的poi顺序,2：综合大数据分析将公司相关的 POI 内容优先返回，即优化返回结果中 pois 字段的poi顺序。
            'sig':sig,
            'output':'json'# 可选输入内容包括：JSON，XML。设
        }
        response = requests.get(url,params=params)
        data = response.json()
        return data
    else:
        params1={
           'key': key_fung,
        'location':location,
        'poitype':poitype,#返回附近POI类型,可以返回经纬度附近符合限定要求的POI内容（在 extensions 字段值为 all 时才会返回POI内容），该参数在 batch 取值为 true 时不生效。
        'radius':radius,  #radius取值范围在0~3000，默认是1000。单位：米
        'extensions':extensions,# 返回结果控制,默认取值是 base,取值为 all 时会返回基本地址信息、附近 POI 内容、道路信息以及道路交叉口信息。
        'batch':batch,#参数设置为 true 时进行批量查询操作，最多支持 20 个经纬度点进行批量地址查询操作。设置为 false 时进行单点查询
        'roadlevel':roadlevel,# 道路等级,extensions 参数为 all 时才生效,当roadlevel=0时，显示所有道路,当roadlevel=1时，过滤非主干道路，仅输出主干道路数据 
        'homeorcorp':homeorcorp,#是否优化POI返回顺序,0：不对召回的排序策略进行干扰,1：综合大数据分析将居家相关的 POI 内容优先返回，即优化返回结果中 pois 字段的poi顺序,2：综合大数据分析将公司相关的 POI 内容优先返回，即优化返回结果中 pois 字段的poi顺序。
        'sig':sig
        }
        response1 = requests.get(url,params=params1)
        codeurl=response1.url
        return codeurl        
天河城逆地理编码 = regeocode(1,天河城地理编码)
print(天河城逆地理编码)
df_天河城逆地理编码 = pd.json_normalize(天河城逆地理编码).T
display(df_天河城逆地理编码)

# 3.路径规划
# 3.1步行(100KM以内的步行通勤方案)
def walking(x,origin,destination,sig=None)->dict:
    url = 'https://restapi.amap.com/v3/direction/walking?parameters'
    if x>=1:
        params={
            'key':key_fung,
            'origin':origin,# 经纬度
            'destination':destination,# 经纬度
            'output':'json'
        }
        response = requests.get(url,params=params)
        data = response.json()
        return data
    else:
        params1={
            'key':key_fung,
            'origin':origin,# 经纬度
            'destination':destination
                }
        response1 = requests.get(url,params=params1)
        codeurl=response1.url
        return codeurl        
# 3.2 公交路径规划
# D-1 准备base url、params、response.json（） 
def bus (x,origin,destination,city=None,cityd=None,extensions='base',strategy=None,nightflag=0,date=None,time=None,sig=None)->dict:
    url="https://restapi.amap.com/v3/direction/transit/integrated?parameters"
    if x>=1:
        params={
            'key':key_fung,
            'origin':origin,
            'destination':destination,
            'city':city,#必填，起点城市
            'cityd':cityd,#跨城必填，终点城市
            'extensions':extensions,
            'strategy':strategy,#公交换乘策略,可选值：0：最快捷模式,1：最经济模式,2：最少换乘模式.3：最少步行模式.5：不乘地铁模式
            'nightflag':nightflag,
            'date':date,
            'time':time,
            'sig':sig,
            'output':'json'
        }
        respond=requests.get(url,params=params)
        data=respond.json()
        return data
    else:
            params1={
            'key':key_fung,
            'origin':origin,
            'destination':destination,
            'city':city,#必填，起点城市
            'cityd':cityd,#跨城必填，终点城市
            'extensions':extensions,
            'strategy':strategy,#公交换乘策略,可选值：0：最快捷模式,1：最经济模式,2：最少换乘模式.3：最少步行模式.5：不乘地铁模式
            'nightflag':nightflag,
            'date':date,
            'time':time,
            'sig':sig
                    }
            response1 = requests.get(url,params=params1)
            codeurl=response1.url
            return codeurl  
# 3.3驾车路径规划
def drive(origin,destination,strategy=None,extensions='base')->dict:
    url='https://restapi.amap.com/v3/direction/driving?parameters'
    params={
        'KEY':key_fung,
        'origin':origin,
        'destination':destination,
        'strategy':strategy,
        'output':'json',
        'extensions':extensions
    }
    respond=requests.get(url,params)
    data=respond.json()
    return data
#4.搜索POI
#4.1关键字搜索
def key_word (keywords,city,citylimit=None,extensions=None,types=None, page=None)->dict:
    url="https://restapi.amap.com/v3/place/text?parameters"
    params={
        'key':key_fung,
        'keywords':keywords,
        'types':types,# (keywords和types两者至少必选其一)
        'city':city,
        'citylimit':citylimit,
        'extensions':extensions,
        'page':page,
        'output':'json'
            
    }
    respond=requests.get(url,params)
    data=respond.json()
    return data
#4.2周边搜索
def around (location,keywords,city,radius=None,extensions=None,page=None,sortrule='distance')->dict:
    url="https://restapi.amap.com/v3/place/text?parameters"
    params={
        'key':key_fung,
        'keywords':keywords,
        'location':location,# (keywords和types两者至少必选其一)
        'city':city,
        'radius':radius,
        'extensions':extensions,
        'page':page,
        'output':'json',
        'sortrule':sortrule
    }
    respond=requests.get(url,params)
    data=respond.json()
    return data
#4.3多边形搜索
def polygon (polygon,keywords,extensions=None,page=None)->dict:
    url="https://restapi.amap.com/v3/place/polygon?parameters "
    params={
        'key':key_fung,
        'keywords':keywords,
        'polygon':polygon,# (keywords和types两者至少必选其一),
        'extensions':extensions,
        'page':page,
        'output':'json'
    }
    respond=requests.get(url,params)
    data=respond.json()
	return data
	
#4.4ID查询
def ID (id)->dict:
    url="https://restapi.amap.com/v3/place/detail?parameters  "
    params={
        'key':key_fung,
        'id':id,
        'output':'json'
    }
    respond=requests.get(url,params)
    data=respond.json()
    return data
#5.IP定位
def IP (ip,sig=None)->dict:
    url="https://restapi.amap.com/v3/ip?parameters"
    params={
        'key':key_fung,
        'ip':ip,
        'sig':sig,
        'output':'json'
    }
    respond=requests.get(url,params)
    data=respond.json()
    return data
#6.批量请求接口
def 批量请求(url2,url3):
    url='https://restapi.amap.com/v3/batch'
    params={
        'key':key_fung
    }
    data={
    "ops": [
        {
            "url":url2 ,
            
        },
        {
            "url": url3
        }
    ]
}
    header={
        'Content-Type':'application/json'
    }
    respond=requests.get(url,params,json=data)
    datas=respond.json()
    return datas
	#url准备
	geocode_url=geocode(0,'广东省广州市天河城购物中心')
	url5=geocode_url.split('com')
	url6=(url5[1])
	print(url5[1])
#7.静态地图
from PIL import Image
from io import BytesIO 
def maps (x,location,zoom=None,size=None,scale=None,paths=None,labels=None,traffic=None)->dict:
    url="https://restapi.amap.com/v3/staticmap?parameters "
    if x>=1:
        params={
            'key':key_fung,
            'location':location,
            'zoom':zoom,
            'size':size,
            'scale':scale,
            'paths':paths,
            'labels':labels,
            'traffic':traffic,
            'output':'json'
        }
        respond=requests.get(url,params)
        data=Image.open(BytesIO(respond.content)) #打开照片的数据——bytesio
        return data
    else:
            params1={
            'key':key_fung,
            'location':location,
            'zoom':zoom,
            'size':size,
            'scale':scale,
            'paths':paths,
            'labels':labels,
            'traffic':traffic
            }
            response1 = requests.get(url,params=params1)
            codeurl=response1.url
            return codeurl
#8.坐标转换
def convert (location,coordsys=None)->dict:
    url="https://restapi.amap.com/v3/assistant/coordinate/convert?parameters "
    params={
        'key':key_fung,
        'locations':location,
        'coordsys':coordsys,
        'output':'json'
    }
    respond=requests.get(url,params)
    data=respond.json()
    return data
#9.交通态势
#9.1 矩形交通姿态
def status_rectangle (rectangle,level=None,extensions=None)->dict:
    url="https://restapi.amap.com/v3/traffic/status/rectangle?parameters"
    params={
        'key':key_fung,
        'level':level,
        'extensions':extensions,
        'rectangle':rectangle,
        'output':'json'
    }
    respond=requests.get(url,params)
    data=respond.json()
    return data
# 9.2圆形交通姿态
def status_circle (location,level=None,extensions=None,radius=None)->dict:
    url="https://restapi.amap.com/v3/traffic/status/circle?parameters"
    params={
        'key':key_fung,
        'level':level,
        'extensions':extensions,
        'location':location,
        'radius':radius,
        'output':'json'
    }
    respond=requests.get(url,params)
    data=respond.json()
    return data
# 10.行政区域查询
def district (keywords,subdistrict=None,extensions=None)->dict:
    url="https://restapi.amap.com/v3/config/district?parameters"
    params={
        'key':key_fung,
        'keywords':keywords,
        'extensions':extensions,
        'subdistrict':subdistrict,
        'output':'json'
    }
    respond=requests.get(url,params)
    data=respond.json()
    return data
#11.天气查询
def weather (city,extensions=None)->dict:
    url="https://restapi.amap.com/v3/weather/weatherInfo?parameters"
    params={
        'key':key_fung,
        'city':city,
        'extensions':extensions,
        'output':'json'
    }
    respond=requests.get(url,params)
    data=respond.json()
    return data
#12.输入提示
def inputtips (keywords,type1=None,city=None,datatype=None)->dict:
    url="https://restapi.amap.com/v3/assistant/inputtips?parameters"
    params={
        'key':key_fung,
        'keywords':keywords,
        'type':type1,
        'city':city,
        'datatype':datatype,
        'output':'json'
    }
    respond=requests.get(url,params)
    data=respond.json()
    return data
#13.地理围栏
# 创建围栏
def creat (name,center=None,radius=None,enable=None,valid_time=None,repeat=None,time=None,desc=None,alert_condition=None)->dict:
    url="https://restapi.amap.com/v4/geofence/meta"
    params={
        'key':key_fung
    }
    body={
        'name':name,
        'center':center,
        'radius':radius,
        'enable':enable,
        'valid_time ':valid_time,
        'repeat':repeat,
        'time':time,
        'desc':desc,
        'alert_condition':alert_condition
    }
    respnod=requests.post(url,params=params,json=body)
    data=respnod.json()
    return data
#查询围栏
def search (id1=None,gid=None,name=None)->dict:
    url="https://restapi.amap.com/v4/geofence/meta"
    params={
        'key':key_fung,
        'id':id1,
        'gid':gid,
        'name':name
    }
    respond=requests.get(url,params)
    data=respond.json()
    return data
#更新围栏
def renew (name,gid,center=None,radius=None,enable=None,valid_time=None,repeat=None,time=None,desc=None,alert_condition=None)->dict:
    url="https://restapi.amap.com/v4/geofence/meta"
    params={
        'key':key_fung,
        'gid':gid
    }
    body={
        'name':name,
        'center':center,
        'radius':radius,
        'enable':enable,
        'valid_time ':valid_time,
        'repeat':repeat,
        'time':time,
        'desc':desc,
        'alert_condition':alert_condition
    }
    respnod=requests.post(url,params=params,json=body)
    data=respnod.json()
    return data
#围栏启动&停止
def star_stop (name,gid,enable)->dict:
    url="https://restapi.amap.com/v4/geofence/meta"
    params={
        'key':key_fung,
        'gid':gid,
        'name':name
    }
    body={
        'enable':enable,
    }
    respnod=requests.post(url,params=params,json=body)
    data=respnod.json()
    return data
#删除围栏
def delete (gid)->dict:
    url="https://restapi.amap.com/v4/geofence/meta"
    params={
        'key':key_fung,
        'gid':gid,
    }
    respond=requests.post(url,params)
    data=respond.json()
    return data
#监控
def status (diu,location)->dict:
    url="https://restapi.amap.com/v4/geofence/status"
    params={
        'key':key_fung,
        'diu':diu,
        'locations':locations
    }
    respnod=requests.get(url,params=params)
    data=respnod.json()
    return data
#14.轨迹纠偏
