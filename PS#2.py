"""C-4.14 In the Towers of Hanoi puzzle, we are given a platform with three pegs, a,b, and c, sticking out of it. 
On peg a is a stack of n disks, each larger than the next, so that the smallest is on the top and the largest is on the bottom. 

The puzzle is to move all the disks from peg a to peg c, moving one disk at a time, so that we never place a larger disk on top of a smaller one. ... 

Describe a recursive algorithm for solving the Towers of Hanoi puzzle for arbitrary n.
(Hint: Consider ﬁrst the subproblem of moving all but the nth disk from peg a to another peg using the third as “temporary storage.”) another peg using the third as “temporary storage."""

n = 3
pA, pB, pC = [],[],[]

for i in range(n):
    pA.append(n-i)

print('Sorting started')
def move(n=n, src=pA, temp=pB, dest=pC):
    # print poles
    print("pole A from bottom to top")
    for i in range(len(pA)):
        print(pA[i])

    print("pole B from bottom to top")
    for i in range(len(pB)):
        print(pB[i])

    print("pole C from bottom to top")
    for i in range(len(pC)):
        print(pC[i])

    if n == 1:
        dest.append(n)
        print("disk moved:", n)
        src.pop()
    elif n >= 1:
        move(n-1, src, dest, temp)
        dest.append(n)
        print("disk moved:", n)
        src.pop()
        move(n-1, temp, src, dest)
'''
    # August's code:
    if n>=1:
        # move a n-1 tower (recursive) src -> temp
        move(n-1, src, dest, temp)

        # move the nth disc (atomic)
        dest.append(n)
        print("disk moved:", n)
        src.pop()

        # move a n-1 tower (recursive), temp -> dest
        move(n-1, temp, src, dest)
'''

#initial call
move()
# print poles
print("pole A from bottom to top")
for i in range(len(pA)):
    print(pA[i])

print("pole B from bottom to top")
for i in range(len(pB)):
    print(pB[i])

print("pole C from bottom to top")
for i in range(len(pC)):
    print(pC[i])