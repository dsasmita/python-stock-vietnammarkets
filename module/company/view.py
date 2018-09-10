import datetime
import json

from flask import Blueprint, jsonify, request

from module.company.model_crawler import Company, db_crawler
from module.company.vietnammarkets.VietnamMarkets import VietnamMarkets

module_company = Blueprint('module_scrap_news', __name__, template_folder='templates')

@module_company.route('/')
def index():
    data = {'page': 'leadbook', 'title': 'stock.vietnammarkets'}
    return jsonify(data)

@module_company.route('/company-index')
def company_index():
    start_time = datetime.datetime.now()

    vietnam_market = VietnamMarkets()
    company_list = vietnam_market.company_index()

    if len(company_list) > 0:
        with open('files/company_index.json', 'w') as outfile:
            json.dump(company_list, outfile)

    end_time = datetime.datetime.now()

    data = {
        'page': 'stock.vietnammarkets',
        'title': 'stock vietnammarkets list',
        'count': len(company_list),
        'start': start_time,
        'end': end_time
    }
    return jsonify(data)

@module_company.route('/company-profile')
def company_profile():
    start_time = datetime.datetime.now()

    try:
        f = open('files/company_index.json', 'r')
        profiles = json.loads(f.read())
    except IOError:
        data = {
            'page': 'stock.vietnammarkets.profile',
            'title': 'stock vietnammarkets profile',
            'result': 'file company_index.json not found'
        }
        return jsonify(data)

    vietnam_market = VietnamMarkets()
    company_profiles = vietnam_market.company_crawler_list(profiles)

    if len(company_profiles) > 0:
        with open('files/company_profiles.json', 'w') as outfile:
            json.dump(company_profiles, outfile)

    end_time = datetime.datetime.now()

    data = {
        'page': 'stock.vietnammarkets.profile',
        'title': 'stock vietnammarkets profile',
        'count': len(company_profiles),
        'start': start_time,
        'end': end_time
    }
    return jsonify(data)

@module_company.route('/company-insert-db')
def company_insert_db():
    start_time = datetime.datetime.now()

    try:
        f = open('files/company_profiles.json', 'r')
        profiles = json.loads(f.read())
    except IOError:
        data = {
            'page': 'stock.vietnammarkets.insert',
            'title': 'stock vietnammarkets insert',
            'result': 'file company_profiles.json not found'
        }
        return jsonify(data)

    end_time = datetime.datetime.now()

    for profile in profiles:
        check_exist = Company.query.filter_by(uid=profile['uid']).count()
        if check_exist == 0:
            prof = Company()
            prof.name = profile['name']
            prof.ticker_symbol = profile['ticker_symbol']
            prof.uid = profile['uid']
            prof.business = profile['business']
            prof.contact_phone = json.dumps(profile['contact_phone'])
            prof.contact_website = profile['contact_website']
            prof.contact_email = profile['contact_email']
            prof.listing_bourse = profile['listing_bourse']
            prof.address_full_en = profile['address_full_en']
            prof.address_full = profile['address_full']
            prof.address_city_district = profile['address_city_district']
            prof.address_street = profile['address_street']
            prof.address_province = profile['address_province']
            prof.address_country = profile['address_country']
            prof.business_summary = profile['business_summary']
            prof.business_summary_en = profile['business_summary_en']
            prof.market_cap = profile['market_cap']
            prof.financial_summary = json.dumps(profile['financial_summary'])
            prof.business_registration = json.dumps(profile['business_registration'])
            prof.auditing_company = json.dumps(profile['auditing_company'])
            prof.crawled_at = request.args.get('date', profile['crawled_at'])

            db_crawler.session.add(prof)
            db_crawler.session.commit()

        else:
            prof = Company.query.filter_by(uid=profile['uid']).first()

            prof.name = profile['name']
            prof.ticker_symbol = profile['ticker_symbol']
            prof.uid = profile['uid']
            prof.business = profile['business']
            prof.contact_phone = json.dumps(profile['contact_phone'])
            prof.contact_website = profile['contact_website']
            prof.contact_email = profile['contact_email']
            prof.listing_bourse = profile['listing_bourse']
            prof.address_full_en = profile['address_full_en']
            prof.address_full = profile['address_full']
            prof.address_city_district = profile['address_city_district']
            prof.address_street = profile['address_street']
            prof.address_province = profile['address_province']
            prof.address_country = profile['address_country']
            prof.business_summary = profile['business_summary']
            prof.business_summary_en = profile['business_summary_en']
            prof.market_cap = profile['market_cap']
            prof.financial_summary = json.dumps(profile['financial_summary'])
            prof.business_registration = json.dumps(profile['business_registration'])
            prof.auditing_company = json.dumps(profile['auditing_company'])
            prof.crawled_at = request.args.get('date', profile['crawled_at'])

            db_crawler.session.add(prof)
            db_crawler.session.commit()

    data = {
        'page': 'stock.vietnammarkets.insert',
        'title': 'stock vietnammarkets insert',
        'count': len(profiles),
        'start': start_time,
        'end': end_time
    }
    return jsonify(data)