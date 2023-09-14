

customer_list = []

def add_customer(name, surname, id, date):
    customer_list.append(
        {
        "name":name,
        "surname":surname,
        "id":id,
        "date":date,
        }
    )

def del_customer(id):

    for i in range(len(customer_list)):

        if(customer_list[i]["id"]==id):
            customer_list.pop(i)
            break

add_customer("arda","ceviz",1,"12-5-2022")
print(customer_list[0])
add_customer("ardad","ceviz",2,"12-5-2022")
del_customer(1)
print(customer_list[0])

while True:
    choose = int(input("write 1 to add customer \n write 2 to delete customer"))
    if(choose==1):
        print("write name")
        add_customer