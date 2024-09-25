def mario_pyramid(height):
  """
  Prints a Mario-style pyramid of '#' characters with the specified height.

  Args:
    height: The height of the pyramid (between 1 and 8).
  """

  if height < 1 or height > 8:
    print("Invalid input. Please enter a height between 1 and 8.")
    while True:
      print("1. Try again")
      print("2. Exit")
      choice = input("Enter your choice: ")
      if choice == '1':
        height = int(input("Enter the height of the pyramid (1-8): "))
        mario_pyramid(height)
        break  # Exit the loop if the user chooses to try again
      elif choice == '2':
        return  # Exit the function if the user chooses to exit
      else:
        print("Invalid choice. Please enter 1 or 2.")
  else:
    for i in range(1, height + 1):
      print(" " * (height - i), end="")
      print("#" * i, end="")
      print("#" * i)

    # Play again or exit after a valid pyramid is printed
    while True:
      print("1. Play again")
      print("2. Exit")
      choice = input("Enter your choice: ")
      if choice == '1':
        height = int(input("Enter the height of the pyramid (1-8): "))
        mario_pyramid(height)
        break
      elif choice == '2':
        return
      else:
        print("Invalid choice. Please enter 1 or 2.")

# Get user input for the pyramid height
while True:
  try:
    height = int(input("Enter the height of the pyramid (1-8): "))
    mario_pyramid(height)
    break  # Exit the loop if a valid height is entered
  except ValueError:
    print("Invalid input. Please enter a number.")

