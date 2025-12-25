import time
print("Water intake reminder ")
def set_goal():
 daily_water_goal = int(input("Enter your daily water goal(ml):"))
 return daily_water_goal
def water_intake(intake,daily_water_goal):
        amount = int(input("Enter amount(ml): "))
        intake.append(amount)
        sum = print(f"{amount}/{daily_water_goal}")
      
def progress(daily_water_goal,intake):
        total_intake = sum(intake)
        percentage = (total_intake/daily_water_goal )* 100
        print(f"total intake: {total_intake}")
        print(f"percentage:{percentage}")
def reminder_system():
     x = int(input("How many reminders do you want?"))
     y = int(input("How long do you want the duration to be?"))
     for i in range(x):
          print("Time to drink water")
          time.sleep(y)

def main():     
 daily_water_goal = set_goal() 
 intake = []
 while True:
  print("1.Add water intake \n 2. Show progress \n3. Start reminder system \n 4. Exit ")
  options = (input("Choose an option: "))
  if options == "1":
        water_intake(intake,daily_water_goal)
  elif options == "2":
        progress(daily_water_goal,intake)
  elif options == "4":
      break
  elif options == "3":
       reminder_system()
main()
