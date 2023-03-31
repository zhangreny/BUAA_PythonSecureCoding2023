import requests
      
class Dnslog:
    def __init__(self):
        self.getdnssub_url = 'http://www.dnslog.cn/getdomain.php'	# 获取子域名的url
        self.getres_url = 'http://www.dnslog.cn/getrecords.php'	# 获取记录的url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X ',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Connection': 'close'
        }
        self.s = requests.session()  # 这里定义一个session，同一个session可以拿到之前获取到的子域名的日志

    def req(self):  # 获取请求到的dnslog随机子域名
        try:
            response_getdnsurl = requests.get(url=self.getdnssub_url, headers=self.headers, verify=False)
            dnscode = response_getdnsurl.text
            cookie = response_getdnsurl.cookies
            cookies = requests.utils.dict_from_cookiejar(cookie)
            self.PHPSESSID = cookies['PHPSESSID']
            return dnscode
        except:
            return None

    def res(self):  # 获取dnslog随机子域名的dns查询日志
        try:
            headers_seesion = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Cookie': "PHPSESSID=%s" % self.PHPSESSID}
            response_dns = requests.get(url=self.getres_url, headers=headers_seesion)
            return response_dns.text
        except:
            return None

dnslog = Dnslog()           # 实例化一个DNSLog对象
dns_host = dnslog.req()     # 调用req()方法生成一个子域名

import os
result = os.popen('ping '+dns_host) # 调用系统ping方法去ping子域名
print(result.read())

if dns_host in dnslog.res():    # 调用res()方法获取域名解析记录
    print("子域名",dns_host, "有解析记录")



