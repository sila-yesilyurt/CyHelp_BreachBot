#Breach Bot Starter Code
breachYear = 2019

#Greets user
print("Hello! I'm Breach Bot.")
userName = input("What's your name?\n")
print("Nice to meet you " + userName)

#Recounts year of breach
todaysYear = input("What year is it?\n")
timePassed = int(todaysYear) - breachYear
print("Wow! That means it has been " + str(timePassed) + " years since the Facebook breach.")



#Introduces breach
print("Would you like to learn about the Facebook breach?")
giveInfo = input("Type 'yes' or 'no'\n")


#Explains breach
while giveInfo == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) breach details, (b) organization's response, (c) I would like to hear your reflection")
  topic = input()
  
  
  if topic.lower() == "a":
    print("Personal information of 533 million people was taken and published in a low-level hacking forum including phone numbers, Facebook IDs, full names, locations, birthdates, bios, and email addresses. Data was scraped because of a vulnerability that the company patched in 2019.")
  elif topic.lower() == "b":
    print("Facebook fixed the issue, but the organization didn’t give any recommendations to affected users or notify them.")
  elif topic.lower() == "c":
    break
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  input("Press enter to continue\n")

#Introduces my take 
print("\nI'm excited to share my perspective with you. Are you ready to hear my take?")
giveInfo = input("Type 'yes' or 'no'\n")


#Shares my take
while giveInfo == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) relation to the CIA Triad, (b) my reaction, (c) my advice, or (d) none")
  topic = input()
  
  
  if topic.lower() == "a":
    print("This data breach connects to confidentiality because it made personal information publicly available.")
  elif topic.lower() == "b":
    print("We disagree with the organization's response because Facebook should have notified the affected users so they could be cautious against malicious users and be prepared.")
  elif topic.lower() == "c":
    print("I would convince victims to take action by changing their phone number and being cautious with any messages or emails they receive.")
  elif topic.lower() == "d":
    break
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
    input("Press enter to continue\n")
#Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")
