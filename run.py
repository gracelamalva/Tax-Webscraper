from scraper import download, scrape_json
import sys
import json

if (len(sys.argv) == 0):
    print("Bad args try again")
    print("Run: python3 run.py [function]")

elif(sys.argv[1] == "scrape"):
    search_query = input ("Enter Form Name: " ) #"Form W-9S"
    results = scrape_json(search_query)
    for result in results:
        print (f'FOUND!!!!! Product Number: {result["form_number"]} Title: {result["form_title"]} Years Available: {result["min_year"]}')
    print(json.dumps(result))    

elif(sys.argv[1] == "download"):
    tax_form = input ("Enter name of tax form: ") #"Form W-9S"
    start_year = int(input ("Enter start year: "))   #2003
    end_year = int(input ("Enter end year: ") )      #2006

    download(tax_form, start_year, end_year)

