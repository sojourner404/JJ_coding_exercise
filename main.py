import time

status = True

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
  print("A. John changes his attitude towards education and starts taking it seriously.")
  print("B. John continues with the same attitude he had towards education in Spain, without studying or completing any homework.")
  decision = input(
      "What do you think John did?\nPlease pick an option between A or B: ")
  if decision.casefold() == "a":
    print('\n')
    time.sleep(1)
    print("John then proceeded to start secondary school in England and his mentality towards education changed. His grades started to improve and his old habits were disappearing, however, there was one subject that John couldn’t understand but he thought he would be fine because he never experienced failure before. He ended up failing English and was forced to waste a year before starting his level 3 course. It was very painful for him as he saw his secondary school peers going to university when he was on his second year of his level 3 course.  However, that did not demotivate John to do his best and receive an offer from the university he wanted to go to. John managed to meet the requirements of that university. John went through a lot of obstacles that were preventing him from succeeding but he manged to overcome them. On his first day of university, John met James.")
  elif decision.casefold() == "b":
    print("\n")
    time.sleep(1)
    print("John continued with the same mentality he had when he was in Spain and didn’t take his education seriously. Because of that, John was placed on the lower sets in every subject and as expected, his GCSE results were poor. His parents were very disappointed but instead of giving up on him, his parents decided to make his life miserable. John started a level 2 course while resitting his English and mathematics GCSE exam and during that year, John wasn’t aloud to use his phone or watch tv for more than 3 h a day until his grades started to improve.")
  else:
    print("\n")
    print("You've inputted a the wrong option. Program terminating in 2 seconds")
    status = False
    time.sleep(2)
    break

  print("\n")
  print("A. John listens to his parents and takes his education seriously")
  print("B. John continues to disobey his parents and not take his education seriously.")
  decision2 = input(
      "What do you think John did?\nPlease pick an option between A or B: ")
  if decision2.casefold() == "a":
    print('\n')
    time.sleep(1)
    print("John realised that it was a better option to study and receive good grades as it would not only make her parents proud, but it would also be beneficial for him to have a better future. John ended up passing his English and maths GCSE exam as well as the btec level 2 course. He then proceeded to complete a btec level 3 course and even though he struggled at times, he still pushed forward and passed with a great score. After that John went to university and on his first day, he met James.")
  elif decision2.casefold() == "b":
    print('\n')
    time.sleep(1)
    print("John continued to disobey his parents and not take his education seriously despite all the parents’ efforts to change his life for the better. John ended up leaving his parents’ house at the age of 18 and started working in a factory.")
  else:
    print("\n")
    print("You've inputted a the wrong option. Program terminating in 2 seconds")
    status = False
    time.sleep(2)
    break