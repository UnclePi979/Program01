import requests
from bs4 import BeautifulSoup
import re
import json
from tqdm import tqdm
class CoronaVirusSpider(object):

    def __init__(self):
        self.home_url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'

    def get_content_from_url(self, url):
        """"
        根据url，获取响应的字符串数据
        :param url: 请求的URL
        :return: 响应内容的字符串
        """
        response = requests.get(url)
        return response.content.decode()


    def parse_home_page(self, home_page, tag_id):
        """
        解析首页内容，获取解析后的Python数据
        :param home_page: 首页的内容
        :return: 解析后的Python数据
        """
        # 2.从疫情首页，提取最近一日各国数据
        soup = BeautifulSoup(home_page, 'lxml')
        script = soup.find(id=tag_id)
        text = script.string
        # print(text)

        # 3.从疫情数据中，获取json格式的字符串
        json_str = re.findall(r'\[.+\]', text)[0]
        # print(json_str)

        # 4.把json格式的字符串转化为Python类型
        data = json.loads(json_str)
        return data

    def save(self, data, path):
        # 5.以json格式保存最近一日各国疫情数据
        with open(path, 'w', encoding='utf8') as fp:
            json.dump(data, fp, ensure_ascii=False)

    def crawl_last_day_corona_virus(self):
        """
        采集最近一天的各国疫情信息
        :return:
        """
        # 1.发送请求，获取首页内容
        home_page = self.get_content_from_url(self.home_url)
        # 2.解析首页内容,获取最近一天的各国疫情数据
        last_day_corona_virus = self.parse_home_page(home_page, tag_id='getListByCountryTypeService2true')
        # 3.保存数据
        self.save(last_day_corona_virus,'data/last_day_corona_virus.json')

    def crawl_corona_virus(self):
        """
        采集从1月23号以来各国疫情数据
        :return:
        """
        # 1.加载各国疫情数据

        last_day_corona_virus = self.load('data/last_day_corona_virus.json')
        # print(last_day_corona_virus)
        # 定义列表，用于存储各国从1月23日以来的疫情数据
        corona_virus = self.parse_corona_virus(last_day_corona_virus, '采集1月23日以来各国疫情信息')
            # 5.保存列表的数据以JSON格式保存为文件
        self.save(corona_virus, 'data/corona_virus.json')

    def craw_last_day_corona_virus_of_china(self):
        """
        采集最近一日各省疫情数据
        :return:
        """
        # 一.发送请求获取疫情首页
        home_page = self.get_content_from_url(self.home_url)
        # 二.解析疫情首页，获取最近一日各省疫情数据
        data = self.parse_home_page(home_page, tag_id='getAreaStat') # 与以往的代码不同，增加了parse_home_page函数的一个tag_id参数，直接调用该函数即可。
        # 三.保存疫情数据
        self.save(data, 'data/last_day_corona_virus_of_china.json')

    def craw_corona_virus_of_china(self):
        """
        采集1月22日以来全国各省的疫情数据
        :return:
        """
        # 加载最近一日全国疫情信息
        last_day_corona_virus_of_china = self.load('data/last_day_corona_virus_of_china.json')

        # 遍历最近一日全国疫情信息,获取各省疫情URL
        corona_virus = self.parse_corona_virus(last_day_corona_virus_of_china, '采集1月22日以来各省疫情信息')

        # 以json格式保存疫情信息
        self.save(corona_virus, 'data/corona_virus_of_china.json')

    def parse_corona_virus(self, last_day_corona_virus_of_china, desc):
        # 定义列表，用于存储各省从1月22日以来的疫情数据
        corona_virus = []
        # 2.遍历各国疫情数据
        for country in tqdm(last_day_corona_virus_of_china, desc):
            # 发送请求,获取各省疫情json字符串
            statistics_data_url = country['statisticsData']
            statistics_data_json_str = self.get_content_from_url(statistics_data_url)
            # 4.解析各省疫情json字符串，并添加列表中
            statistics_data = json.loads(statistics_data_json_str)['data']
            # print(statistics_data)
            for one_day in statistics_data:
                one_day['provinceName'] = country['provinceName']
                if country.get('countryShortCode'):
                    one_day['countryShortCode'] = country['countryShortCode']
                # print(statistics_data)
            corona_virus.extend(statistics_data)  # 将元素放到列表里去
            # print(corona_virus)
        return corona_virus

    def load(self, path):    #重构load方法
        """
        根据路径加载数据
        :param path:
        """
        with open(path, encoding='utf8') as fp:
            data = json.load(fp)
        return data

    def run(self):
        self.craw_corona_virus_of_china()
        # self.crawl_last_day_corona_virus()
        self.crawl_corona_virus()
        # self.craw_last_day_corona_virus_of_china()

if __name__ == '__main__':
    spider = CoronaVirusSpider()
    spider.run()