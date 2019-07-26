# import random
#
# import pymysql
#
# class C():
#     def __init__(self):
#         pass
#
#         self.conn = pymysql.connect(
#                 host='192.168.1.11',
#                 port=3306,
#                 user='root',
#                 passwd='Front@2017',
#                 db='auto')
#         self.cursor = self.conn.cursor()
#
#         list_sql = "select ip, port from tb_proxy"
#
#         # names = self.cursor.execute(list_sql)
#         self.cursor.execute(list_sql)
#         names_obj = self.cursor.fetchall()
#         ips = []
#         for i, j in names_obj:
#             ips.append(i + ":" +j)
#             # for ip in ips:
#                 # print(ip)
#         ip = random.choice(ips)
#         print(ip)
#
# C()


import requests


url = "https://r.inews.qq.com/search?chlid=_qqnews_custom_search_all&search_from=&new_user=0&devid=4100bcad78c3b131&qimei=4100bcad78c3b131&uid=4100bcad78c3b131&appver=28_android_5.8.44&trueVersion=5.8.44&omgid=0c1d885f982c8c42d49a3a8ac567b9c1494a0010213a05&Cookie=lskey%3D;skey%3D;uin%3D;%20luin%3D;logintype%3D0;%20main_login%3D;%20&qn-sig=7468c660985029332a8e23e766579f42&qn-rid=16329df8-4a8a-4893-8f2e-8defae4ca25c&search_type=all&query=%E5%88%AB%E5%85%8BGL8&cp_type=0&disable_qc=0&searchStartFrom=header&launchSearchFrom=sug&isDefault=0&searchTag=%E5%88%AB%E5%85%8BGL8&loc_district_name=%E6%99%AE%E9%99%80%E5%8C%BA&loc_street=%E4%B8%AD%E6%B1%9F%E8%B7%AF&loc_catalog=%E6%88%BF%E4%BA%A7%E5%B0%8F%E5%8C%BA%3A%E5%95%86%E5%8A%A1%E6%A5%BC%E5%AE%87&lon=121.392922&loc_streetNo=%E4%B8%AD%E6%B1%9F%E8%B7%AF112%E5%8F%B7&cityId=12&cityList=news_news_sh&loc_city_name=%E4%B8%8A%E6%B5%B7%E5%B8%82&provinceId=12&lastLocatingTime=1564020022&town_name=%E9%95%BF%E9%A3%8E%E6%96%B0%E6%9D%91%E8%A1%97%E9%81%93&loc_name=%E5%8C%97%E5%B2%B8%C2%B7%E9%95%BF%E9%A3%8E&loc_addr=%E4%B8%8A%E6%B5%B7%E5%B8%82%E6%99%AE%E9%99%80%E5%8C%BA%E5%A4%A7%E6%B8%A1%E6%B2%B3%E8%B7%AF168%E5%BC%84&village_name=Unknown&loc_province_name=%E4%B8%8A%E6%B5%B7%E5%B8%82&lat=31.221189&net_proxy=DIRECT&rom_type=MIUI%20V10&top_activity=SplashActivity&currentChannelId=news_news_top&omgbizid=d203d1ef8dcf394e30680bef61d2fa94eb380050214303&mid=c8c17ffc23298a8ac159701509592351ef0a28e8&videoAutoPlay=1&real_device_width=2.68&mac=F4%3A60%3AE2%3A55%3A1B%3AA4&isMainUserLogin=0&hw=Xiaomi_MI8Lite&isoem=0&preStartTimestamp=1562726547&cpuabi=armeabi-v7a&screen_height=2068&is_special_device=0&imsi_history=0%2C460024397311811&origin_imei=869809035092596&global_info=1%7C1%7C1%7C1%7C1%7C13%7C7%7C1%7C0%7C6%7C1%7C1%7C1%7C%7C0%7CJ309P000000000%3AJ902P000000000%3AA601P000079502%3AJ601P500000000%3AJ601P100000000%3AJ601P600000000%3AJ601P400000000%3AJ601P300000000%3AJ601P200000000%3AJ603P000000000%3AJ604P000000000%3AB401P000050902%3AJ401P100000000%3AJ602P000000000%3AJ602P900000000%3AJ304P000000000%3AJ701P000000000%3AJ703P000000000%3AB704P000103003%3AB702P000118502%3AA064P000117303%3AA085P000087701%3AB267P000084602%3AJ267P100000000%3AA060P000084801%3AJ060P400000000%3AJ060P100000000%3AJ060P016000000%3AA403P000115801%3AA403P100109204%3AB055P000109902%3AB055P200076802%3AA402P000118201%3AA402P100113701%3AJ402P013000000%3AJ054P000000000%3AJ054P600000000%3AJ054P200000000%3AA901P000117401%7C1429%7C0%7C1%7C26%7C26%7C0%7C0%7C0%7C10%7C3%7C3%7C1%7C1%7C1%7C1%7C1%7C1%7C-1%7C1%7C2%7C2%7C2%7C0%7C1%7C0%7C0%7C0%7C0%7C1%7C1%7C0%7C1%7C0%7C0%7C0%7C0%7C0%7C1%7C0%7C1%7C1%7C0%7C0%7C1%7C2%7C3%7C0%7C1%7C1%7C11%7C20%7C1%7C0%7C1%7C0%7C0%7C0%7C1%7C4%7C0%7C1%7C1%7C40%7C1%7C52%7C60%7C0%7C0%7C0%7C12%7C0%7C3%7C1%7C1%7C0%7C76%7C0%7C2&net_slot=0&dpi=440.0&pagestartfrom=icon&screen_width=1080&net_ssid=xiaomiwifi&adcode=310107&apptype=android&store=826&net_apn=0&baseid=..6176.9631756&isColdLaunch=1&real_device_height=5.67&islite=0&isElderMode=0&activefrom=icon&global_session_id=1564020017537&origCurrentTab=top&is_chinamobile_oem=0&net_bssid=1c%3Ae6%3Ac7%3A5a%3A6f%3Ac0&qqnetwork=wifi&network_type=wifi&currentTabId=news_news&startTimestamp=1564020017"
hreders = {
    'Cookie': "SID=130102; ASP.NET_SessionId=3h0uwsyalnpe0s55uuqd1g3e; AutoIpLogin=; LID=; FileNameM=cnki%3A",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
    'Referer': 'http://dbpub.cnki.net/grid2008/dbpub/brief.aspx?curpage=3&RecordsPerPage=50&QueryID=4&ID=SCPD&turnpage=1&systemno=&NaviDatabaseName=SCPD_IPCCLS&NaviField=%e4%b8%bb%e5%88%86%e7%b1%bb%e5%8f%b7&navigatorValue=&subBase=fm'
}
res = requests.post(url, "", hreders)
print(res.text)
# SID=130102; ASP.NET_SessionId=3h0uwsyalnpe0s55uuqd1g3e; AutoIpLogin=; LID=; FileNameM=cnki%3A