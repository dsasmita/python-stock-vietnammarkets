# -*- coding: utf-8 -*-
import datetime
import re

import bs4
import requests
from flask import request
from googletrans import Translator


class VietnamMarkets:
    HEADERS = {
        'Accept-Encoding': 'gzip, '
        'deflate, sdch', 'Accept-Language': 'en-US,en;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Cache-Control': 'max-age=0', 'Connection': 'keep-alive'}
    LINK = 'http://stock.vietnammarkets.com/vietnam-stock-market.php'

    def company_index(self):
        companies = []
        try:
            content = requests.get(VietnamMarkets.LINK, timeout=10, headers=VietnamMarkets.HEADERS)
        except:
            return companies

        response = bs4.BeautifulSoup(content.text, "html.parser")

        result = response.find('div', 'results')

        if result is not None:
            for tr in result.select("tr"):
                row = tr.findAll('td')
                if row[0].get_text() != 'Ticker':
                    tmp = {}
                    tmp['ticker_symbol'] = row[0].get_text()
                    tmp['url'] = row[0].find('a')['href']
                    tmp['company_name'] = row[1].get_text()
                    tmp['business'] = row[2].get_text()
                    tmp['listing_bourse'] = row[3].get_text()
                    tmp['crawled_at'] = request.args.get('date', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                    companies.append(tmp)

        response.decompose()
        return companies

    def company_profiles(self, profile):
        url = profile['url']
        profile = {}
        try:
            content = requests.get(url, timeout=10, headers=VietnamMarkets.HEADERS)
        except:
            return profile
        response = bs4.BeautifulSoup(content.text, "html.parser")

        result = response.find('div', 'results')

        if result is not None:
            container = result.select_one('table')
            company_profile = []
            financial_summary = []
            business_summary = []
            for row in container.select("td"):
                if 'Company Profile' in row.get_text():
                    company_profile = row
                if 'Financial Summary' in row.get_text():
                    financial_summary = row
                if 'Business Summary' in row.get_text():
                    business_summary = row

            # company profile
            company_name_container = result.find_all('p', 'r1', limit=5)
            company_name = company_name_container[4].find('strong').get_text().replace('(', '').replace(')', '').split(':')
            company_profile = company_profile.prettify().split('<br/>')

            profile['name'] = company_name[1].strip()
            profile['uid'] = url
            profile['contact_phone'] = [company_profile[3].strip(), company_profile[4].strip()]
            profile['contact_email'] = company_profile[5].strip()
            profile['contact_website'] = company_profile[6].strip()
            profile['business'] = company_profile[7].replace('Business:', '').strip()

            # address
            profile['address_country'] = 'Vietnam'
            profile['address_full'] = company_profile[2].strip()
            profile['address_full_en'] = ''

            profile['address_street'] = profile['address_full']
            profile['address_city_district'] = ''
            profile['address_province'] = ''

            address = profile['address_full'].split(',')
            if len(address) > 2:
                try:
                    translator = Translator()
                    address_en = translator.translate(profile['address_full'], dest='en')
                    profile['address_full_en'] = address_en.text
                    address = profile['address_full_en'].split(',')
                except:
                    print('error line 92')
                    address = profile['address_full'].split(',')

                for add in address:
                    tmp = str.lower(add)
                    if 'city' in tmp or 'district' in tmp:
                        profile['address_city_district'] = add.strip()
                    if 'province' in tmp:
                        profile['address_province'] = add.strip()
                profile['address_street'] = address[0]

            # ticker symbol and listing bourse
            ticket_bourse = company_name[0].split('-')
            profile['ticker_symbol'] = ticket_bourse[0].strip()
            profile['listing_bourse'] = ticket_bourse[1].strip()

            # financial summary
            financial = {}
            financial['capital_currency'] = ''
            financial['market_cap'] = ''
            financial['par_value'] = ''
            financial['equity'] = ''
            financial['listing_volume'] = ''
            financial['listed_date'] = ''
            financial['initial_listed_price'] = ''

            for row in financial_summary.find_all('tr'):
                tmp = row.get_text().split(':')
                tmp_string = str.lower(row.get_text())
                value = tmp[1].replace(',', '')
                if 'capital currency' in tmp_string:
                    financial['capital_currency'] = value
                if 'market cap' in tmp_string:
                    financial['market_cap'] = value
                if 'par value' in tmp_string:
                    financial['par_value'] = value
                if 'equity' in tmp_string:
                    financial['equity'] = value
                if 'listing volume' in tmp_string:
                    financial['listing_volume'] = value
                if 'listed date' in tmp_string:
                    financial['listed_date'] = value
                if 'initial listed price' in tmp_string:
                    financial['initial_listed_price'] = value

            profile['financial_summary'] = financial
            profile['market_cap'] = financial['market_cap']

            # business summary
            summary = re.findall('Business Summary:(.*?)Auditing Company:', business_summary.get_text(), re.DOTALL)
            profile['business_summary'] = summary[0].strip()
            profile['business_summary_en'] = ''
            try:
                translator = Translator()
                business_summary_en = translator.translate(summary[0].strip(), dest='en')
                profile['business_summary_en'] = business_summary_en.text
            except:
                print('error line 148')
                profile['business_summary_en'] = ''

            # auditing company
            auditings = re.findall('Auditing Company:(.*?)Business Registration:', business_summary.prettify(), re.DOTALL)
            auditing_split = auditings[0].replace('<strong>', '').replace('</strong>', '').split('<br/>')
            auditing = []
            for row in auditing_split:
                if row.strip() != '':
                    auditing.append(row.strip())
            profile['auditing_company'] = auditing

            # business registration
            reg = business_summary.prettify().split('Business Registration:')
            reg = reg[1].split('<br/>')
            registration = {}
            for row in reg:
                if 'Established License' in row:
                    registration['established_license'] = row.replace('Established License:', '').replace('Established License', '').strip()
                if 'Business License' in row:
                    registration['business_license'] = row.replace('Business License:', '').replace('Business License', '').strip()
            profile['business_registration'] = registration

            profile['crawled_at'] = request.args.get('date', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

        response.decompose()

        data = profile
        return data

    def company_crawler_list(self, profiles):
        n = 0
        results = []
        for profile in profiles:
            profile_detail = self.company_profiles(profile)
            results.append(profile_detail)
            n = n + 1

        return results

    def phone_format(self, phone_number):
        clean_phone_number = re.sub('[^0-9]+', '', phone_number)
        formatted_phone_number = re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1-", "%d" % int(clean_phone_number[:-1])) + \
                                 clean_phone_number[-1]
        return formatted_phone_number