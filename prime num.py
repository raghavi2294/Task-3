list_1 = [10,501,22,37,100,999,87,351]
prime_list = []
for data in list_1:
    if data%1 == 0:
        prime_list.append(data)
        print("prime num are:",prime_list)