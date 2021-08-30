#!/usr/bin/python

import mechanicalsoup
import time
import smtplib, ssl
from random import randrange

# Personalized config file:
from Constants import *


url="https://egov.uscis.gov/casestatus/landing.do"
browserms = mechanicalsoup.StatefulBrowser()


list = names.keys()


email_text='''Subject: My USCIS Case Status\n\n'''

for MSC in list:
    print(names[MSC], "-", MSC, ":")
    email_text=email_text + names[MSC] + "-" + MSC + ":" + "\n"
    time.sleep(1)



    browserms.open(url)

    browserms.select_form()
    browserms.get_current_page()

    search_term=MSC
    browserms["appReceiptNum"]=search_term


    response=browserms.submit_selected()

    # once the form is submitted, due to redirect, the url in the object changes now
    new_url=browserms.get_url()
    
    #print("new_url: ", new_url)
    browserms.open(new_url)
    page=browserms.get_current_page()


    #response.soup is the whole HTML of the page
    type(response.soup)



    tag=response.soup.select("form")

    textbs_resultobject=response.soup.find_all('div', class_='rows text-center')

    for textbs in textbs_resultobject:
        print(textbs.text)
        email_text=email_text + textbs.text + "\n\n"

    time.sleep(randrange(10))

print("################################################")
print(email_text)



context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_emails, email_text)
    server.quit
