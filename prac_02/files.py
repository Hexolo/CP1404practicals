# 1.
user_name = input("Please enter your name: ")
out_file = open("name.txt", "w")
in_file = open("name.txt", "r")
print(f"Your name is {user_name}", file=out_file)
out_file.close()
# 2.
in_file = open("name.txt", "r")
print(in_file.readline())
in_file.close()
# 3.
number_file = open("numbers.txt", "r")
first_line = int(number_file.readline())
second_line= int(number_file.readline())
total = first_line + second_line
print(total)
number_file.close()
# 4.
total = []
ask_file = input("Please enter text file: ")
temp_file = open(ask_file,"r")
for line in temp_file:
    number = int(line)
    total.append(number)
print(sum(total))
temp_file.close()