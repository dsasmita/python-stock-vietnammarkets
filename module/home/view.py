import json
from flask import Blueprint, jsonify, request

from module.company.model_crawler import Company

module_home = Blueprint('module_home', __name__, template_folder='templates')


@module_home.route('/')
def index():
    data = {'page': 'leadbook', 'title': 'api'}
    return jsonify(data)

@module_home.route('/companies', methods=['GET'])
def companies():

    companies = Company.query
    # company_name
    company_name = request.args.get('company_name', default='')
    if company_name != '':
        company = companies.filter(Company.name.contains(company_name)).first()

        formated = {}
        tmp = {}
        tmp['name'] = company.name
        tmp['ticker_symbol'] = company.ticker_symbol
        tmp['uid'] = company.uid
        tmp['business'] = company.business
        tmp['contact_phone'] = json.loads(company.contact_phone)
        tmp['contact_website'] = company.contact_website
        tmp['contact_email'] = company.contact_email
        tmp['listing_bourse'] = company.listing_bourse
        tmp['address_full_en'] = company.address_full_en
        tmp['address_full'] = company.address_full
        tmp['address_city_district'] = company.address_city_district
        tmp['address_street'] = company.address_street
        tmp['address_province'] = company.address_province
        tmp['address_country'] = company.address_country
        tmp['business_summary'] = company.business_summary
        tmp['business_summary_en'] = company.business_summary_en
        tmp['market_cap'] = company.market_cap
        tmp['financial_summary'] = json.loads(company.financial_summary)
        tmp['business_registration'] = json.loads(company.business_registration)
        tmp['auditing_company'] = json.loads(company.auditing_company)
        tmp['crawled_at'] = company.crawled_at
        tmp['created_at'] = company.created_at
        tmp['updated_at'] = company.updated_at
        formated = tmp
    else:
        # business_industry
        business_industry = request.args.get('business_industry', default='')
        if business_industry != '':
            companies = companies.filter(Company.business.contains(business_industry))

        # market cap
        market_cap_min = request.args.get('market_cap_min', default='')
        market_cap_max = request.args.get('market_cap_max', default='')
        if market_cap_max != '' and market_cap_min != '':
            companies = companies.filter(Company.market_cap.between(market_cap_min, market_cap_max))
        elif market_cap_min != '':
            companies = companies.filter(Company.market_cap >= market_cap_min)
        elif market_cap_max != '':
            companies = companies.filter(Company.market_cap <= market_cap_max)

        companies = companies.all()

        formated = []
        for company in companies:
            tmp = {}
            tmp['name'] = company.name
            tmp['ticker_symbol'] = company.ticker_symbol
            tmp['uid'] = company.uid
            tmp['business'] = company.business
            tmp['contact_phone'] = json.loads(company.contact_phone)
            tmp['contact_website'] = company.contact_website
            tmp['contact_email'] = company.contact_email
            tmp['listing_bourse'] = company.listing_bourse
            tmp['address_full_en'] = company.address_full_en
            tmp['address_full'] = company.address_full
            tmp['address_city_district'] = company.address_city_district
            tmp['address_street'] = company.address_street
            tmp['address_province'] = company.address_province
            tmp['address_country'] = company.address_country
            tmp['business_summary'] = company.business_summary
            tmp['business_summary_en'] = company.business_summary_en
            tmp['market_cap'] = company.market_cap
            tmp['financial_summary'] = json.loads(company.financial_summary)
            tmp['business_registration'] = json.loads(company.business_registration)
            tmp['auditing_company'] = json.loads(company.auditing_company)
            tmp['crawled_at'] = company.crawled_at
            tmp['created_at'] = company.created_at
            tmp['updated_at'] = company.updated_at
            formated.append(tmp)

    data = {
        'status_code' : 200,
        'count' : len(formated),
        'message' : 'successful',
        'data' : formated
    }
    return jsonify(data)