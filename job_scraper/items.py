import scrapy

class JobItem(scrapy.Item):
    """
    Defines the structure of job data we'll scrape
    """
    # Basic job information
    title = scrapy.Field()
    company = scrapy.Field()
    location = scrapy.Field()
    sector = scrapy.Field()
    
    # Job details
    description = scrapy.Field()
    salary = scrapy.Field()
    contract_type = scrapy.Field()  
    
    # Metadata
    posted_date = scrapy.Field()
    source_website = scrapy.Field()
    job_url = scrapy.Field()
    scraped_at = scrapy.Field()  