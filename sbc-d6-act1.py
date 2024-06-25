user = input("Enter a string: ")
users = user.replace(" ", "").upper()
is_palindrome = True

for i in range(len(users) // 2):
    if users[i] != users[-1 - i]:
        is_palindrome = False
        break

print(f"'{user}' is {'a' if is_palindrome else 'not a'} palindrome.")
