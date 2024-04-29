def find_6(list1):
    for i in list1:
        if i == 6:
            print(f"Списокта 6 саны бар")
            return 
    print("Списокта 6 саны жоқ")
    return 
list1 = [1,10,8,9,6,7,2,3,1,0]
find_6(list1)

def find_6(list1):
    index = 0
    for item in list1:
        if item == 6:
            return "6 знаходиться в индексе:", index
        index += 1
    return "6 не найдено"
    
print(find_6(list1=[5,8,8,5,8,9,5,4,6,5,1,7]))
