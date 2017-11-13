#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Please note that the function 'make_request' is provided for your reference only.
# You will not be able to to actually use it from within the Udacity web UI.
# Your task is to process the HTML using BeautifulSoup, extract the hidden
# form field values for "__EVENTVALIDATION" and "__VIEWSTATE" and set the appropriate
# values in the data dictionary.
# All your changes should be in the 'extract_data' function
# from bs4 import BeautifulSoup
import requests
import json


html_page = "vrigin_and_logan_airport.html"
temp_html_page = 'temp.html'




# def extract_data(page):
#     data = {"eventvalidation": "",
#             "viewstate": ""}
#     with open(page, "r") as html:
#         # do something here to find the necessary values
#         soup = BeautifulSoup(html, 'html.parser')
#         data['eventvalidation'] = soup.find(id='__EVENTVALIDATION')['value']
#         data['viewstate'] = soup.find(id='__VIEWSTATE')['value']
#
#         pass
#
#     return data


def make_request(data):
    eventvalidation = data["eventvalidation"]
    viewstate = data["viewstate"]

    r = requests.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
                      data={'AirportList': "BOS",
                            'CarrierList': "VX",
                            'Submit': 'Submit',
                            "__EVENTTARGET": "",
                            "__EVENTARGUMENT": "",
                            "__EVENTVALIDATION": eventvalidation,
                            "__VIEWSTATE": viewstate
                            })

    print(r.text)
    f = open(html_page, 'w')
    f.write(r.text)


def test():
    import pdb; pdb.set_trace()

    s = requests.Session()
    r = s.get('http://www.transtats.bts.gov/Data_Elements.aspx?Data=2', verify=False)

    f = open(temp_html_page, 'w')
    f.write(r.text)
    # data = extract_data(temp_html_page)

    # eventvalidation = data['eventvalidation']
    # viewstate = data['viewstate']
    # make_request(data)



    # assert data["eventvalidation"] != ""
    # assert data["eventvalidation"].startswith("/wEWjAkCoIj1ng0")
    # assert data["viewstate"].startswith("/wEPDwUKLTI")


test()