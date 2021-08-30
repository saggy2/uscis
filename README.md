# uscis
USCIS related scripts

# First Script:
- uscis-case-status-mailer.py

# Howto
 - Configure/Create application password in yahoo mail for sending emails. You could use any other smtp email system. 
 - Create Constants.py file with content like this below 'names' is a python dictionary with MSC/TSC etc file numbers and names/Forms of your family/friends.
 - Place Email server details and credentials in in Constants.py file accordingly (format below)
 
 

# File Constants.py:
    names={"MSC2120640168": "Ramesh_I-485J", "MSC2190312345": "Ramesh_I-485",
           "MSC2190312346": "Rita_I-485",
          "MSC2190312347": "Terri_I-485"  }

    #The email configuration
    port = 587  # For starttls
    smtp_server = "smtp.mail.yahoo.com"
    sender_email = "senders-email-addr43@yahoo.com"
    receiver_emails = ["receiver1-email-fdfrd@gmail.com", "receiver2-email-hwtdf@gmail.com"]
    password = "fdfgjrsaswdfsrtg"
