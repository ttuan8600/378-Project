import os

mailList =[]
# read emails from text file separated by \n
# with open('facultyList.txt') as f:
with open('testlist.txt') as f:
    for line in f:
        mailList.append(line.strip())

# get first name from email
def getNames(email):
  name = ""
  for i in range(len(email)):
    if email[i] == '@' or email[i] == '.' or str(email[i]).isupper() and i > 0:
      break
    if not email[i].isdigit():
      name += email[i]

  name = name.title()
  return name

first_names = [] 
for mail in mailList:
    first_names.append(getNames(mail))


# update the HTML file to include name
for i in range(len(mailList)):
  # with open('message.html', 'r', encoding='utf-8') as file:
  #   data = file.readlines()
  with open('withdrawal.html', 'r') as file :
    filedata = file.read()

# Replace the target string
  filedata = filedata.replace('name', first_names[i])

# Write the file out again
  with open('message2.html', 'w') as file:
    file.write(filedata)
 
  os.system('sendemail -xu faizan.zafar01@student.csulb.edu -xp YRrC8L37zgbWpdhv -s smtp-relay.sendinblue.com:587 -f es-records@csulb.edu -t '+ mailList[i] + ' -u "Action Required: Pending Worklist Requests" -o message-header="From: CSULB Enrollment Services <es-records@csulb.edu>"  -o message-content-type=html -o message-file=./message2.html')



''' Want to keep the original just in case this messes up @-@

#send emails to users in mailList using linux command
for i in mailList:
    os.system('sendemail -xu faizan.zafar01@student.csulb.edu -xp YRrC8L37zgbWpdhv -s smtp-relay.sendinblue.com:587 -f es-records@csulb.edu -t '+i+' -u "Reminder: Update Your Emergency Contacts" -o message-header="From: CSULB Enrollment Services <es-records@csulb.edu>" -o message-header="Importance:High" -o message-content-type=html -o message-file=./msg.html')


#revert message file to go from name to {name}

'''