#!/usr/bin/env python3

"""
Game that lets you check how well you know your computer

TODO
[ ] add option for user to see computer spec
[ ] add windows machine
[ ] put on github
[ ] tells user different thing based off of score

"""
import os
import socket 
import shutil
import random
import re
from urllib import response

# check what OS you are running and based off that gather questions and put them in a dictionary
def get_computer_spec():
   computer_spec = {}
   operating_system = os.uname()
   # x = shutil.disk_usage("/").total
   if operating_system.sysname == "Darwin" or "Linux":
      print("I am a linux / mac")
      computer_spec ={
         "operating_system": operating_system.sysname,
         "cpu_architecture": operating_system.machine,
         "computer_name": operating_system.nodename,
         "memory_size": os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES') / (1024**3),
         "size_main_partition": shutil.disk_usage("/").total // (2**30),
         "size_free_main_partition": shutil.disk_usage("/").total // (2**30),
         "cpu_core_count": os.cpu_count(),
         "current_user": os.environ.get('USER'),
         "path": os.environ.get('PATH').split(":"),
         "shell_using": os.environ.get('SHELL')
      }
      if operating_system.sysname == "Linux":
         computer_spec["ip_address"] = socket.gethostbyname_ex(socket.gethostname())[2][0]
      else:
         computer_spec["ip_address"] = socket.gethostbyname_ex(socket.gethostname())[2][1]

      # print(computer_spec)
   elif operating_system.sysname == "Windows":
      # Will implement when I get a Windows VM running
      print("Windows not implemented, but your on a Windows exiting")
      exit(0)
   else:
      print("I dont know what OS you are running")
      exit(1)
   return computer_spec

# Ask user questions
def user_questions(computer_spec):
   round = 0 
   question_list = list(computer_spec.keys())
   user_score = 0

   while round < 3:
      
      question_number = random.randrange(0, len(question_list))
      question = question_list[question_number]
      answer_raw = computer_spec[question_list[question_number]]
      answer = str(answer_raw)
      # regex pattern
      pattern = ("[A-Za-z0-9]")
      if isinstance(answer_raw, list):
         example = re.sub(pattern, 'x', str(answer_raw[0])) 
      else:
         example = re.sub(pattern, 'x', answer) 

      if isinstance(answer_raw, int or float):
         print(f"question {round + 1}")
         print(f"What is your {question} \n should be in this format {example}" )
         print("answer")
         user_response = input("?  ").strip()
         if answer == user_response:
            user_score = user_score + 1
            print("CORRECT !!! ")
         else:
            print(f"WRONG :( correct answer is: {answer}")
      elif isinstance(answer_raw, list):
         print(f"question {round + 1}")
         print(f"What is your {question} \n should be in this format {example}" )
         print("answer")
         user_response = input("?  ").strip().lower()
         if user_response in answer_raw:
            user_score = user_score + 1
            print("CORRECT !!! ")
         else:
           print(f"WRONG :( correct answer is: {answer}")
      elif isinstance(answer_raw, str):
         print(f"question {round + 1}")
         print(f"What is your {question} \n should be in this format {example}" )
         print("answer")
         user_response = input("?  ").strip().lower()
         if answer.lower() == user_response:
            user_score = user_score + 1
            print("CORRECT !!! ")
         else:
           print(f"WRONG :( correct answer is: {answer}")
      else:
         print(f"something went wrong dont have structured question for {type(question)}")
      round = round +1
   return user_score
      
# Main app that runs the game
def main():
   user_wants_to_play = "yes"

   while user_wants_to_play in ["yes" , "y", "ye", "ya", "yas"]:
      # runs game
      computer_spec = get_computer_spec()
      user_score = user_questions(computer_spec)
      # Scoreboard
      print(f"You got {user_score} correct !!! out of 3")
      # want to play again
      user_wants_to_play = input("Do you want to play again please answer y / yes ").lower()

if __name__ == "__main__":
   main()        