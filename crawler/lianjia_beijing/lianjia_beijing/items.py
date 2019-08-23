# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class LianjiaBeijingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #标题
    title = scrapy.Field()
    #详细描述
    full_desp = scrapy.Field()
    #价格
    price = scrapy.Field()
    #单价
    unit_price = scrapy.Field()
    #小区名字
    community_name = scrapy.Field()
    # 地区
    region = scrapy.Field()
    #联系人
    #linkman = scrapy.Field()
    #联系电话
    #linktel = scrapy.Field()
    #户型
    house_type = scrapy.Field()
    #建筑面积
    construction_area = scrapy.Field()
    #实际面积
    actual_area = scrapy.Field()
    #房屋朝向
    orientation = scrapy.Field()
    #装修情况
    decoration = scrapy.Field()
    #所在楼层
    floor = scrapy.Field()
    #电梯
    elevator = scrapy.Field()
    #产权年限
    property_limit = scrapy.Field()
    #房屋年限
    house_year = scrapy.Field()
    #有无抵押
    mortgage = scrapy.Field()
    #房屋用途
    purpose = scrapy.Field()
    #挂牌时间
    release_date = scrapy.Field()
    #上次交易时间
    last_date = scrapy.Field()
    #供暖方式
    warm = scrapy.Field()
    pass

class zuFangItem(scrapy.Item):

    #标题
    title = scrapy.Field()
    #价格
    price = scrapy.Field()
    #地区
    region = scrapy.Field()
    #付款时长
    pay = scrapy.Field()
    #地铁信息
    retro = scrapy.Field()
    #方式
    way = scrapy.Field()
    #户型
    house_type = scrapy.Field()
    #面积
    area = scrapy.Field()
    #方向
    orientation = scrapy.Field()
    #配套实施
    facility = scrapy.Field()
    #详细描述
    desp = scrapy.Field()
    #发布日期
    release_date = scrapy.Field()
    #租期
    lease = scrapy.Field()
    #楼层
    floor = scrapy.Field()
    #用电方式
    elc_usage = scrapy.Field()
    #供暖方式
    #warm = scrapy.Field()
    #入住
    moveIn = scrapy.Field()
    #电梯
    elevator = scrapy.Field()
    #用水
    water_usage = scrapy.Field()
    #燃气
    gas = scrapy.Field()


class chengJiaoItem(scrapy.Item):
    #链家编号
    id = scrapy.Field()
    #小区
    community = scrapy.Field()
    #城区
    big_district = scrapy.Field()
    #小城区
    small_district = scrapy.Field()
    #成交价格
    price = scrapy.Field()
    #均价
    price_unit = scrapy.Field()
    #小区均价
    #community_price_avg = scrapy.Field()
    #地铁
    subway = scrapy.Field()
    #房本是否五年
    five_years = scrapy.Field()
    #房本是否两年
    two_years = scrapy.Field()
    #关注人数
    followers = scrapy.Field()
    #房屋户型
    house_type = scrapy.Field()
    #面积
    area = scrapy.Field()
    #房屋朝向
    orientation = scrapy.Field()
    #装修情况
    decoration = scrapy.Field()
    #供暖方式
    warm = scrapy.Field()
    #所在楼层
    floor = scrapy.Field()
    #建筑类型
    building_type = scrapy.Field()
    #建筑类型
    building_structure = scrapy.Field()
    #建成年代
    built_year = scrapy.Field()
    #挂牌日期
    day_on_market = scrapy.Field()
    #户型结构
    huxing_structure = scrapy.Field()
    #户梯比例
    ratio = scrapy.Field()
    #电梯
    elevator = scrapy.Field()
    #房屋用途
    purpose = scrapy.Field()
    #成交时间
    trade_time = scrapy.Field()
    #小区ID
    community_id = scrapy.Field()
    #URL
    url = scrapy.Field()