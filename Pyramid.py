def build_pyramid(height):
  """Builds a pyramid of '#' characters."""
  for i in range(1, height + 1):
    print("#" * i)

while True:
  try:
    height = int(input("Enter the height of the pyramid (1-8): "))
    if 1 <= height <= 8:
      build_pyramid(height)
      while True:
        choice = input("1. Play again\n2. Exit\nChoose an option: ")
        if choice == '1':
          break
        elif choice == '2':
          exit()
        else:
          print("Invalid choice. Please enter 1 or 2.")
    else:
      print("Invalid input. Please enter a number between 1 and 8.")
      while True:
        retry_choice = input("1. Try again\n2. Exit\nChoose an option: ")
        if retry_choice == '1':
          break
        elif retry_choice == '2':
          exit()
        else:
          print("Invalid choice. Please enter 1 or 2.")
  except ValueError:
    print("Invalid input. Please enter a number.")
    while True:
      retry_choice = input("1. Try again\n2. Exit\nChoose an option: ")
      if retry_choice == '1':
        break
      elif retry_choice == '2':
          exit()
      else:
        print("Invalid choice. Please enter 1 or 2.")
