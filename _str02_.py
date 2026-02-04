first_name = "German"
last_name = "Titov"
id = "123 123 123"
phone = "050-311NOBODY"

print(f"{first_name}, {last_name} id number: [{id}] phone number: {phone}")

print(len(phone))

# outer execution
print(str.upper(first_name))
# inner execution
print(first_name.upper())