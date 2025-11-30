import json
import sqlite3
from datetime import datetime
from itemadapter import ItemAdapter


class JobScraperPipeline:
    """
    Pipeline to store scraped jobs in SQLite database
    """
    
    def __init__(self):
        self.conn = None
        self.cur = None
    
    def open_spider(self, spider):
        """Called when spider opens - create database connection"""
        self.conn = sqlite3.connect('jobs.db')
        self.cur = self.conn.cursor()
        
        # Create table if it doesn't exist
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                company TEXT,
                location TEXT,
                sector TEXT,
                description TEXT,
                salary TEXT,
                contract_type TEXT,
                posted_date TEXT,
                source_website TEXT,
                job_url TEXT UNIQUE,
                scraped_at TEXT
            )
        ''')
        self.conn.commit()
    
    def close_spider(self, spider):
        """Called when spider closes - close database connection"""
        self.conn.close()
    
    def process_item(self, item, spider):
        """Process each scraped item"""
        adapter = ItemAdapter(item)
        
        # Add timestamp when scraped
        adapter['scraped_at'] = datetime.now().isoformat()
        
        try:
            # Insert or ignore if URL already exists (avoid duplicates)
            self.cur.execute('''
                INSERT OR IGNORE INTO jobs (
                    title, company, location, sector, description, 
                    salary, contract_type, posted_date, source_website, 
                    job_url, scraped_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                adapter.get('title'),
                adapter.get('company'),
                adapter.get('location'),
                adapter.get('sector'),
                adapter.get('description'),
                adapter.get('salary'),
                adapter.get('contract_type'),
                adapter.get('posted_date'),
                adapter.get('source_website'),
                adapter.get('job_url'),
                adapter.get('scraped_at')
            ))
            self.conn.commit()
            
        except sqlite3.Error as e:
            spider.logger.error(f"Database error: {e}")
        
        return item


class JsonWriterPipeline:
    """
    Pipeline to write scraped items to a JSON file
    """
    
    def open_spider(self, spider):
        self.file = open('jobs.json', 'w', encoding='utf-8')
        self.file.write('[')
        self.first_item = True
    
    def close_spider(self, spider):
        self.file.write(']')
        self.file.close()
    
    def process_item(self, item, spider):
        if not self.first_item:
            self.file.write(',\n')
        else:
            self.first_item = False
        
        line = json.dumps(dict(item), ensure_ascii=False, indent=2)
        self.file.write(line)
        return item