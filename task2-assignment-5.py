#list created is my_list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#extracted_list is created with the pre-existing my_list
extracted_list = my_list[0:5]
#reverse_list is created first by coping the extracted_list and reversing it
reverse_list=extracted_list
reverse_list.reverse()
#printout the list
print("original_list: ",my_list)
print("extracted_list:",extracted_list)
print("reversed_list:",reverse_list)
