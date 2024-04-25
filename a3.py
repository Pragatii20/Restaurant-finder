# Class Node to create node of a balanced binary search tree
class Node():
    def __init__(self,node):
        self.key  = node  #Key
        self.left = None  #Left Child
        self.right = None #Right Child
        self.parent = None #Parent of Node
        self.y_subtree = None # y subtree of the node (y sorted BST of the subtree of that node including itself)
# Converts a sorted list into its binary search tree        
def binarysearchtree(list):
    # if List is empty, BST is Null
    if  len(list) == 0:
        return None
    else:
        midpoint = (len(list))//2
        node = Node(list[midpoint])
        node.left = binarysearchtree(list[:midpoint])
        if node.left != None:
            node.left.parent = node
        node.right = binarysearchtree(list[midpoint+1:])
        if node.right != None:
            node.right.parent = node
    return node # Returns BST in form of Root as class Node

# Key to sort list in y
def y_key(tuple):
    return tuple[1]

# Creates y subtree of each node and assign it to the respective node
def y_subtree(node,y):
    # base case : if only one element left in the tree
    if len(y) == 1:
        node.y_subtree = Node(y[0])
    else:
        if node != None:
            node.y_subtree = binarysearchtree(y)
            y_left = []
            y_right = []
            for i in range (0,len(y)):
                if y[i][0] < node.key[0]:
                    y_left.append(y[i])
                elif y[i][0] > node.key[0]:
                    y_right.append(y[i])
            if node.left != None:
                y_subtree(node.left,y_left)
            if node.right != None:
                y_subtree(node.right,y_right)
    return node

# prints preoder traversal of BST        
def preorder(root):
    if root == None:
        return
    print(root.key)
    preorder(root.left)
    preorder(root.right)

# Return a list which contains all the node in  BST as preoder traversal
def preorder_node(root,ans):
    if root == None:
        return ans
    ans.append(root)
    preorder_node(root.left,ans)
    preorder_node(root.right,ans)
    return ans

# Return a list which contains all the node in  BST as preoder traversal
def preorder_1d(root):
    ans = []
    answer = preorder_node(root,ans)
    return answer

# Finds the maximum node less than a given value 'value'
def fin_max(node,value,x_or_y,max):
    if node != None:
        if node.key[x_or_y]< value:
            if max == None or node.key[x_or_y] > max.key[x_or_y]  :
                max = node
            if node.right != None:
                    return fin_max(node.right,value,x_or_y,max)
            else:
                return max
        else:
            if node.left != None:
                return fin_max(node.left,value,x_or_y,max)
            else:
                return max
    else:
        return None
# Finds the maximum node less than a given value 'value'
def find_max(node,value,x_or_y):
    max = None
    ans = fin_max(node,value,x_or_y,max)
    if ans != None:
        return (ans.key,ans)
    else:
        return None

# Finds the minimum node greater than a given value 'value'
def fin_min(node,value,x_or_y,min):
    if node != None:
        if node.key[x_or_y] > value:
            if min == None or node.key[x_or_y] < min.key[x_or_y]  :
                min = node
            if node.left != None:
                    return fin_min(node.left,value,x_or_y,min)
            else:
                return min
        else:
            if node.right != None:
                return fin_min(node.right,value,x_or_y,min)
            else:
                return min
    else:
        return None

# Finds the minimum node greater than a given value 'value'
def find_min(node,value,x_or_y):
    min = None
    ans = fin_min(node,value,x_or_y,min)
    if ans != None:
        return (ans.key,ans)
    else:
        return None
# Finds the height of node in the BST if it is present in the bst
def fin_height(tree,node,x_or_y,height):
    if node != None:
        if node.key[x_or_y] < tree.key[x_or_y]:
            height += 1
            return fin_height(tree.left,node,x_or_y,height)
        elif node.key[x_or_y] > tree.key[x_or_y]:
            height +=1
            return fin_height(tree.right,node,x_or_y,height)
        else:
            return height 
    else:
        return None
# Finds the height of node in the BST if it is present in the bst
def find_height(tree,node,x_or_y):
    height = 1
    ans = fin_height(tree,node,x_or_y,height)
    return ans

# Finds the Node which is the first common ancestor of the given two nodes in a BST
def v_split(node_1,node_2,bst,x_or_y):
    height_1 = find_height(bst,node_1,x_or_y)
    height_2 = find_height(bst,node_2,x_or_y)
    while height_1 != height_2:
        if height_1 < height_2:
            node_2 = node_2.parent
            height_2 -= 1
        else:
            node_1 = node_1.parent
            height_1 -= 1
    while node_1 != node_2:
        node_1 = node_1.parent
        node_2 = node_2.parent
    return node_1

# given a BST and min and max value returns all the nodes in the BST whose key is between the range of min and max
def one_d_search(bst,min,max,x_or_y):
    ans_list = []
    node_min = find_min(bst,min,x_or_y)
    node_max = find_max(bst,max,x_or_y)
    
    if node_min != None and node_max != None:
        node_min = node_min[1]
        node_max = node_max[1]
    # Start from the first common ancestor(split)
        if node_min.key[x_or_y] > node_max.key[x_or_y]:
            return ans_list

        split = v_split(node_min,node_max,bst,x_or_y)
        ans_list.append(split)
    # Find valid nodes in left subtree of the split
        node = split.left
        if node != None:
            while node != node_min:
                if node.key[x_or_y] > node_min.key[x_or_y]:
                    ans_list.append(node)
                    node_right_subtree = preorder_1d(node.right)
                    ans_list = ans_list + node_right_subtree
                    node = node.left
                    if node == None:
                        break
                elif node.key[x_or_y] < node_min.key[x_or_y]:
                    node = node.right
                    if node == None:
                        break
                else:
                    ans_list.append(node)
            if node != None:
                ans_list.append(node)
                node_right_subtree = preorder_1d(node.right)
                ans_list = ans_list + node_right_subtree
    # Find valid nodes in right subtree of the split    
        node = split.right
        if node != None:
            while node != node_max:
                if node.key[x_or_y] < node_max.key[x_or_y]:
                    ans_list.append(node)
                    node_left_subtree = preorder_1d(node.left)
                    ans_list = ans_list + node_left_subtree
                    node = node.right
                    if node == None:
                        break
                elif node.key[x_or_y] > node_max.key[x_or_y]:
                    node = node.left
                    if node == None:
                        break
                else:
                    ans_list.append(node)
            if node != None:
                ans_list.append(node)
                node_left_subtree = preorder_1d(node.left)
                ans_list = ans_list + node_left_subtree
        
        return ans_list
    else:
        return ans_list



# Give a BST with y subtree stored in their respective nodes returns a list which contains all the nodes which are within the range of minimum and maximum range of x and y respectively
def two_d_search(bst,min_x,max_x,min_y,max_y):
    ans_list = []
    node_min = find_min(bst,min_x,0)
    node_max = find_max(bst,max_x,0)
    if node_min != None and node_max != None:
        node_min = node_min[1]
        node_max = node_max[1]
    
        if node_min.key[0] > node_max.key[0]:
            return ans_list
    # Start from the first common ancestor(split)
        split = v_split(node_min,node_max,bst,0)
        if split.key[1] > min_y and split.key[1] < max_y:
            ans_list.append(split)
    # Find valid nodes in left subtree of the split    
        node = split.left
        if node != None:
            while node != node_min:
                if node.key[0] > node_min.key[0]:
                    if node.key[1] > min_y and node.key[1] < max_y:
                        ans_list.append(node)
                    if node.right != None:
                        node_right_subtree = one_d_search(node.right.y_subtree,min_y,max_y,1)
                        ans_list = ans_list + node_right_subtree
                    node = node.left
                    if node == None:
                        break
                elif node.key[0] < node_min.key[0]:
                    node = node.right
                    if node == None:
                        break
                else:
                    if node.key[1] > min_y and node.key[1] < max_y:
                        ans_list.append(node)
            if node != None:
                if node.key[1] > min_y and node.key[1] < max_y:
                        ans_list.append(node)
                if node.right != None:
                    node_right_subtree = one_d_search(node.right.y_subtree,min_y,max_y,1)
                    ans_list = ans_list + node_right_subtree
    # Find valid nodes in right subtree of the split    
        node = split.right
        if node != None:
            while node != node_max:
                if node.key[0] < node_max.key[0]:
                    if node.key[1] > min_y and node.key[1] < max_y:
                        ans_list.append(node)
                    if node.left != None:
                        node_left_subtree = one_d_search(node.left.y_subtree,min_y,max_y,1)
                        ans_list = ans_list + node_left_subtree
                    node = node.right
                    if node == None:
                        break
                elif node.key[0] > node_max.key[0]:
                    node = node.left
                    if node == None:
                        break
                else:
                    if node.key[1] > min_y and node.key[1] < max_y:
                        ans_list.append(node)
            if node != None:
                if node.key[1] > min_y and node.key[1] < max_y:
                        ans_list.append(node)
                if node.left != None:
                    node_left_subtree = one_d_search(node.left.y_subtree,min_y,max_y,1)
                    ans_list = ans_list + node_left_subtree
        
        return ans_list
    else:
        return ans_list

# Given a list of nodes returns a list containing the keys of all the nodes present in the input list
def node_to_key(list):
    ans = []
    for i in range(0,len(list)):
        ans.append(list[i].key)
    return ans

# Class PointDatabase according to the assignment which creates the required Database in __init__ method
class PointDatabase():
    def __init__(self, pointlist):
        self.pointlist = pointlist
        pointlist.sort()
        self.pointlist = pointlist # List of pointlist sorted in x
        y = pointlist.copy()
        y.sort(key=y_key) # List of pointlist sorted in y
        x_tree = binarysearchtree(self.pointlist)  # Creates BST of the list
        rangetree = y_subtree(x_tree,y) # assigns y subtree to all the nodes of BST 
        self.rangetree = rangetree # final Data Structure
    # method which, given a point q and distance d, returns the list of all points in valid range of the searchquery given
    def searchNearby(self,q,d):
        output_2d = two_d_search(self.rangetree,q[0]-d,q[0]+d,q[1]-d,q[1]+d)
        return node_to_key(output_2d) # output list

