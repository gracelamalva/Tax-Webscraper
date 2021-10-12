from bs4 import BeautifulSoup
import requests
import numpy as np
from os import path, makedirs
from scraper import config



def download(tax_form, start_year, end_year):
    req = requests.get(config.URL,config.HEADERS)
    soup = BeautifulSoup(req.content,'html.parser')

    table = soup.find('table', class_ = 'picklist-dataTable')
    rows = table.find_all('tr')

    pages = np.arange(1,20236,200)

    year_range = (np.arange(start_year,end_year+1, 1))       #2003, 2004, 2005, 2006

    for page in pages: 
        page = requests.get(config.URL +";j?resultsPerPage=200&sortColumn=sortOrder&indexOfFirstRow=" + str(page)+ "&criteria=&value=&isDescending=false")
            
        #req = requests.get(page.text,headers)
        soup = BeautifulSoup(page.text,'html.parser')
                            #req.content

        table = soup.find('table', class_ = 'picklist-dataTable')
        rows = table.find_all('tr')

        links = table.find_all('a')

        i = 0

        for row in rows[1:]:
            product_no = row.find('a').text
            product_link = row.find('a')
            title = row.find('td', class_="MiddleCellSpacer").text.strip()
            year_avl = soup.find('td', class_= "EndCellSpacer").text.strip()
            
            #print(f'Product Number: {product_no} Title: {title} Years Available: {year_avl}')
            if (tax_form == product_no and year_avl in str(year_range)):
                print (f'FOUND!!!!! Product Number: {product_no} Title: {title} Years Available: {year_avl}')
                    
                i+=1 
                print("Downloading File: ", i )

                response = requests.get(product_link.get('href'))
                folder = path.join("Forms", product_no)
                if not path.exists(folder):
                    makedirs(folder)

                pdf = open(path.join("Forms" , product_no, product_no+"-"+ year_avl + "-"+ str(i) +".pdf"), 'wb')
            
                pdf.write(response.content)
                pdf.close()
                print("File ", i, " downloaded")

    print("All pdfs downloaded")

