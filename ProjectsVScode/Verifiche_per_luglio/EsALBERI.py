dizio={0:[4], 1:[3,5], 2:[2,4.5,6]}
tree={4:[3,5],3:[2,None],5:[4.5,6],2:[None,None]}
{0:4,1:4,2:4.166}
def media_albero (tree,root)->dict:
    avg_for={}
    nodos={}
    stack=[root,0]
    while stack:
        curr_node, curr_leve=stack.pop(0)
        left_child, right_child=tree.get(curr_node, [None,None])
        if right_child:
            stack.append(right_child, curr_leve+1)
            avg_for[curr_leve]=avg_for.get(curr_leve,0)+ right_child
        if left_child:
            stack.append(left_child, curr_leve+1)
            avg_for[curr_leve]=avg_for.get(curr_leve,0)+ left_child
    for level in avg_for:
        avg_for[level]/= nodos[level]
media_albero(tree,4)