import time

status = True
y="Yes"
n="No"
while status:
  print("\n")
  print("Welcome to the story of John and James. This will be an interactive program, Please pay attention and pick an option of your choice..")
  welcome = input("To proceed, please any 'key' or 'No (n)' to cancel: ")
  
  # If the user decides to cencel and not proceed
  if welcome.casefold() == "no" or welcome.casefold() == "n":
    time.sleep(1)
    print("We're sorry to see you go. I hope you come back some other time and enjoy the story we prepared. Thank you ")
    status = False
    time.sleep(1)
    break
  
  print("You've decided to proceed. Sit back relax and enjoy the story")
  time.sleep(1)
  print("\n")
  print("This is the story of John and James, two people who came from two different countries and became friends at a university in England.\nThis story will explore who they are and the struggles they went through before they managed to get to university.\nJohn is 19-year-old student who was born in Spain but his parents are Nigerian.\nWhen John started primary school, his grades were amazing and he would always get home from school with a smile on his face but when he got to year 9, everything changed.\nHis grades kept going lower and lower and he would come home sad or angry.\nThe main reason was because he kept getting bullied because of his race.\nHe would always get into fights and get in trouble for it. The second reason why his grades were getting worse was because he lost the motivation to study.\nHe didn’t care about his grades as he gradually stopped doing his homework and study for exams. All he wanted to do is go out with friends and watch tv all day. However, he did manage to finish primary school without failing. When he got to secondary school, his whole life changed. People became more friendly towards him and even the people who used to bully him and be racist towards him changed.\nThat caused John to change his view towards people and he started taking a different approach when dealing with people who were racist towards him.\nHowever, the only thing that John didn’t change was his habits regarding education. His grades were still getting worse. It got the point where he failed most of the subjects. Thankfully, Spain had system in place that gave students the opportunity to gain a pass on failed subjects and John managed to pass all of them. When John finished year 7, he moved to England and instead of starting from year 8, John was told to start from year 9.\nThe reason is because in Spain there is only 4 years in secondary school. ")
  print("\n")

  proceed = input("Press any key to proceed or 'No (n)' to cancel: ")
  # If the user decides to cencel and not proceed
  if proceed.casefold() == "no" or proceed.casefold() == "n":
    time.sleep(1)
    print("Thank you for participating.")
    status = False
    time.sleep(1)
    break

  print("\n")
  decision = input(
      "What do you think John did? \n\nA. John changes his attitude towards education and starts taking it seriously. \nB. John continues with the same attitude he had towards education in Spain, without studying or completing any homework.")
