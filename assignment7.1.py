def chop(input_list):
    if len(input_list) >= 2:
        del input_list[0]
        del input_list[-1]
    else:
        input_list.clear()

def middle(input_list):
    if len(input_list) >= 3:
        return input_list[1:-1]
    else:
        return []

my_list = [1, 2, 3, 4]

print("my list before call chop function =>", my_list)
chop(my_list)
print("my list after call chop function =>", my_list)

my_list = [1, 2, 3, 4]

print("\nmy list before call middle function =>", my_list)
new_list = middle(my_list)
print("my list after call middle function =>", my_list)
print("new list after call middle function =>", new_list)
