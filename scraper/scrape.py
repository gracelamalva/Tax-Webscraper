from bs4 import BeautifulSoup
import requests
import numpy as np
from scraper import config


def scrape_json (search_query):
    pages = np.arange(1,20236,200)
    results = []

    for page in pages: 
        page = requests.get(config.URL + ";j?resultsPerPage=200&sortColumn=sortOrder&indexOfFirstRow=" + str(page)+ "&criteria=&value=&isDescending=false")
            
        #req = requests.get(page.text,headers)
        soup = BeautifulSoup(page.text,'html.parser')
                            #req.content

        table = soup.find('table', class_ = 'picklist-dataTable')
        rows = table.find_all('tr')

    

        for row in rows[1:]:

            product_no = row.find('a').text
            title = row.find('td', class_="MiddleCellSpacer").text.strip()
            year_avl = soup.find('td', class_= "EndCellSpacer").text.strip()
            #print(f'Product Number: {product_no} Title: {title} Years Available: {year_avl}')

            if (search_query == product_no ):

                product = {
                        "form_number": product_no,
                        "form_title": title,
                        "min_year": year_avl,
                        "max_year": year_avl
                    }
                
                results.append(product)

                


    return results
            
