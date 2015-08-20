import scrapy
from flipkart.items import FlipkartItem

class FlipkartSpider(scrapy.Spider):
    name = "flipkart"
    allowed_domain = ["flipkart.com"]
    start_urls = ["http://www.flipkart.com/nexus-6/p/itme7zd5x6rfaps9?pid=MOBEFAGFZHG7SRZU&ref=L%3A6577827142689115781&srno=p_1&query=nexus+6&otracker=from-search"]
    item = FlipkartItem()

    def parse(self, response):
        self.item['name'] = response.xpath('//h1[@class="title"]/text()').extract()
        self.item['ratingOutOfFive'] = response.xpath('//div[@class="bigStar"]/text()').extract()
        self.item['review'] = response.xpath('//div[@class="reviews"]/a/span/text()').extract()
        self.item['ratingByUser'] = response.xpath('//div[@class="avgWrapper"]/p[@class="subText"]/text()').extract()
        self.item['price'] = response.xpath('//span[@class="selling-price omniture-field"]/text()').extract()
        self.item['delivery'] = response.xpath('//div[@class="delivery"]/ul/li/text()').extract() 
        self.item['SellerOffer'] = response.xpath('//div[@class="bottomOffers"]//span[@class="offerDescription"]/text()').extract()
        self.item['AvailableOrNot'] = response.xpath('//div[@class="out-of-stock-text"]/div[@class="out-of-stock-status"]/text()').extract()
        return self.item
'''
        print "----------flipkart-----------"
        print name[0].strip()
        print ratingOutOfFive[0].strip()
        print ratingByUser[0].strip() + ratingByUser[1].strip()
        print review[0].strip()
        print price[0].strip()
        print delivery[0].strip() 
        print SellerOffer[0].strip()
        print AvailableOrNot
        print "-----------------------------"
'''
