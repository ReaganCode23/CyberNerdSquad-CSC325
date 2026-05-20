
def preorder(T, n):
    ''' node, left, right '''
    if n >= len(T):
        return
    if T[n] is None:
        return

    print(T[n], end=" ")
    preorder(T, 2*n + 1)
    preorder(T, 2*n + 2)

def postorder(T, n):
    ''' left, right, node '''
    if n >= len(T):
        return
    if T[n] is None:
        return

    postorder(T, 2*n + 1)
    postorder(T, 2*n + 2)
    print(T[n], end=" ")

def inorder(T, n):
    ''' left, node, right '''
    if n >= len(T):
        return
    if T[n] is None:
        return

    inorder(T, 2*n + 1)
    print(T[n], end=" ")
    inorder(T, 2*n + 2)

def eulertour(T, n):
    ''' node, left, node, right, node '''
    if n >= len(T):
        return
    if T[n] is None:
        return

    left = 2*n + 1
    right = 2*n + 2

    print(T[n], end=" ")

    if left < len(T) and T[left] is not None:
        eulertour(T, left)
        print(T[n], end=" ")

    if right < len(T) and T[right] is not None:
        eulertour(T, right)
        print(T[n], end=" ")

if __name__ == "__main__":
    T = ['+', '*', '*', '2', '-', '3', '2', None, None, '5', '1']
    print("preorder:")
    preorder(T, 0)
    print("\npostorder:")
    postorder(T, 0)
    print("\ninorder:")
    inorder(T, 0)
    print("\neuler tour:")
    eulertour(T, 0)

'''
Expected output:
preorder:
+ * 2 - 5 1 * 3 2
postorder:
2 5 1 - * 3 2 * +
inorder:
2 * 5 - 1 + 3 * 2
euler tour:
+ * 2 * - 5 - 1 - * + * 3 * 2 * +
'''
