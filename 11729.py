input = int(input())


def hanoi(num, start, via, dest):

    if num == 0:
        return
    else:
        hanoi(num-1, start, dest, via)
        print(start, dest)
        hanoi(num-1, via, start, dest)
    # return True


print(2**input-1)
hanoi(input, 1, 2, 3)

# move ( 탑 갯수, 시작점, 이동할 점):
#    move (2, 1, 2) --> 탑 두개를 1에서 2로 이동해라
#       move ( 1, 1, 3)
#          print (1, 3)
#       print (1, 2)
#       move ( 1, 3, 2)
#          print (3, 2)
#    print (시작점, 이동할 점)
#    move (2, 2, 3 ) --> 탑 두개를 2에서 3으로 이동해라
#       move ( 1, 2, 1)
#          print( 2, 1)
#       print (2, 3)
#       move (1, 1, 3)
#          print(1, 3)
