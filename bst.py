class Node:
    def __init__(self,data):
        self.right=self.left= None
        self.data = data

class Bst:

    def insert(self,root,data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                curr = self.insert(root.left,data)
                root.left = curr
            else:
                curr = self.insert(root.right,data)
                root.right = curr
            return root

    def getTreeLevelInorder(self,root):
        queue = [root]
        tree = []
        while len(queue) != 0:
            cur = queue[0]
            queue = queue[1:]
            #print("{}".format(cur.data), end=" ")
            tree.append(cur.data)
            if cur.left != None:
                queue.append(cur.left)
            if cur.right != None:
                queue.append(cur.right)
        
        return tree

arr = [3,5,4,7,2,1]
MyTree = Bst()
root = None
for i in arr:
    root = MyTree.insert(root,i)
    
doc = MyTree.getTreeLevelInorder(root)
print(doc)