import os
import aspose.words as aw # https://products.aspose.com/words/python-net/conversion/txt-to-html/ 

mailList =[]
# read emails from text file separated by \n
with open('maillist.txt') as f:
    for line in f:
        mailList.append(line.strip())

# get first name from email
def getNames(email): # Was for full names but the emails only use first names so first names 
  print(email) 
  name = ""
  for i in email: # just in case 
    if i == '@':
      break 
    if i == '.':
      break
    if not i.isdigit():      
      name += i

  name = name.title()
  return name

first_names = [] 
for mail in mailList:
    first_names.append(getNames(mail))


# update the HTML file to include name
for i in range(len(mailList)):
  with open('html.txt', 'r', encoding='utf-8') as file:
    data = file.readlines()

  part1 = '<p class="x_EsComm">Dear '
  name = first_names[i] 
  part2 = ',</p>'
  insert = part1 + name + part2

  data[508] = insert  # the name will always be on line 509

  with open('example.txt', 'w', encoding='utf-8') as file: # may be over complicating it with example.txt ... ;;;
    file.writelines(data)

    
  # Convert the text file to html to ship out 
  doc = aw.Document("example.txt")
  doc.save("message.html")

  
  # send emails to users in mailList using linux command
  os.system(
    'sendemail -xu faizan.zafar01@student.csulb.edu -xp YRrC8L37zgbWpdhv -s smtp-relay.sendinblue.com:587 -f es-records@csulb.edu -t '
    + mailList[i] +
    ' -u "Reminder: Update Your Emergency Contacts" -o message-header="From: CSULB Enrollment Services <es-records@csulb.edu>" -o message-header="Importance:High" -o message-content-type=html -o message-file=./message.html'
  )

''' Want to keep the original just in case this messes up @-@

#send emails to users in mailList using linux command
for i in mailList:
    os.system('sendemail -xu faizan.zafar01@student.csulb.edu -xp YRrC8L37zgbWpdhv -s smtp-relay.sendinblue.com:587 -f es-records@csulb.edu -t '+i+' -u "Reminder: Update Your Emergency Contacts" -o message-header="From: CSULB Enrollment Services <es-records@csulb.edu>" -o message-header="Importance:High" -o message-content-type=html -o message-file=./msg.html')


#revert message file to go from name to {name}

'''