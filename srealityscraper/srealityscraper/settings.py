BOT_NAME = 'srealityscraper'
SPIDER_MODULES = ['srealityscraper.spiders']
NEWSPIDER_MODULE = 'srealityscraper.spiders'
ROBOTSTXT_OBEY = False

DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}
SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
FEED_EXPORT_ENCODING = 'utf-8'
ITEM_PIPELINES = {
   'srealityscraper.pipelines.SrealityPipeline': 300,
}
