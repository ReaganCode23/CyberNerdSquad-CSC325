"""C-4.14 In the Towers of Hanoi puzzle, we are given a platform with three pegs, a,b, and c, sticking out of it. 
On peg a is a stack of n disks, each larger than the next, so that the smallest is on the top and the largest is on the bottom. 

The puzzle is to move all the disks from peg a to peg c, moving one disk at a time, so that we never place a larger disk on top of a smaller one. ... 

Describe a recursive algorithm for solving the Towers of Hanoi puzzle for arbitrary n.
(Hint: Consider ﬁrst the subproblem of moving all but the nth disk from peg a to another peg using the third as “temporary storage.”) another peg using the third as “temporary storage."""

n = 4
pA, pB, pC = [],[],[]

print('DEBUG: pole A from base to height')
for i in range(n):
    pA.append(n-i)
    print(pA[-1])

print('Sorting started')
def move(n=n, src=pA, temp=pB, dest=pC):
    # src is starting pA
    if n>=1:
        # move a n-1 tower (recursive) src -> temp
        move(n-1, src, dest, temp)

        # move the nth disc (atomic)
        dest.append(n)
        print("disk moved:", n)
        src.pop()

        # move a n-1 tower (recursive), temp -> dest
        move(n-1, temp, src, dest)

    # base case: if n=0, stop

#initial call
move()

print('DEBUG: pole C from base to height')
for i in range(n):
    print(pC[i])

