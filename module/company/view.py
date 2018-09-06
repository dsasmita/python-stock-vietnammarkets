import datetime
import json

from flask import Blueprint, jsonify

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
    comapny_list = vietnam_market.company_index()

    with open('files/company_index.json', 'w') as outfile:
        json.dump(comapny_list, outfile)

    end_time = datetime.datetime.now()

    data = {
        'page': 'stock.vietnammarkets',
        'title': 'stock vietnammarkets list',
        'count': len(comapny_list),
        'start': start_time,
        'end': end_time
    }
    return jsonify(data)