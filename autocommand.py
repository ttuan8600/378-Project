import os


mailList =[]
#read emails from text file separated by \n
with open('maillist.txt') as f:
    for line in f:
        mailList.append(line.strip())

# get first name from email
def getNames(email): # Was for full names but the emails only use first names so first names 
  print(email) 
  name = ""
  for i in email:
    #if i == '@':
    #  break 
    if i == '.':
      break
    if not i.isdigit():      
      name += i

  name = name.title()
  return name

first_names = [] 
for mail in mailList:
    first_names.append(getNames(mail))


#update the mes.html file to include name

#send emails to users in mailList using linux command
for i in mailList:
    os.system('sendemail -xu faizan.zafar01@student.csulb.edu -xp YRrC8L37zgbWpdhv -s smtp-relay.sendinblue.com:587 -f es-records@csulb.edu -t '+i+' -u "Reminder: Update Your Emergency Contacts" -o message-header="From: CSULB Enrollment Services <es-records@csulb.edu>" -o message-header="Importance:High" -o message-content-type=html -o message-file=./msg.html')


#revert message file to go from name to {name}