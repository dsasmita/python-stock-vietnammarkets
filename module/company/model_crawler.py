import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, DateTime, BigInteger, String

db_crawler = SQLAlchemy()


class Company(db_crawler.Model):
    __tablename__ = 'company_lists'
    id = Column(BigInteger, primary_key=True)
    ticker_symbol = Column(String(255))
    company_name = Column(String(255))
    url = Column(String(255))
    business = Column(String(255))
    listing_bourse = Column(String(60))
    crawled_at = Column(DateTime, default=datetime.datetime.utcnow)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)