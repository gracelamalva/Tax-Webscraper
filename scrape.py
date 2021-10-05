from bs4 import BeautifulSoup
import requests
import json
import numpy as np
import config



pages = np.arange(1,20236,200)

for page in pages: 
    page = requests.get("https://apps.irs.gov/app/picklist/list/priorFormPublication.html;j?resultsPerPage=200&sortColumn=sortOrder&indexOfFirstRow=" + str(page)+ "&criteria=&value=&isDescending=false")
        
    #req = requests.get(page.text,headers)
    soup = BeautifulSoup(page.text,'html.parser')
                        #req.content

    table = soup.find('table', class_ = 'picklist-dataTable')
    rows = table.find_all('tr')

    search_query = input ("Enter Form Name: " ) #"Form W-9S"

    for row in rows[1:]:

        product_no = row.find('a').text
        title = row.find('td', class_="MiddleCellSpacer").text.strip()
        year_avl = soup.find('td', class_= "EndCellSpacer").text.strip()
        print(f'Product Number: {product_no} Title: {title} Years Available: {year_avl}')

        if (search_query == product_no ):

            result = [
                {
                    "form_number": product_no,
                    "form_title": title,
                    "min_year": year_avl,
                    "max_year": year_avl
                }

            ]

            print (f'FOUND!!!!! Product Number: {product_no} Title: {title} Years Available: {year_avl}')
            print(json.dumps(result))
           
