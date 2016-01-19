### script to check and send  by email date expiration of domain's name

import os, sys

## Use smtplib to send mail on mailbox admin
import smtplib 
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


##use whois to check information about names
import whois

##use datetime to check and manipulate date 
from datetime import date, datetime, timedelta

domains = ['FQDN','FQDN', 'FQDN']   ## get your domain's name here
for names in   (domains):                 ##ask from whois
   w = whois.whois((names))		 ##and get expiration date
   date = w.expiration_date[1]           ## list the date from whois
   date_limit = ((w.expiration_date[1])-timedelta(days=30))   ## get a timedelta less 30 days than expiration date final 
   if (datetime.today()) < date_limit:                           ## compare expiration date from now and the date limit      
       pass
   else:               
       msg = MIMEMultipart()	## send mail to the client or your dashboard mail account
       msg['From'] = 'XXX.mail'
       msg['To'] = 'XXX.maim'
       msg['Subject'] = 'Renew yours domains %s ' % names
       message = " expiration date of your domains i '%s'. Think to renew it." % date
       msg.attach(MIMEText(message))
       mailserver = smtplib.SMTP('smtp.bobiwembley.fr', 587)
       mailserver.ehlo()
       mailserver.starttls()
       mailserver.ehlo()
       mailserver.login('XXX.mail', 'PASSWORD')
       mailserver.sendmail('XXX.mail', 'XXX.mail', msg.as_string())
       mailserver.quit()
