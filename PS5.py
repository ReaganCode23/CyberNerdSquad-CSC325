
'''C-9.30 Give a nonrecursive implementation of the upheap method for the class HeapPriorityQueue.'''
def upheap(a, i, n)
  #top of heap is i=0
  #parent index is i / 2 int division
  while true:
    if (i/2) > -1 and a[i] > a[i/2]:
      a[i/2], a[i] = a[i], a[i/2]
      i = i/2 
    else:
      return

'''C-9.31 Give a nonrecursive implementation of the downheap method for the class HeapPriorityQueue'''
def downheap(a, i, n):
  #n is heap length
  #a is heap[]
  # i is current index we want to downheap
  new_i = 0

  #unrecursive; adjust index via for loop
  while true:
    #indicies of L and R "children" of n
    L_i, R_i = left(i, n), right(i, n)
    new_i = i

    if L > -1 and a[L_i] > a[R_i]:
      new_i = L_i

    if right_i > -1 and a[R_i] > a[new_i]:
      new_i = R_i 
    # i selected is the next biggest item to swap up, satisfies heap property

    if new_i != i:
      #swap
      a[i], a[new_i] = a[new_i], a[i]
      #next index
      i = new_i
    else: #end iterative loop
      return


'''Show how the input of list [1,2,3,4,5,6] changes after each step (merge, remove_min or remove_max, downheap or upheap) of in-place heapsort. Use array format to show the changes, not the tree format.'''
