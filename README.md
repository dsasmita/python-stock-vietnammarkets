## Python Crawler Stock Vietnammarkets

Data crawled from http://stock.vietnammarkets.com/vietnam-stock-market.php using Flask
## Crawl Steps

#### Crawl company_index.json  
Endpoint to crawl company list

````    
$ curl -i http://0.0.0.0:8000/crawler/company-index
HTTP/1.1 200 OK
Server: gunicorn/19.9.0
Date: Mon, 10 Sep 2018 06:04:08 GMT
Connection: close
Content-Type: application/json
Content-Length: 183

{
  "count": 251, 
  "end": "Mon, 10 Sep 2018 13:04:08 GMT", 
  "page": "stock.vietnammarkets", 
  "start": "Mon, 10 Sep 2018 13:04:03 GMT", 
  "title": "stock vietnammarkets list"
}
````    

#### Crawl company_profiles.json​
Endpoint to crawl detail company profile

````    
$ curl -i http://0.0.0.0:8000/crawler/company-profile
HTTP/1.1 200 OK
Server: gunicorn/19.9.0
Date: Mon, 10 Sep 2018 06:49:55 GMT
Connection: close
Content-Type: application/json
Content-Length: 194

{
  "count": 251, 
  "end": "Mon, 10 Sep 2018 13:49:55 GMT", 
  "page": "stock.vietnammarkets.profile", 
  "start": "Mon, 10 Sep 2018 13:43:38 GMT", 
  "title": "stock vietnammarkets profile"
}
````    

#### Insert company_profiles.json to DB
Endpoint to insert company_profiles.json to DB

````    
$ curl -i http://0.0.0.0:8000/crawler/company-insert-db
HTTP/1.1 200 OK
Server: gunicorn/19.9.0
Date: Mon, 10 Sep 2018 07:03:27 GMT
Connection: close
Content-Type: application/json
Content-Length: 192

{
  "count": 251, 
  "end": "Mon, 10 Sep 2018 14:03:24 GMT", 
  "page": "stock.vietnammarkets.insert", 
  "start": "Mon, 10 Sep 2018 14:03:24 GMT", 
  "title": "stock vietnammarkets insert"
}
````  
    
    
## API Endpoint

#### 1. Fetch list of companies
Fetch all companies from DB

````
$ curl -i http://0.0.0.0:8000/companies
{
    "count": 251,
    "data": [
        {
            "address_city_district": "Chau Thanh District",
            "address_country": "Vietnam",
            "address_full": "Village 9, Tan Thach Commune, Chau Thanh District, Ben Tre Province",
            "address_full_en": "Village 9, Tan Thach Commune, Chau Thanh District, Ben Tre Province",
            "address_province": "Ben Tre Province",
            "address_street": "Village 9",
            "auditing_company": [
                "Auditing and Informatic Services Company",
                "Address: 142 Nguyen Thi Minh Khai Street - District 3",
                "Tel: (84.8) 9 305 163 (10 lines) - Fax: (84.8) 9 304 28",
                "Website: http://www.aisc.com.vn - Email: aisc@aisc.com.vn"
            ],
            "business": "Food processing",
            "business_registration": {
                "business_license": "553000010  12-25-2003   Department of Planning and Investment of Ben Tre Province",
                "established_license": "3423/QD-UB  12-01-2003  Ben Tre Province People's Committee"
            },
            "business_summary": "Processing and exporting aquatic products; breeding aquatic products; importing materials and commodities; trading; operating restaurants; providing services; and other business scopes decided by the Board of Directors and in line with the laws",
            "business_summary_en": "Processing and exporting aquatic products; breeding aquatic products; importing materials and commodities; trading; operating restaurants; providing services; and other business scopes decided by the Board of Directors and in line with the laws",
            "contact_email": "aquatex@hcm.vnn.vn",
            "contact_phone": [
                "(84.75) 860 265",
                "(84.75)860 346"
            ],
            "contact_website": "www.aquatexbentre.com",
            "crawled_at": "Mon, 10 Sep 2018 13:43:40 GMT",
            "created_at": "Sun, 09 Sep 2018 16:04:26 GMT",
            "financial_summary": {
                "capital_currency": "VND",
                "equity": "0",
                "initial_listed_price": "90000",
                "listed_date": "12-25-2006",
                "listing_volume": "3300000",
                "market_cap": "81000000000",
                "par_value": "10000"
            },
            "listing_bourse": "HOSE",
            "market_cap": "81000000000",
            "name": "BEN TRE AQUAPRODUCT IMPORT AND EXPORT JSC",
            "ticker_symbol": "ABT",
            "uid": "http://stock.vietnammarkets.com/food-processing/ABT/",
            "updated_at": "Sun, 09 Sep 2018 16:04:26 GMT"
        },
    ]
    ...
    "message": "successful",
    "status_code": 200
}
````

#### 2. Fetch specific company
fetch specific company based on name

````
$ http://0.0.0.0:8000/companies?company_name=ben%20tre%20aquaproduct
{
    "count": 23,
    "data": {
        "address_city_district": "Chau Thanh District",
        "address_country": "Vietnam",
        "address_full": "Village 9, Tan Thach Commune, Chau Thanh District, Ben Tre Province",
        "address_full_en": "Village 9, Tan Thach Commune, Chau Thanh District, Ben Tre Province",
        "address_province": "Ben Tre Province",
        "address_street": "Village 9",
        "auditing_company": [
            "Auditing and Informatic Services Company",
            "Address: 142 Nguyen Thi Minh Khai Street - District 3",
            "Tel: (84.8) 9 305 163 (10 lines) - Fax: (84.8) 9 304 28",
            "Website: http://www.aisc.com.vn - Email: aisc@aisc.com.vn"
        ],
        "business": "Food processing",
        "business_registration": {
            "business_license": "553000010  12-25-2003   Department of Planning and Investment of Ben Tre Province",
            "established_license": "3423/QD-UB  12-01-2003  Ben Tre Province People's Committee"
        },
        "business_summary": "Processing and exporting aquatic products; breeding aquatic products; importing materials and commodities; trading; operating restaurants; providing services; and other business scopes decided by the Board of Directors and in line with the laws",
        "business_summary_en": "Processing and exporting aquatic products; breeding aquatic products; importing materials and commodities; trading; operating restaurants; providing services; and other business scopes decided by the Board of Directors and in line with the laws",
        "contact_email": "aquatex@hcm.vnn.vn",
        "contact_phone": [
            "(84.75) 860 265",
            "(84.75)860 346"
        ],
        "contact_website": "www.aquatexbentre.com",
        "crawled_at": "Mon, 10 Sep 2018 13:43:40 GMT",
        "created_at": "Sun, 09 Sep 2018 16:04:26 GMT",
        "financial_summary": {
            "capital_currency": "VND",
            "equity": "0",
            "initial_listed_price": "90000",
            "listed_date": "12-25-2006",
            "listing_volume": "3300000",
            "market_cap": "81000000000",
            "par_value": "10000"
        },
        "listing_bourse": "HOSE",
        "market_cap": "81000000000",
        "name": "BEN TRE AQUAPRODUCT IMPORT AND EXPORT JSC",
        "ticker_symbol": "ABT",
        "uid": "http://stock.vietnammarkets.com/food-processing/ABT/",
        "updated_at": "Sun, 09 Sep 2018 16:04:26 GMT"
    },
    "message": "successful",
    "status_code": 200
}
````

#### 3. Filter Companies based on industry
Fetch companies based on industry

````
$ curl -i http://0.0.0.0:8000/companies?business_industry=Food processing
{
    "count": 22,
    "data": [
        {
            "address_city_district": "Chau Thanh District",
            "address_country": "Vietnam",
            "address_full": "Village 9, Tan Thach Commune, Chau Thanh District, Ben Tre Province",
            "address_full_en": "Village 9, Tan Thach Commune, Chau Thanh District, Ben Tre Province",
            "address_province": "Ben Tre Province",
            "address_street": "Village 9",
            "auditing_company": [
                "Auditing and Informatic Services Company",
                "Address: 142 Nguyen Thi Minh Khai Street - District 3",
                "Tel: (84.8) 9 305 163 (10 lines) - Fax: (84.8) 9 304 28",
                "Website: http://www.aisc.com.vn - Email: aisc@aisc.com.vn"
            ],
            "business": "Food processing",
            "business_registration": {
                "business_license": "553000010  12-25-2003   Department of Planning and Investment of Ben Tre Province",
                "established_license": "3423/QD-UB  12-01-2003  Ben Tre Province People's Committee"
            },
            "business_summary": "Processing and exporting aquatic products; breeding aquatic products; importing materials and commodities; trading; operating restaurants; providing services; and other business scopes decided by the Board of Directors and in line with the laws",
            "business_summary_en": "Processing and exporting aquatic products; breeding aquatic products; importing materials and commodities; trading; operating restaurants; providing services; and other business scopes decided by the Board of Directors and in line with the laws",
            "contact_email": "aquatex@hcm.vnn.vn",
            "contact_phone": [
                "(84.75) 860 265",
                "(84.75)860 346"
            ],
            "contact_website": "www.aquatexbentre.com",
            "crawled_at": "Mon, 10 Sep 2018 13:43:40 GMT",
            "created_at": "Sun, 09 Sep 2018 16:04:26 GMT",
            "financial_summary": {
                "capital_currency": "VND",
                "equity": "0",
                "initial_listed_price": "90000",
                "listed_date": "12-25-2006",
                "listing_volume": "3300000",
                "market_cap": "81000000000",
                "par_value": "10000"
            },
            "listing_bourse": "HOSE",
            "market_cap": "81000000000",
            "name": "BEN TRE AQUAPRODUCT IMPORT AND EXPORT JSC",
            "ticker_symbol": "ABT",
            "uid": "http://stock.vietnammarkets.com/food-processing/ABT/",
            "updated_at": "Sun, 09 Sep 2018 16:04:26 GMT"
        },
        ...
    ]
    "message": "successful",
    "status_code": 200
}
````

#### 4. Filter companies by company Market Cap
Filter companies by market cap

````
$ curl -i http://0.0.0.0:8000/companies?market_cap_min=90000000000&market_cap_min=96000000000&
{
    "count": 8,
    "data": [
        {
            "address_city_district": "",
            "address_country": "Vietnam",
            "address_full": "Ba Dinh Ward, Bim Son Town, Thanh Hoa Privince",
            "address_full_en": "Ba Dinh Ward, Bim Son Town, Thanh Hoa Privince",
            "address_province": "",
            "address_street": "Ba Dinh Ward",
            "auditing_company": [
                "Accounting and Auditing Financial Consultancy Service Company (AASC)",
                "Address: 01 Le Phung Hieu Street - Hanoi",
                "Tel: (84-4) 826 8681 - Fax: (84-4) 825 3973",
                "Email: aasc-ndd@hn.vnn.vn",
                "Website: http://www.aasc.com.vn"
            ],
            "business": "Construction materials",
            "business_registration": {
                "business_license": "20603000429  05-01-2006   Planning and Investment Department of Thanh Hoa Province",
                "established_license": "366/BXD-TCLD  08-12-1993  Ministry of Construction"
            },
            "business_summary": "Manufacturing, trading, exporting and importing cement, clinker and other construction materials",
            "business_summary_en": "Manufacturing, trading, exporting and importing cement, clinker and other construction materials",
            "contact_email": "ttximangbimson@hn.vnn.vn",
            "contact_phone": [
                "(84-37) 824 242",
                "(84-37) 824 046"
            ],
            "contact_website": "www.ximangbimson.com.vn",
            "crawled_at": "Mon, 10 Sep 2018 13:43:54 GMT",
            "created_at": "Sun, 09 Sep 2018 16:04:26 GMT",
            "financial_summary": {
                "capital_currency": "VND",
                "equity": "0",
                "initial_listed_price": "0",
                "listed_date": "11-24-2006",
                "listing_volume": "90000000",
                "market_cap": "900000000000",
                "par_value": "10000"
            },
            "listing_bourse": "HASTC",
            "market_cap": "900000000000",
            "name": "BIM SON CEMENT JOINT STOCK COMPANY",
            "ticker_symbol": "BCC",
            "uid": "http://stock.vietnammarkets.com/construction-materials/BCC/",
            "updated_at": "Sun, 09 Sep 2018 16:04:26 GMT"
        },
        ...
    ]
    "message": "successful",
    "status_code": 200
}
````