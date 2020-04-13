import numpy as np

print("Player 1 will get 'x' as a mark and Player 2 will get 'o' as a mark.")
X= 'x'
Y= 'o'
n=0
mark_array=np.empty(shape=[0,9], dtype=object)
for i in range(0,9):
    n+=1
    mark_array=np.append(mark_array, n)

main_arr=mark_array.reshape(3,3)
print(main_arr)

ip1_stack=np.empty(shape=[0, 6])
ip2_stack=np.empty(shape=[0, 5])

for i in range(0,9):
    ip_p1=int(input("P1 Enter position From 1 to 9: "))
    while ip_p1 > 9 or ip_p1== 0:
        ip_p1=int(input("P1 Enter position From 1 to 9: "))
    else:
        sec_arr=np.place(main_arr, main_arr==ip_p1, X)
    print(main_arr)
    ip1_stack=np.append(ip1_stack, ip_p1)

    if ip1_stack.size==5:
        print("Game over, Better Luck next time...!")
        break


    if main_arr.item(0)==main_arr.item(1)==main_arr.item(2)==X:
        print("Player 1 won......!")
        break
    elif main_arr.item(3)==main_arr.item(4)==main_arr.item(5)==X:
        print("Player 1 won......!")
        break
    elif main_arr.item(6)==main_arr.item(7)==main_arr.item(8)==X:
        print("Player 1 won......!")
        break
    elif main_arr.item(0)==main_arr.item(4)==main_arr.item(8)==X:
        print("Player 1 won......!")
        break
    elif main_arr.item(2)==main_arr.item(4)==main_arr.item(6)==X:
        print("Player 1 won......!")
        break
    elif main_arr.item(0)==main_arr.item(3)==main_arr.item(6)==X:
        print("Player 1 won......!")
        break
    elif main_arr.item(1)==main_arr.item(4)==main_arr.item(7)==X:
        print("Player 1 won......!")
        break
    elif main_arr.item(2)==main_arr.item(5)==main_arr.item(8)==X:
        print("Player 1 won......!")
        break
        print(main_arr)

    ip_p2=int(input("P2 Enter position From 1 to 9: "))
    while ip_p2 > 9 or ip_p2== 0:
        ip_p2=int(input("P2 Enter position From 1 to 9: "))

    while ip_p1==ip_p2:
        print("Please Enter other value from 1 to 9: ")
        ip_p2=int(input("P2 Enter position From 1 to 9: "))
        arr5=np.place(main_arr, main_arr==ip_p2, Y)
    else:
        arr5=np.place(main_arr, main_arr==ip_p2, Y)

    print(main_arr)
    ip2_stack=np.append(ip2_stack, ip_p2)


    if main_arr.item(0)==main_arr.item(1)==main_arr.item(2)==Y:
        print("Player 2 won......!")
        break
    elif main_arr.item(3)==main_arr.item(4)==main_arr.item(5)==Y:
        print("Player 2 won......!")
        break
    elif main_arr.item(6)==main_arr.item(7)==main_arr.item(8)==Y:
        print("Player 2 won......!")
        break
    elif main_arr.item(0)==main_arr.item(4)==main_arr.item(8)==Y:
        print("Player 2 won......!")
        break
    elif main_arr.item(2)==main_arr.item(4)==main_arr.item(6)==Y:
        print("Player 2 won......!")
        break
    elif main_arr.item(0)==main_arr.item(3)==main_arr.item(6)==Y:
        print("Player 2 won......!")
        break
    elif main_arr.item(1)==main_arr.item(4)==main_arr.item(7)==Y:
        print("Player 2 won......!")
        break
    elif main_arr.item(2)==main_arr.item(5)==main_arr.item(8)==Y:
        print("Player 2 won......!")
        break
        print(main_arr)



