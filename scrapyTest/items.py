from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item, Field

class ScrapytestItem(Item):
	name = 'Test'
	allowed_domains = ["craigslist.org"]
	start_urls = ["http://sfbay.craigslist.org/search/npo"]
	title = Field()
	link = Field()
    pass

	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		titles = hxs.select("//span[@class='p1']")
		for title in titles:
			title = titles.select("a/text()").extract()
			link = titles.select("a/@href").extract()
			print title, link