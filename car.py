import datetime
import time

import pymysql
import requests
import re
from bs4 import BeautifulSoup
from fontTools.ttLib import TTFont
import json
import random
from lxml import etree
import urllib3
from selenium import webdriver


driver = webdriver.Chrome('C:\WebDriver\chromedriver.exe')
urllib3.disable_warnings()
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
            'Cookie': '__ah_uuid=00EC9C6F-E7DA-4790-B743-D134EC8DA6C9; fvlid=1552967337042GM8fz3VIUE; sessionid=1CBA2A06-3AA9-4735-8C71-77A1AE9B7737%7C%7C2019-03-19+11%3A48%3A59.137%7C%7Cwww.baidu.com; sessionuid=1CBA2A06-3AA9-4735-8C71-77A1AE9B7737%7C%7C2019-03-19+11%3A48%3A59.137%7C%7Cwww.baidu.com; jrsfvi=1553237676009ARoKiPGhUXvQ%7Cwww.baidu.com%7C0; autoid=e146573a4c02713f2d4e2210661c8784; mallsfvi=1559294057250XiW9CkqR%7Cwww.autohome.com.cn%7C3311247; sessionfid=3442351364; ahpau=1; ahsids=2073_162_703_2838_4175_172; __ah_uuid_ng=u_66862417; area=310107; __utma=1.1117292856.1561534804.1561534804.1563526150.2; __utmc=1; __utmz=1.1563526150.2.2.utmcsr=club.autohome.com.cn|utmccn=(referral)|utmcmd=referral|utmcct=/bbs/thread/86817b554ed481a5/82236481-1.html; historybbsName4=c-3751%7C%E5%A8%81%E6%9C%97%2Cc-164%7C%E5%90%9B%E5%A8%81%2Cc-834%7C%E5%90%9B%E8%B6%8A%2Cc-4487%7C%E5%88%AB%E5%85%8BGL6%2Cc-442%7C%E9%80%9F%E8%85%BE%2Cc-4776%7CVELITE%206%2Cc-448%7C%E8%BD%A9%E9%80%B8%2Cc-4274%7C%E9%80%94%E8%A7%82%2F%E9%80%94%E8%A7%82L%2Cc-526%7C%E5%8D%A1%E7%BD%97%E6%8B%89%2Cc-614%7C%E6%9C%97%E9%80%B8; sessionip=58.34.170.53; Hm_lvt_9924a05a5a75caf05dbbfb51af638b07=1562049789,1563788884; Hm_lpvt_9924a05a5a75caf05dbbfb51af638b07=1563788899; pbcpopclub=c5f091f0-0372-4122-ae12-6cd0b598507b; sessionvid=D68E4C04-D59D-41C3-8120-628F85DC8338; ahpvno=128; pvidchain=28086821202,28086821202,3311278,3311278,3311278; ref=www.baidu.com%7C0%7C0%7C0%7C2019-07-24+11%3A28%3A28.685%7C2019-03-19+11%3A48%3A59.137',
            'Referer': 'https://club.autohome.com.cn/bbs/forum-c-526-1.html',
            # 'Connection': 'keep-alive'
        }


class crawl():
    def __init__(self):
        self.sess = requests.session()

    def get_html(self, url):
        """
        获得目标网页数据
        :param url:
        :return:
        """
        proxy = {"https://": ip}
        try:
            # r = self.sess.get(url, headers=headers, proxies=proxy, verify=False)
            r = requests.get(url, headers=headers, proxies=proxy, verify=False)
            # if r.status_code != 200 in r.text:
            if "需要您协助验证" in r.text:
                # self.yan_zheng_ma(url)
                print("验证码页面！！！！！！！！！")
                driver.get(url)
                time.sleep(2)
                try:
                    driver.find_element_by_xpath('//*[@id="embed-captcha"]/div/div[2]/div[1]/div[3]').click()
                except:
                    pass
                time.sleep(5)
                # TODO: "验证码判定"
                # time.sleep(3)
                r = self.sess.get(url, headers=headers, proxies=proxy, verify=False)
                if "需要您协助验证" in r.text:
                    self.get_html(url)
                else:
                    return r.content
            else:
                return r.content
        except Exception as e:
            print('抓取失败', e)
            return None

    # 解析字体，
    def decode_font(self, font_parse_name):
        """
        解析字体对应关系
        :param font_parse_name:
        :return:
        """
        # 设置编码和文字的关系
        font_dict = [u'五', u'四', u'短', u'十',
                     u'坏', u'近', u'大', u'九', u'小',
                     u'矮', u'上', u'一', u'六', u'的',
                     u'呢', u'长', u'少', u'下', u'地',
                     u'右', u'好', u'更', u'远', u'二',
                     u'和', u'低', u'七', u'很', u'着',
                     u'高', u'了', u'是', u'得', u'不',
                     u'左', u'八', u'三', u'多']

        font_base = TTFont('font_base.ttf')
        # font_1.saveXML('font_base.xml')
        font_base_order = font_base.getGlyphOrder()[1:]    # 原始font_base 编码

        font_parse = TTFont(font_parse_name)   # 解析新得到的网页字体
        # font_parse.saveXML('font_parse_2.xml')  # 调试用
        font_parse_order = font_parse.getGlyphOrder()[1:]   # 解析新得到的网页字体编码

        f_base_flag = []
        for i in font_base_order:
            flags = font_base['glyf'][i].flags   # 获取0、1值
            f_base_flag.append(list(flags))

        f_flag = []
        for i in font_parse_order:
            flags = font_parse['glyf'][i].flags
            f_flag.append(list(flags))
        # print(f_flag)

        result_dict = {}
        for a, i in enumerate(f_base_flag):  # 遍历本地字体0、1（flags）值列表
            for b, j in enumerate(f_flag):   # 遍历网络字体0、1值（flags）列表
                # print(b, j)
                if self.comp(i, j):   # 逐一对比本地与网络字体（根据0、1值）
                    # print(b, font_parse_order)
                    key = font_parse_order[b].replace('uni', '')
                    key = eval(r'u"\u' + str(key) + '"').lower()
                    # print(result_dict[key], font_dict[a])
                    result_dict[key] = font_dict[a]   # 对网络字体赋予对应的本地字体值
                    # font_dict[a]：第a个本地字体
                    # result_dict[key]：与font_dict[a]（本地字体）对应的网络字体
        return result_dict

    def comp(self, L1, L2):
        """
        比较字体是否为同一字体替换
        :param L1: 本地字体
        :param L2: 网络加密字体
        :return:
        """
        if len(L1) != len(L2):
            return 0
        for i in range(len(L2)):
            if L1[i] == L2[i]:
                pass
            else:
                return 0
        return 1

    # 解析网页
    def parse_html(self, html):
        """
        替换正常字体（字体映射）
        :param html:
        :return: 需要的正常数据
        """
        soup = BeautifulSoup(html, 'lxml')

        # font_url = soup.find('style', attrs={'type': 'text/css'}).text
        # font_url = 'https:' + re.search(",url\('(//.*.ttf)'\) format\('woff'\)", font_url, re.S).group(1)
        try:
            # font_url = 'https:' + re.search(r"\,url\('(.*\.ttf)'\)", font_url, re.S).group(1)
            font_url = 'https:' + re.search(r"\,url\('(.*\.ttf)'\)", soup.text, re.S).group(1)
        except:
            print("===================>", "出错了！")
            return
        # print(font_url)
        new_font_name = "font_new.ttf"

        font_data = self.get_html(font_url)
        with open(new_font_name, 'wb') as f:  # 获得字体文件
            f.write(font_data)

        map_data = self.decode_font(new_font_name)   # 得到字体映射
        # print("!!!", map_data)
        # conttxt = soup.find(class_='conttxt').text              #####
        # # conttxt = soup.find(class_='conttxt').get_text()          #
        # print(conttxt)                                              # 获取内容文本
        # # 去掉html标签                                              #
        # text_data = re.sub(r'<.*?>', '', conttxt).strip()           #
        # text_data = re.sub(r'\s+', '', text_data).strip()           #
        # print(conttxt)                                          #####

        finall_res = etree.HTML(html)
        content_first = finall_res.xpath(
            "//div[@id='F0']/div/div[@class='rconten']/div[@class='conttxt']/div/div//text()")
        replies = ""
        # for j in range(1, 21):
        #     # try:
        #     reply = "".join(finall_res.xpath(
        #         "//div[@id='F" + str(j) + "']/div/div/div[@class='x-reply font14']/div//text()")).strip()
        #     replies.join(reply)
        # print(replies)
        text_data = "".join(content_first)
        # text_data = replies

        if text_data:
            for j in map_data.keys():
                # print(j)
                text_data = text_data.replace(j, map_data[j])
            # print('actually data', text_data)
            return text_data

    def yan_zheng_ma(self, url):
        """
        验证码处理
        :param url:
        :return:
        """
        print("验证码页面！！！！！！！！！")
        driver.get(url)
        try:
            driver.find_element_by_xpath('//*[@id="embed-captcha"]/div/div[2]/div[1]/div[3]').click()
        except:
            pass
        time.sleep(6)
        # TODO: "验证码判定"
        proxy = {"https://": ip}
        r = self.sess.get(url, headers=headers, proxies=proxy, verify=False)
        # return r.content
        if "需要您协助验证" in r.text:
            return self.yan_zheng_ma(url)
        else:
            return r.content

    def get_proxy(self):
        """
        获取ip池（数据库）ip
        :return: ips（ip：port）列表
        """
        list_sql = "select ip, port from tb_proxy"
        cursor.execute(list_sql)
        names_obj = cursor.fetchall()
        ips = []
        for i, j in names_obj:
            ips.append(i + ":" + j)
        print(ips)
        return ips

    def con_mysql(self):
        """
        链接数据库
        :return:
        """
        self.conn = pymysql.connect(
            host='192.168.1.11',
            port=3306,
            user='root',
            passwd='Front@2017',
            db='auto')
        self.cursor = self.conn.cursor()
        return self.cursor, self.conn


if __name__ == "__main__":

    cursor, conn = crawl().con_mysql()
    ip = random.choice(crawl().get_proxy())
    names = ["Velite6"]
    ssids = [4776]
    # names = ["轩逸"]
    # ssids = [448]
    # names = ["君越", "君威", "威朗", "英朗", "阅朗", "凯越", "昂科拉", "昂科威", "GL8", "GL6", "Velite6"]
    # ssids = [834, 164, 3751, 982, 4552, 875, 2896, 3554, 166, 4487, 4776]

    aim = dict(zip(names, ssids))
    for name in names:
        key_word = name
        ssid = aim[name]
        for page in range(1, 11):
            start_url = "https://club.autohome.com.cn/frontapi/topics/getByBbsId?pageindex={}&pagesize=50&bbs=c&bbsid={}&orderby=topicid-&fields=topicid%2Ctitle%2Cpost_memberid%2Cpost_membername%2Cpostdate%2Cispoll%2Cispic%2Cisrefine%2Creplycount%2Cviewcount%2Cvideoid%2Cisvideo%2Cvideoinfo%2Cqainfo%2Ctags%2Ctopictype%2Cimgs%2Cjximgs%2Curl%2Cpiccount%2Cisjingxuan%2Cissolve%2Cliveid%2Clivecover%2Ctopicimgs"
            url = start_url.format(page, ssid)
            proxy = {"https://": ip}
            response = requests.get(url, proxies=proxy, headers=headers, verify=False)
            res = json.loads(response.text)
            lists = res['result']['list']
            for i in lists:
                # print(i)
                title = i['title']
                url = i['url']
                sign_time = i['postdate']
                author = i['post_membername']
                reply_num = i['replycount']
                view_num = i['viewcount']
                source = '汽车之家'
                add_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                spider = crawl()
                html = spider.get_html(url)
                # html = "".join(replies)
                text_data = spider.parse_html(html)

                values = [title, url, author, text_data, sign_time, add_time, source, key_word, reply_num, view_num]
                print(values)
                sql = "insert into sp_news(title, url, author, content, issuetime, addtime, source, key_word, reply_num, view_num) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, values)
            conn.commit()
