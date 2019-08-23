# -*- coding: utf-8 -*-
import scrapy
import re
import json
from lianjia_beijing.items import LianjiaBeijingItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
from scrapy.utils.url import urljoin_rfc
from scrapy.http import Request
#from datacrawler.items import bbsItem
from lianjia_beijing.items import zuFangItem
from lianjia_beijing.items import chengJiaoItem

class LianjiaSpider(Spider):
    name = 'bj_ershoufang'
    #allowed_domains = ['https://bj.lianjia.com/ershoufang/']
    url_list = []

    for i in range(1,101):
        url = "https://bj.lianjia.com/ershoufang/pg{}/".format(str(i))
        url_list.append(url)


    start_urls = url_list
    
    # rules = {
    #         #房产详情链接
    #         Rule(LinkExtractor(restrict_xpaths='//div[@class="info clear"]/div[@class="title"]'), follow=True, callback="parse_Item"),
    #         }
    def pross_Item(self, response):
        #print(response.url)
        #print("正在执行parseItem函数")
        item = LianjiaBeijingItem()
        item['title'] = response.xpath("/html/body/div[3]/div/div/div[1]/h1/text()").extract()[0]
        item['full_desp'] = response.xpath("/html/body/div[3]/div/div/div[1]/div/text()").extract()[0]
        item['price'] = response.xpath("/html/body/div[5]/div[2]/div[4]/span[1]/text()").extract()[0]
        item ['unit_price'] = response.xpath("/html/body/div[5]/div[2]/div[4]/div[1]/div[1]/span/text()").extract()[0]
        item['community_name'] = response.xpath("/html/body/div[5]/div[2]/div[6]/div[1]/a[1]/text()").extract()[0]
        region_big  = response.xpath("/html/body/div[5]/div[2]/div[6]/div[2]/span[2]/a[1]/text()").extract()[0]
        region_small = response.xpath("/html/body/div[5]/div[2]/div[6]/div[2]/span[2]/a[2]/text()").extract()[0]
        item['region'] = region_big+'/'+region_small
        #item['linkman'] = response.xpath("/html/body/div[5]/div[2]/div[7]/div/div[1]/a").extract)()[0]
        #item['linktel'] = response.xpath("")
        item['house_type'] = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[1]/text()').extract()[0]
        item['construction_area'] = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[3]/text()').extract()[0]
        item['actual_area'] = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[5]/text()').extract()[0]
        item['orientation'] = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[7]/text()').extract()[0]
        item['decoration'] = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[9]/text()').extract()[0]
        item['floor'] = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[2]/text()').extract()[0]
        item['elevator'] = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[12]/text()').extract()[0]
        item['property_limit'] = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[13]/text()').extract()[0]
        item['house_year'] = response.xpath('//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[5]/span[2]/text()').extract()[0]
        s = response.xpath('//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[7]/span[2]/text()').extract()[0]
        item['mortgage'] = re.findall(r"[\u4e00-\u9f5a]+",s)[0]
        item['purpose'] = response.xpath('//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[4]/span[2]/text()').extract()[0]
        item['release_date'] = response.xpath('//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[1]/span[2]/text()').extract()[0]
        item['last_date'] = response.xpath('//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[3]/span[2]/text()').extract()[0]
        item['warm'] = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[11]/text()').extract()[0]        
        #print(item)
        yield item

    def parse(self, response):
        #print("正在执行parse函数")
        alinkLists = response.xpath('//div[@class="info clear"]/div[@class="title"]/a/@href').extract()
        #print(alinkLists)
        for alinkList in alinkLists:
            print(alinkList)
            yield Request(url=alinkList, callback=self.pross_Item)

class ZuFangSpider(Spider):
    name = 'bj_zufang'
    #allowed_domains = ['https://bj.lianjia.com/ershoufang/']
    url_list = []

    for i in range(1,101):
        url = "https://bj.lianjia.com/zufang/pg{}/#contentList".format(str(i))
        url_list.append(url)


    start_urls = url_list
    
    # rules = {
    #         #房产详情链接
    #         Rule(LinkExtractor(restrict_xpaths='//div[@class="info clear"]/div[@class="title"]'), follow=True, callback="parse_Item"),
    #         }
    def pross_Item(self, response):
        item = zuFangItem()

        item['title'] = response.xpath("/html/body/div[3]/div[1]/div[3]/p/text()").extract()[0]
        item['way'] = response.xpath('//*[@id="aside"]/ul[1]/p/span[1]/text()').extract()[0]
        item['house_type'] = response.xpath('//*[@id="aside"]/ul[1]/p/span[2]/text()').extract()[0]
        item['area'] = response.xpath('//*[@id="aside"]/ul[1]/p/span[3]/text()').extract()[0]
        item['orientation'] = response.xpath('//*[@id="aside"]/ul[1]/p/span[4]/text()').extract()[0]
        item['price'] = response.xpath('//*[@id="aside"]/p[1]/span/text()').extract()[0]
        item['pay'] = response.xpath('//*[@id="aside"]/p[1]/text()').extract()[0]

        region_big = list(response.xpath('/html/body/div[3]/div[1]/div[7]/p[1]/a[2]/text()').extract()[0])
        region_small = list(response.xpath('/html/body/div[3]/div[1]/div[7]/p[1]/a[3]/text()').extract()[0])
        item['region'] = "".join(region_big[:len(region_big)-2]) +"/"+"".join(region_small[:len(region_small)-2])
        desc_list = response.xpath('//*[@id="aside"]/p[2]/i/text()').extract()
        item['desp'] = ' '.join(desc_list)
        item['release_date'] = response.xpath('/html/body/div[3]/div[1]/div[3]/div[2]/div[2]/ul/li[2]/text()').extract()[0]
        item['lease'] = response.xpath('/html/body/div[3]/div[1]/div[3]/div[2]/div[2]/ul/li[5]/text()').extract()[0]
        item['floor'] = response.xpath('/html/body/div[3]/div[1]/div[3]/div[2]/div[2]/ul/li[8]/text()').extract()[0]
        item['elc_usage'] = response.xpath('/html/body/div[3]/div[1]/div[3]/div[2]/div[2]/ul/li[14]/text()').extract()[0]
        item['moveIn'] = response.xpath('/html/body/div[3]/div[1]/div[3]/div[2]/div[2]/ul/li[3]/text()').extract()[0]
        item['elevator'] = response.xpath('/html/body/div[3]/div[1]/div[3]/div[2]/div[2]/ul/li[9]/text()').extract()[0]
        item['water_usage'] = response.xpath('/html/body/div[3]/div[1]/div[3]/div[2]/div[2]/ul/li[12]/text()').extract()[0]
        item['gas'] = response.xpath('/html/body/div[3]/div[1]/div[3]/div[2]/div[2]/ul/li[15]/text()').extract()[0]
        facility_lists =  response.xpath("/html/body/div[3]/div[1]/div[3]/div[2]/ul/li/@class").extract()[1:]
        facility_list = []
        for facilities in facility_lists:
            facility = facilities.split()[2]
            facility_list.append(facility)
        
        item['facility'] = " ".join(facility_list)
        #print(item)
        yield item

    def parse(self, response):
        #print("正在执行parse函数")
        alinkLists = response.xpath('//div[@class="content__list--item--main"]/p[@class="content__list--item--title twoline"]/a/@href').extract()
        #print(alinkLists)
        #https://bj.lianjia.com
        for alinkList in alinkLists:
            alinkList = "https://bj.lianjia.com"+alinkList
            yield Request(url=alinkList, callback=self.pross_Item)


class chengJiaoSpider(Spider):
    name = 'bj_chengjiao'
    allowed_domains = ['bj.lianjia.com']
    regions = {'dongcheng':'东城',
               'xicheng':'西城',
               'chaoyang':'朝阳',
               'haidian':'海淀',
               'fengtai':'丰台',
               'shijingshan':'石景山',
               'tongzhou':'通州',
               'changping':'昌平',
               'daxing':'大兴',
               'yizhuangkaifaqu':'亦庄开发区',
               'shunyi':'顺义',
               'fangshan':'房山',
               'mentougou':'门头沟',
               'pinggu':'平谷',
               'huairou':'怀柔',
               'miyun':'密云',
               'yanqing':'延庆'

    }
    cnt = 0

    def start_requests(self):
        for region in list(self.regions.keys()):
            url = "https://bj.lianjia.com/xiaoqu/"+region+"/"
            yield Request(url=url, callback = self.parse, meta={'region':region})

    def parse(self, response):
        region = response.meta['region']
        sel = response.xpath("//div[@class='page-box house-lst-page-box']/@page-data").extract()[0]
        sel = json.loads(sel)
        total_pages = sel.get("totalPage")

        for i in range(1, int(total_pages)+1):
        #for i in range(1, 3):
            url_page = "https://bj.lianjia.com/xiaoqu/{}/pg{}/".format(region, str(i + 1))
            yield Request(url=url_page, callback=self.parse_xiaoqu, meta={'region':region})
    
    def parse_xiaoqu(self,response):
        region = response.meta['region']
        xiao_qu_id_lists = response.xpath('//ul[@class="listContent"]/li/@data-id').extract()
        
        for xiao_qu_id in xiao_qu_id_lists:
            url_xiaoqu_full = "https://bj.lianjia.com/chengjiao/c{}/".format(xiao_qu_id)
            yield Request(url=url_xiaoqu_full, callback=self.parse_xiaoqu_full,meta={'region':region,'xiaoqu_id':xiao_qu_id})

    def parse_xiaoqu_full(self,response):
        region = response.meta['region']
        xiaoqu_id = response.meta['xiaoqu_id']
        pages = response.xpath("//div[@class='page-box house-lst-page-box']/@page-data").extract()
        if len(pages) == 0:
            pass
        else:
            sel = pages[0]
            sel = json.loads(sel)
            total_pages = sel.get("totalPage")

            for i in range(1,int(total_pages)+1):
            #for i in range(1,2):
                url_chengjiao_xiaoqu = "https://bj.lianjia.com/chengjiao/pg{}c{}/".format(i,xiaoqu_id)
                yield Request(url=url_chengjiao_xiaoqu, callback=self.parse_chengjiao_xiaoqu,meta={'region':region,'xiaoqu_id':xiaoqu_id})

    def parse_chengjiao_xiaoqu(self,response):
        xiaoqu_id = response.meta['xiaoqu_id']
        url_chengjiao_item_list =  response.xpath('//ul[@class="listContent"]/li/a/@href').extract()
        for url_chengjiao_item in url_chengjiao_item_list:
            yield Request(url = url_chengjiao_item, callback=self.parse_chengjiao_Item, meta={'xiaoqu_id':xiaoqu_id})

    def parse_chengjiao_Item(self, response):
        self.cnt +=1
        print(self.cnt)
        item = chengJiaoItem()
        item['url'] = response.request.url
        item['id'] = response.xpath('//*[@id="introduction"]/div[1]/div[2]/div[2]/ul/li[1]/text()').extract()[0].rstrip()
        title =  response.xpath('/html/body/div[4]/div/text()').extract()[0].split()
        item['community'] = title[0]
        item['community_id'] = response.meta['xiaoqu_id']
        item['trade_time'] = response.xpath('/html/body/div[4]/div/span/text()').extract()[0][:-3]
        item['house_type'] = response.xpath('//*[@id="introduction"]/div[1]/div[1]/div[2]/ul/li[1]/text()').extract()[0].rsplit()
        item['area'] =  response.xpath('//*[@id="introduction"]/div[1]/div[1]/div[2]/ul/li[3]/text()').extract()[0].rsplit() 
        item['big_district'] = response.xpath('/html/body/section[2]/div[2]/div/div/div[1]/a[1]/text()').extract()[0]
        item['small_district'] = response.xpath('/html/body/section[2]/div[2]/div/div/div[1]/a[2]/text()').extract()[0]
        info_fr = response.xpath('//div[@class="info fr"]/div').extract()
        if len(info_fr) == 4:
            item['price'] = response.xpath('/html/body/section[1]/div[2]/div[2]/div[1]/span/i/text()').extract()[0]
            item['price_unit'] = response.xpath('/html/body/section[1]/div[2]/div[2]/div[1]/b/text()').extract()[0]
            item['followers'] = response.xpath('/html/body/section[1]/div[2]/div[2]/div[3]/span[5]/label/text()').extract()[0]
        else:
            item['price']='na'
            item['price_unit']='na'
            item['followers']='na'
        
        teSe =  response.xpath('//*[@id="house_feature"]/div/div/div[2]/a/text()').extract()
        # if len(teSe) >= 2:
        #     item['subway']=1
        #     item['five_years']=1
        # elif len(teSe) == 1:
        #     if teSe[0] == '地铁':
        #         item['subway']=1
        #         item['five_years']=0
        #     else:
        #         item['subway']=0
        #         item['five_years']=1
        # else:
        #     item['subway']=0
        #     item['five_years']=0
        if '地铁' in teSe:
            item['subway']=1
        else:
            item['subway']=0
        if '房本满五年' in teSe:
            item['five_years']=1
        else:
            item['five_years']=0
        if '房本满两年' in teSe:
            item['two_years']=1
        else:
            item['two_years']=0

        item['orientation'] =  response.xpath('//*[@id="introduction"]/div[1]/div[1]/div[2]/ul/li[7]/text()').extract()[0].rstrip()
        item['decoration'] = response.xpath('//*[@id="introduction"]/div[1]/div[1]/div[2]/ul/li[9]/text()').extract()[0].rstrip()
        item['warm'] = response.xpath('//*[@id="introduction"]/div[1]/div[1]/div[2]/ul/li[11]/text()').extract()[0].rstrip()
        item['floor'] = response.xpath('//*[@id="introduction"]/div[1]/div[1]/div[2]/ul/li[2]/text()').extract()[0].rstrip()
        item['building_type'] = response.xpath('//*[@id="introduction"]/div[1]/div[1]/div[2]/ul/li[6]/text()').extract()[0].rstrip()
        item['built_year'] = response.xpath('//*[@id="introduction"]/div[1]/div[1]/div[2]/ul/li[8]/text()').extract()[0].rstrip()
        item['day_on_market'] = response.xpath('//*[@id="introduction"]/div[1]/div[2]/div[2]/ul/li[3]/text()').extract()[0].rstrip()
        item['huxing_structure'] = response.xpath('//*[@id="introduction"]/div[1]/div[1]/div[2]/ul/li[4]/text()').extract()[0].rstrip()
        item['ratio'] = response.xpath('//*[@id="introduction"]/div[1]/div[1]/div[2]/ul/li[12]/text()').extract()[0].rstrip()
        item['elevator'] = response.xpath('//*[@id="introduction"]/div[1]/div[1]/div[2]/ul/li[14]/text()').extract()[0].rstrip()
        item['purpose'] = response.xpath('//*[@id="introduction"]/div[1]/div[2]/div[2]/ul/li[4]/text()').extract()[0].rstrip()
        item['building_structure'] = response.xpath('//*[@id="introduction"]/div[1]/div[1]/div[2]/ul/li[10]/text()').extract()[0].rstrip()
        yield item




            


