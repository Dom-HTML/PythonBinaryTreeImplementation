class BinTree:
    def __init__(self, nods):
        self.data = self.Stack(nods, len(nods))
        self.root = self.Node(self.data.pop())
        self.nodes = []
        self.cache = self.Cache()
        self.initTree()

    def initTree(self):#initialise tree
        self.nodes.append(self.root)
        for x in range(self.data.len()):
            item = self.data.pop()
            node = self.Node(item)
            nextNode = self.root
            while True:
                if node.data < nextNode.data:
                    if nextNode.left == None:
                        nextNode.left = node
                        node.root = nextNode
                        self.nodes.append(node)
                        break
                    elif not nextNode.left == None:
                        nextNode = nextNode.left
                        continue
                elif node.data >= nextNode.data:
                    if nextNode.right == None:
                        nextNode.right = node
                        node.root = nextNode
                        self.nodes.append(node)
                        break
                    elif not nextNode.right == None:
                        nextNode = nextNode.right
                        continue

    def path(self, value):#func to get path to a node (returns two arrays: numeric & node)
        self.search(value)#inputs: value to path to
        rev = self.cache.store[::-1]
        numArr = [num.data for num in rev]
        path = type("path", (), {"nodes":rev, "numer":numArr})
        return (path)

    def search(self, value):#returns Node class of search value (returns node object)
        self.cache.clear()  #inputs: value to search for
        root = self.root#Note: implement array return if multiple

        if root.data == value:
            return root
        else:
            return self.searchRecur(value, root)

    def searchRecur(self, value, root):#recursion for search func
        if root.left:
            if root.left.data == value:
                return root.left
            else:
                rVal = self.searchRecur(value, root.left)
                self.cache.commit(root.left)
                return rVal

        if root.right:
            if root.right.data == value:
                return root.right
            else:
                rVal = self.searchRecur(value, root.right)
                self.cache.commit(root.right)
                return rVal

        return False

    def add(self, data, root = None):#adds a node to the tree (returns)
        if not root:                 #inputs: data of new node, optional root of branch to add to
            root = self.root

        if str(type(data)) == "<class 'list'>":
            for value in data:
                self.addRecr(value, root)
        else:
            self.addRecr(data, root)

    def addRecr(self, value, root):#recursion for add func
        if value <= root.data:
            if root.left:
                self.addRecr(value, root.left)
            else:
                newNode = self.Node(value)
                newNode.root = root
                root.left = newNode
                self.nodes.append(newNode)
        elif value > root.data:
            if root.right:
                self.addRecr(value, root.right)
            else:
                newNode = self.Node(value)
                newNode.root = root
                root.right = newNode
                self.nodes.append(newNode)
        
    def delete(self, value):#delete func yet to be implemented
        order = self.inOrder()

    def outTree(self):#outputs all node objects in tree in order added (no return)
        for node in self.nodes:
            print(node.__dict__)

    def inOrder(self, index = -1):#outputs the tree in order (returns node array)
        self.cache.clear()        #inputs: optional index of wanted node
        self.inOrderProcess(self.root)
        return self.returnOrder(index)
                
    def preOrder(self, index = -1):#outputs the tree in pre order (returns node array)
        self.cache.clear()         #inputs: optional index of wanted node
        self.preOrderProcess(self.root)
        return self.returnOrder(index)

    def postOrder(self, index = -1):#outputs the tree in post order (returns node array)
        self.cache.clear()          #inputs: optional index of wanted node
        self.postOrderProcess(self.root)
        return self.returnOrder(index)

    def returnOrder(self, index):#returns a single node in the order, if index provided
        if index == -1:          #useful if you want to get the last/first/root node
            return self.cache.store
        else:
            try:
                return self.cache.store[index]
            except IndexError:
                print("Tree Index out of range")
                return self.cache.store

    def inOrderProcess(self, root):#recursion func for inOder
        if root.left:
            if root.left.left or root.left.right:
                self.inOrderProcess(root.left)
            else:
                self.cache.commit(root.left)
        self.cache.commit(root.data)
        if root.right:
            if root.right.left or root.right.right:
                self.inOrderProcess(root.right)
            else:
                self.cache.commit(root.right)

    def preOrderProcess(self, root):#recursion func for preOder
        self.cache.commit(root.data)
        if root.left:
            if root.left.left or root.left.right:
                self.preOrderProcess(root.left)
            else:
                self.cache.commit(root.left)
        if root.right:
            if root.right.left or root.right.right:
                self.preOrderProcess(root.right)
            else:
                self.cache.commit(root.right)

    def postOrderProcess(self, root):#recursion func for postOder
        if root.left:
            if root.left.left or root.left.right:
                self.postOrderProcess(root.left)
            else:
                self.cache.commit(root.left)
        if root.right:
            if root.right.left or root.right.right:
                self.postOrderProcess(root.right)
            else:
                self.cache.commit(root.right)
        self.cache.commit(root.data)

    def leftMost(self, root = False):#returns the left most node of a tree 
        if root == False:            #aka first node in in-order
            root = self.root         #inputs: root of where to get left most

        leftMost = root
        while True:
            cur = leftMost.left
            if cur == None:
                break
            elif not cur == None:
                leftMost = cur

        return leftMost

    def rightMost(self, root = False):#returns the right most node of a tree
        if root == False:             #aka last node in in-order (dk why i made this)
            root = self.root          #inputs: root of where to get right most

        rightMost = root
        while True:
            cur = rightMost.right
            if cur == None:
                break
            elif not cur == None:
                rightMost = cur

        return rightMost

    class Node:#implementation of a node class, stores left/right/root node
        def __init__(self, data):#and the data in the node
            self.data = data
            self.root = None
            self.left = None
            self.right = None       

    class Cache:#implementation of a cache (basically a glorified array) QOL
        def __init__(self):
            self.store = []

        def commit(self, data):
            if str(type(data)) == "<class 'list'>":
                for item in data:
                    self.store.append(item)
            else:
                self.store.append(data)

        def clear(self):
            self.store.clear()

    class Stack:#cause i wanted to, an implementation of a stack
        def __init__(self, args, maxLen):
            self.data = [*args]
            self.maxLen = maxLen
            self.reverse()

        def pop(self):
            if len(self.data) == 0:
                print("Stack Underflow")
            else:
                return self.data.pop()

        def push(self, item):
            if len(self.data) >= int(self.maxLen):
                print("Stack Overflow")
            else:
                self.data.append(item)

        def reverse(self):
            self.data = self.data[::-1]

        def clear(self):
            self.data.clear()

        def len(self):
            return len(self.data)

myNodes = [58, 50,48,30,49,32,31,33,34,58, 1]
myTree = BinTree(myNodes)

result = myTree.search(1)
print(result.data)

ret = myTree.path(1)
for item in ret.numer:
    print(item)
