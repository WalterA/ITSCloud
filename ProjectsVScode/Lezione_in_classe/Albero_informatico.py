#log(len(arrey)) liste ordinate per trovare un numero
def binary_search (arrey:list[int],x:int)->int:
    low=0
    high =len(arrey)
    while low<= high:
        mid=(low + high) //2
        if arrey[mid] ==x:
            return mid
        else:
            if x>arrey[mid]:
                low =mid +1
            else:
                high =mid -1
    return None
#arrey.index(x) ricerca l'elemento in lista
#ricorsione
def visit_tree(tree, node):
    print(node)
    left_child, right_child=tree.get(node, [None,None])
    if left_child:
        visit_tree(tree, left_child)
    if right_child:
        visit_tree(tree, right_child)

tree={4:[3,5],3:[2,None],5:[4.5,6]}
print(visit_tree(tree,4))

def visit_tree_interative(tree, root):
    stack=[root]
    while stack:
        curr_node=stack.pop(0)
        print(curr_node)
        left_child, right_child=tree.get(curr_node, [None,None])
        if right_child:
            stack.append(right_child)
        if left_child:
            stack.append(left_child)
visit_tree_interative(tree,4)
