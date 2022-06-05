#!/usr/bin/python3
import sys
import smtplib
# smtp (smtplib) is only for sending emails if you want to read email you must use imap or pop3
import easyimap as e
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-t","--target",help="Target to attack...")
parser.add_argument("-r","--remove",help="Target remove confirmation from complete list...")
parser.add_argument("-s","--refresh",help="Frefreshing the Instance...")
args = parser.parse_args()
if args.target != None:
    target = args.target
else:
    target = "state"
## removing target from topush list
## getting credentials 
f = open('/etc/creds.config','r')
line = f.readlines()
i = 0
for l in line:
     data = l.strip().split(":")
     #print(data[1])
     #print(l)
     if i == 0:
         jarvis = data[1]
         jarvis_pass = data[2]
     elif i == 1:
         bughunter = data[1]
         bughunter_pass = data[2]
     elif i == 2:
         bucket = data[2]
     elif i == 3:
         access_key = data[1]
         secret_key = data[2]
     else:
       print("its done")
       break
     i = i + 1
"""
input="/creds.cofig"
i=0
jarvis=""
jarvis_pass=""
bughunter=""
bughunter_pass=""
bucket=""
access_key=""
secret_key=""
while read -r line
do 
IFS=":"
read -a strarr <<< $line
#echo ${strarr[0]}
#echo ${strarr[2]}
if [[ $i == 0 ]];then 
jarvis=${strarr[1]}
jarvis_pass=${strarr[2]}
elif [[ $i == 1 ]];then
bughunter=${strarr[1]}
bughunter_pass=${strarr[2]}
elif [[ $i == 2 ]];then
bucket=${strarr[2]}
elif [[ $i == 3 ]];then
access_key=${strarr[1]}
secret_key=${strarr[2]}
else
echo "THIS IS NOT Required"
fi
#echo $line
i=$((i +1))
#echo "i is  $i"
done < $input
"""
####################################################
usermail = bughunter
password = bughunter_pass
tomail = jarvis
msub = "SubHunt=>"+target
msubremove = "CompletedRemove=>"+target
msubremovep = "PendingRemove=>"+target
msubrefresh = "Refresh=>refresh"
mbody = str(target).strip()
# sending email
def send_email():
      if args.refresh == "yes":
        server = smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.login(usermail,password)
        mhead = ['From:%s' % usermail, 'To:%s' %  tomail ,'Subject:%s' % msubrefresh]
        smsg = "\r\n\r\n".join(['\r\n'.join(mhead), mbody])
        server.sendmail(usermail, tomail, smsg)
        #server.listids()
        server.quit()
      if args.remove == None and args.refresh != "yes":
        server = smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.login(usermail,password)
        mhead = ['From:%s' % usermail, 'To:%s' %  tomail ,'Subject:%s' % msub]
        smsg = "\r\n\r\n".join(['\r\n'.join(mhead), mbody])
        server.sendmail(usermail, tomail, smsg)
        #server.listids()
        server.quit()
      else:
        server = smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.login(usermail,password)
        mhead = ['From:%s' % usermail, 'To:%s' %  tomail ,'Subject:%s' % msubremove]
        smsg = "\r\n\r\n".join(['\r\n'.join(mhead), mbody])
        server.sendmail(usermail, tomail, smsg)
        #server.listids()
        server.quit()
        server = smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.login(usermail,password)
        mhead = ['From:%s' % usermail, 'To:%s' %  tomail ,'Subject:%s' % msubremovep]
        smsg = "\r\n\r\n".join(['\r\n'.join(mhead), mbody])
        server.sendmail(usermail, tomail, smsg)
        #server.listids()
        server.quit()
send_email()
f = open('pull.txt','a')
f.write(target)
f.close()
