# ----------------------------
#  Node & Doubly Linked List
# ----------------------------

class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  
        self.prev = None  


class List:
    """ Circular doubly-linked list implementation """
    
    def __init__(self):        
        self.head = Node(None)
        self.head.next = self.head
        self.head.prev = self.head
        self.n = 0
        
    def get(self, i):
        if i >= self.size(): 
            raise Exception('Index Out of Range')
        x = self.head.next
        for _ in range(i):
            x = x.next
        return x
    
    def insert_after(self, x, data):
        """ Insert a new node after x """
        y = Node(data)
        self.n += 1 
        y.prev = x
        y.next = x.next
        x.next.prev = y
        x.next = y
        return y
        
    def delete(self, x):
        if self.n == 0:
            raise Exception('Linked list is empty')
        self.n -= 1
        x.prev.next = x.next
        x.next.prev = x.prev
        return x
        
    def find(self, val):
        """ Find first node with given value """
        x = self.head.next
        for _ in range(self.size()):
            if x.data == val:
                return x
            x = x.next
        return None
    
    def size(self):
        return self.n
    

# ----------------------------
# Linked List Helper Functions
# ----------------------------

def linkedListToList(linked_list):
    result = []
    current = linked_list.head.next
    while current != linked_list.head:
        result.append(current.data)
        current = current.next
    return result

def listToTheLinkedList(values):
    l = List()
    for val in values:
        l.insert_after(l.head, val)
    return l


# ----------------------------
# Median via BST
# ----------------------------

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insertBST(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insertBST(root.left, value)
    else:
        root.right = insertBST(root.right, value)
    return root

def inorderBST(node):
    return inorderBST(node.left) + [node.value] + inorderBST(node.right) if node else []

def calculateMedian(arr):
    root = None
    for v in arr:
        root = insertBST(root, v)
    sorted_vals = inorderBST(root)

    n = len(sorted_vals)
    if n % 2 == 1:
        return sorted_vals[n // 2]
    return (sorted_vals[n//2 - 1] + sorted_vals[n//2]) / 2

def Calculate_Median(linked_list):
    return calculateMedian(linkedListToList(linked_list))


# ----------------------------
# BST Node for Products
# ----------------------------

class BSTNode:
    def __init__(self, product):
        self.product = product
        self.left = None
        self.right = None


# ----------------------------
# Product BST by name
# ----------------------------

class ProductBST:
    """ BST sorted by product name """

    def __init__(self):
        self.root = None

    def insert(self, product):
        self.root = self._insert(self.root, product)

    def _insert(self, node, product):
        if not node:
            return BSTNode(product)
        if product.productName < node.product.productName:
            node.left = self._insert(node.left, product)
        elif product.productName > node.product.productName:
            node.right = self._insert(node.right, product)
        return node

    def search(self, name):
        return self._search(self.root, name)

    def _search(self, node, name):
        if not node or node.product.productName == name:
            return node
        if name < node.product.productName:
            return self._search(node.left, name)
        return self._search(node.right, name)

    def delete(self, name):
        self.root = self._delete(self.root, name)

    def _delete(self, node, name):
        if not node: 
            return node
        
        # Standard BST delete logic
        if name < node.product.productName:
            node.left = self._delete(node.left, name)
        elif name > node.product.productName:
            node.right = self._delete(node.right, name)
        else:
            if not node.left: return node.right
            if not node.right: return node.left
            temp = self._min(node.right)
            node.product = temp.product
            node.right = self._delete(node.right, temp.product.productName)
        return node

    def _min(self, node):
        while node.left:
            node = node.left
        return node


# ----------------------------
# Price BST
# ----------------------------

class PriceBST:
    """ BST sorted by price """

    def __init__(self):
        self.root = None

    def insert(self, product):
        self.root = self._insert(self.root, product)

    def _insert(self, node, product):
        if not node:
            return BSTNode(product)
        if product.priceOfThisYear < node.product.priceOfThisYear:
            node.left = self._insert(node.left, product)
        else:
            node.right = self._insert(node.right, product)
        return node

    def inOrder(self, node):
        return [] if not node else self.inOrder(node.left) + [node.product] + self.inOrder(node.right)

    def sorted_smallest_price(self):
        for p in self.inOrder(self.root):
            print(p.productName)

    def sorted_biggest_price(self):
        for p in reversed(self.inOrder(self.root)):
            print(p.productName)


# ----------------------------
# Product Class
# ----------------------------

class Product:
    def __init__(self, name, qcode, prices):
        self.productName = name
        self.productQcode = qcode
        self.listOfPrice = listToTheLinkedList(prices)
        self.priceOfThisYear = prices[0]
        self.medianPrice = Calculate_Median(self.listOfPrice)


# ----------------------------
# Product Manager
# ----------------------------

class ProductManager:
    def __init__(self):
        self.products = []
        self.product_bst = ProductBST()
        self.price_bst = PriceBST()

    def add_product(self, product):
        self.products.append(product)
        self.product_bst.insert(product)
        self.price_bst.insert(product)

    def find_product_by_name(self, name):
        node = self.product_bst.search(name)
        return node.product if node else None

    def check_qr_code(self, code):
        return any(p.productQcode == code for p in self.products)


# ----------------------------
# User Interface Functions
# ----------------------------

product_manager = ProductManager()

def AddProduct():
    name = input("Product name: ")
    qcode = input("QR Code: ")

    if product_manager.check_qr_code(qcode):
        print("⚠ QR already exists")
        return

    prices = []
    print("Enter yearly prices (0 to finish):")
    while True:
        p = int(input("Price: "))
        if p == 0: break
        prices.append(p)

    product_manager.add_product(Product(name, qcode, prices))


def AddNewPrice(pname):
    product = product_manager.find_product_by_name(pname)
    if not product:
        print("❌ Product not found")
        return
    newprice = int(input("New price: "))
    product.listOfPrice.insert_after(product.listOfPrice.head, newprice)
    product.medianPrice = Calculate_Median(product.listOfPrice)


# ----------------------------
# Main Menu Loop
# ----------------------------

while True:
    print("\n1 Add product / price\n2 Delete product\n3 Show medians\n4 Smallest prices\n5 Largest prices\n6 Exit")
    c = int(input("> "))

    if c == 1:
        if int(input("1 = Add product, 0 = Add price: ")):
            AddProduct()
        else:
            AddNewPrice(input("Product name: "))
    elif c == 3:
        for p in product_manager.products:
            print(p.productName, "Median:", p.medianPrice)
    elif c == 6:
        break
