import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, DateTime, BigInteger, String, Text

db_crawler = SQLAlchemy()


class Company(db_crawler.Model):
    __tablename__ = 'company_lists'
    id = Column(BigInteger, primary_key=True)
    name = Column(Text)
    ticker_symbol = Column(Text)
    uid = Column(Text)
    business = Column(Text)
    contact_phone = Column(Text)
    contact_website = Column(Text)
    contact_email = Column(Text)
    listing_bourse = Column(Text)
    address_full_en = Column(Text)
    address_full = Column(Text)
    address_city_district = Column(Text)
    address_street = Column(Text)
    address_province = Column(Text)
    address_country = Column(Text)
    business_summary = Column(Text)
    business_summary_en = Column(Text)
    market_cap = Column(Text)
    financial_summary = Column(Text)
    business_registration = Column(Text)
    auditing_company = Column(Text)
    crawled_at = Column(DateTime, default=datetime.datetime.utcnow)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)