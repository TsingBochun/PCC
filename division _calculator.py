
# Using Exceptions to Prevent Crashe
print("Give me two numbers, and I will divede them.")
print("ENTER 'Q' TO QUIT.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break

    answer = int(first_number) / int(second_number)
    print(answer)
