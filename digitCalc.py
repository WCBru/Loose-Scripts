def digitCalc():
  """Calculates and prints the checksum digit of a UQ ID
  Takes no parameters, instead raw inputs are taken
  Accepts 7 digits, or an 's' preceeding 7 digits
  Prints the output as a str

  Takes no arguments and returns None
  """
  raw = input("Please input a user name or the 7 digits of the username: ")
  base = 0 #Starting number
  if raw[0] == 's': #If 1st letter S
    base += 1  #Skip 1st Letter
  try:
    int(raw[base:]) #Exit if not all numbers
    if len(raw[base:]) != 7: #7 letters are not given
      print('Error: invalid username length')
    else:
      tot = 0 #Running total
      count = 0 #nth digit
      for i in raw[base:]: #For each digit
        tot += int(i) * (11-(2**((count%3)+1))) #Algotithm
        count += 1 #Next digit
      print("Last digit is: " + str(tot%10)) #give last digit
  except ValueError:
    print('Error: invalid username')
  
  x = input("Press enter to end")

digitCalc()
