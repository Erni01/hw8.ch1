
"""
@Makers
Backstory: Usain Bolt, you, and Aybek
had a race. Surprisingly, Usain bolt won.
You came in 2nd and Aybek came in 3rd :(.
Can you think of a way to write a function 
that given a person's name, returns his/her place?
ALSO
Can you think of a way to write a function 
that given a place, returns his/her name?
WRITE 2 FUNCTIONS
One that converts choice to number
and
One that converts number to choice.
"""
#Make sure to un-comment the code test line
#all the way below when you are done.
#Remember to name your function correctly.

def choice_to_number(choice):  
  if choice == "Usain":
    return 1
  elif choice == "Me":
    return 2
  elif choice == "Aybek":
    return 3

# If choice is Usain you should get back 1.

def number_to_choice(number):
      if number == 1:
          return "Usain"
      elif number == 2:
          return "Me"
      elif number == 3:
          return "Aybek"

"""Convert number to choice."""
# if number is 1 then return usain bolt.
#DO NOT remove lines below here,
#this is designed to test your code.
def test_choice_to_number():
  assert choice_to_number('Usain') == 1
  assert choice_to_number('Me') == 2
  assert choice_to_number('Aybek') == 3

def test_number_to_choice():
  assert number_to_choice(1) == 'Usain'
  assert number_to_choice(2) == 'Me'
  assert number_to_choice(3) == 'Aybek'

def test_all():
  try:
    test_choice_to_number()
    test_number_to_choice()

  except AssertionError:
    print("wrong")

  else:
    print("success")
#test your code by un-commenting the line(s) below
test_all()