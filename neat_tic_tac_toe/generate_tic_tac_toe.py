

def test(num, expec_1, exprec_0):
    e1 = 0
    e0 = 0
    for i in range(9):
        if((num >> i) & 1):
            e1 += 1
        else:
            e0 += 1

    if e1 == expec_1 and e0 == exprec_0:
        # print("Test case passed!!")
        return True
    else:
        # print("Test case failed")
        # print(f"e1: {e1} e0: {e0} ==> expec_1: {expec_1} exprec_0: {exprec_0}")
        return False

i= 0; 
 
final_lst = []

# 1--> x 0 --> 0
# generate all the numbers
while(i < 512):
    if test(i, 5,4): 
        final_lst.append(('{:09b}'.format(i), 1,))

    if test(i,4,5):
        final_lst.append(('{:09b}'.format(i),0,))
    i += 1


with open("all_tic_tac_toe", "w") as f:
    for i in range(len(final_lst)):
        f.write(str(final_lst[i][0]) + "," + str(final_lst[i][1]))
        f.write("\n")
