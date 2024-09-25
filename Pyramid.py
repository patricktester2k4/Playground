def mario_pyramid(height):
  """
  Prints a single-sided Mario-style pyramid of '#' characters with the specified height.

  Args:
    height: The height of the pyramid (between 1 and 8).
  """

  if height < 1 or height > 8:
    print("Invalid input. Please enter a height between 1 and 8.")
    print("1. Input the correct value")
    print("2. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
      height = int(input("Enter the height of the pyramid (1-8): "))
      mario_pyramid(height)
    elif choice == '2':
      return
    else:
      print("Invalid choice.")
      return

  for i in range(1, height + 1):
    print(" " * (height - i), end="")  # Print spaces
    print("#" * i)  # Print '#' characters

# Get user input for the pyramid height
height = int(input("Enter the height of the pyramid (1-8): "))

# Call the function to print the pyramid
mario_pyramid(height)
