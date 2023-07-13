some_list = []
some_list_length = 0

while some_list_length < 10:
    new_input = input(">>>")
    some_list.append(new_input)
    some_list_length += 1

print("; ".join(some_list))