import os


mailList =[]

with open('maillist.txt') as f:
    for line in f:
        mailList.append(line.strip())

# print(mailList)

for i in mailList:
    os.system(' sendemail -xu faizan.zafar01@student.csulb.edu -xp YRrC8L37zgbWpdhv -s smtp-relay.sendinblue.com:587 -f es-records@csulb.edu -t '+i+' -u "Reminder: Update Your Emergency Contacts" -o message-header="From: CSULB Enrollment Services <es-records@csulb.edu>" -o message-header="Importance:High" -o message-content-type=html -o message-file=./msg.html')