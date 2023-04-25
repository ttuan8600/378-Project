import os

mailList =[]
# read emails from text file separated by \n
with open('maillist.txt') as f:
    for line in f:
        mailList.append(line.strip())


# update the HTML file to include name
for i in range(len(mailList)):
  
  # send emails to users in mailList using linux command
  
  os.system('sendemail -xu faizan.zafar01@student.csulb.edu -xp YRrC8L37zgbWpdhv -s smtp-relay.sendinblue.com:587 -f es-records@csulb.edu -t '+ mailList[i] + ' -u "Warning: Verify Your Account Fees" -o message-header="From: CSULB Enrollment Services <es-records@csulb.edu>" -o message-header="Importance:High" -o message-content-type=html -o message-file=./faculty.html')



''' Want to keep the original just in case this messes up @-@

#send emails to users in mailList using linux command
for i in mailList:
    os.system('sendemail -xu faizan.zafar01@student.csulb.edu -xp YRrC8L37zgbWpdhv -s smtp-relay.sendinblue.com:587 -f es-records@csulb.edu -t '+i+' -u "Reminder: Update Your Emergency Contacts" -o message-header="From: CSULB Enrollment Services <es-records@csulb.edu>" -o message-header="Importance:High" -o message-content-type=html -o message-file=./msg.html')


#revert message file to go from name to {name}

'''