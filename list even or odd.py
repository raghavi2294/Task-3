list_1 = [10,501,22,37,100,999,87,351]
even_list = []
odd_list = []
for data in list_1:
    if data%2 == 0:
        even_list.append(data)
    else:
        odd_list.append(data)
        print("Even list:", even_list)
        print("odd List:", odd_list)