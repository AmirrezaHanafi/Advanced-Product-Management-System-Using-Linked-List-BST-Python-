class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  
        self.prev = None  

class List:
    def __init__(self):        
        self.head = Node(None)
        self.head.next = self.head
        self.head.prev = self.head
        self.n = 0
        
    def get(self, ind):
        if ind >= self.size(): 
            raise Exception('Out of list')
        x = self.head
        for i in range(ind):
            x = x.next
        return x
    
    def insert_after(self, x, data):
        y = Node(data)
        self.n += 1 
        y.prev = x
        y.next = x.next
        x.next = y
        y.next.prev = y
        return y
        
    def delete(self, x):
        if self.n == 0:
            raise Exception('Linked list is empty')
        self.n -= 1
        x.prev.next = x.next
        x.next.prev = x.prev
        return x
        
    def find(self, val):
        x = self.head.next
        for i in range(self.size()):
            if x.data == val:
                return x
            x = x.next
        return None
    
    def size(self):
        return self.n
    

# Converts a linked list to a regular list.
def linkedListToList(linked_list):
    result = []
    current = linked_list.head.next
    while current != linked_list.head:
        result.append(current.data)
        current = current.next
    return result


# Sorts a list using the merge sort algorithm.
def mergeSort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = mergeSort(lst[:mid])
    right = mergeSort(lst[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result



class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_into_bst(root, value):
    if root is None:
        return TreeNode(value)
    elif value < root.value:
        root.left = insert_into_bst(root.left, value)
    else:
        root.right = insert_into_bst(root.right, value)
    return root

def listToBstTree(arr):
    root = None
    for value in arr:
        root = insert_into_bst(root, value)
    return root

def inorder_bst(node):
    result = []
    if node:
        result.extend(inorder_bst(node.left))   
        result.append(node.value)
        result.extend(inorder_bst(node.right))  
    return result


# Calculates the median of a list for third option.
def calculateMedian(lst):
    root=listToBstTree(lst)
    sorted_lst = inorder_bst(root)
    print(sorted_lst)
    n = len(sorted_lst)
    if n % 2 == 1:
        return sorted_lst[n // 2]
    else:
        return (sorted_lst[n // 2 - 1] + sorted_lst[n // 2]) / 2


def Calculate_Median(linked_list):
    lst = linkedListToList(linked_list)
    return calculateMedian(lst)

#Convert list to linked list
def listToTheLinckedlist(oldList):
    linked_list = List()
    for product in oldList:
        linked_list.insert_after(linked_list.head, product)
    return linked_list


class BSTNode:
    def __init__(self, product):
        self.product = product
        self.left = None
        self.right = None

#################
class ProductBST:
    def __init__(self):
        self.root = None

    def insert(self, product):
        if self.root is None:
            self.root = BSTNode(product)
        else:
            self._insert(self.root, product)

    def _insert(self, node, product):
        if product.productName < node.product.productName:
            if node.left is None:
                node.left = BSTNode(product)
            else:
                self._insert(node.left, product)
        elif product.productName > node.product.productName:
            if node.right is None:
                node.right = BSTNode(product)
            else:
                self._insert(node.right, product)

    def delete(self, productName):
        self.root = self._delete(self.root, productName)

    def _delete(self, node, productName):
        if node is None:
            return node

        if productName < node.product.productName:
            node.left = self._delete(node.left, productName)
        elif productName > node.product.productName:
            node.right = self._delete(node.right, productName)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            temp = self._min_value_node(node.right)
            node.product = temp.product
            node.right = self._delete(node.right, temp.product.productName)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, name):
        return self._search(self.root, name)

    def _search(self, node, name):
        if node is None or node.product.productName == name:
            return node
        if name < node.product.productName:
            return self._search(node.left, name)
        return self._search(node.right, name)


#################
class PriceBST:
    def __init__(self):
        self.root = None

    #Add new product
    def insert(self, product):
        if self.root is None:
            self.root = BSTNode(product)
        else:
            self.insert2(self.root, product)

    #Add new product in bst tree
    def insert2(self, node, product):
        if product.priceOfThisYear < node.product.priceOfThisYear:
            if node.left is None:
                node.left = BSTNode(product)
            else:
                self.insert2(node.left, product)
        elif product.priceOfThisYear > node.product.priceOfThisYear:
            if node.right is None:
                node.right = BSTNode(product)
            else:
                self.insert2(node.right, product)

    #Delete a product in bst tree
    def delete(self, price):
        self.root = self._delete(self.root, price)

    def _delete(self, node, price):
        if node is None:
            return node

        if price < node.product.priceOfThisYear:
            node.left = self._delete(node.left, price)
        elif price > node.product.priceOfThisYear:
            node.right = self._delete(node.right, price)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            temp = self._min_value_node(node.right)
            node.product = temp.product
            node.right = self._delete(node.right, temp.product.priceOfThisYear)

        return node

    #Get minimum value in bst tree
    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current


    #Get In order of bst tree
    #In order give a sorted array
    def inOrder(self, node):
        order_list = []
        if node is None:
            return order_list

        order_list.extend(self.inOrder(node.left))
        order_list.append(node.product)
        order_list.extend(self.inOrder(node.right))

        return order_list
    

    #array of smallest price by using in order in bst tree
    def sorted_smallest_price(self):
        array = self.inOrder(self.root)
        for product in array:
            print(product.productName)


    #array of biggest price by using reverse of in order in bst tree
    def sorted_biggest_price(self):
        array = reversed(self.inOrder(self.root))
        for product in array:
            print(product.productName)


    #finding a product by price in bst tree
    def find_product_by_price(self, price):
        return self.search(self.root, price)

    def search(self, node, price):
        if node is None or node.product.priceOfThisYear == price:
            return node
        if price < node.product.priceOfThisYear:
            return self.search(node.left, price)
        return self.search(node.right,price)

    #for show a list of price in special range in last year
    def range_of_price(self, range1, range2):
        if range2 < range1:
            range2, range1 = range1, range2

        productRange1 = self.find_product_by_price(range1)
        productRange2 = self.find_product_by_price(range2)

        while productRange1 is None:
            range1 += 1
            productRange1 = self.find_product_by_price(range1)
        while productRange2 is None:
            range2 -= 1
            productRange2 = self.find_product_by_price(range2)

        list = self.inOrder(self.root)
        for product in list:
            if product.priceOfThisYear >= productRange1.product.priceOfThisYear and product.priceOfThisYear <= productRange2.product.priceOfThisYear:
                print(product.productName)

############
class Product:
    def __init__(self, productName, productQcode, listOfPrice):
        self.productName = productName
        self.productQcode = productQcode
        self.listOfPrice = listToTheLinckedlist(listOfPrice)
        self.priceOfThisYear = listOfPrice[0]
        self.medianPrice = Calculate_Median(self.listOfPrice)
############

############
class ProductManager:
    def __init__(self):
        self.products = []
        self.product_bst = ProductBST()
        self.price_bst = PriceBST()

    def add_product(self, product):
        self.products.append(product)
        self.product_bst.insert(product)
        self.price_bst.insert(product)

    def check_qr_code(self, qr_code):
        for product in self.products:
            if product.productQcode == qr_code:
                return True
        return False

    def find_product_by_name(self, name):
        result_node = self.product_bst.search(name)
        return result_node.product if result_node else None
#############


#button 1 add new product
def Add_new_product():
    name = input("Enter name of product: ")
    Qcode = input("Enter Qcode of your product: ")
    if product_manager.check_qr_code(Qcode):
        print("QR code already exists.")
        return
    listprice = []
    while True:
        print("Enter the consecutive prices of your product from this year (2025) to previous years in order and enter the number 0 when you are finished.")
        added = int(input("Price: "))
        if added:
            listprice.append(added)
        elif added == 0:
            break
    product = Product(name, Qcode, listprice)
    product_manager.add_product(product)
    return


def Add_new_price(name):
    product = product_manager.find_product_by_name(name)
    if product is None:
        raise Exception("Product not found")
    while True:
        print("Enter the new price of your product.")
        added = int(input("Price: "))
        if added:
            product.listOfPrice.insert_after(product.listOfPrice.head, added)
            product.medianPrice = Calculate_Median(product.listOfPrice)
            break
        else:
            print("Invalid price. Please enter a valid price.")


#button 2  Delete product by name
def Delete_product(name):
    product = product_manager.find_product_by_name(name)
    if product is None:
        raise Exception("Product not found")
    else:
        # Delete from product BST
        product_manager.product_bst.delete(name)
        # Delete from price BST
        current_price = product.listOfPrice.head.next
        while current_price != product.listOfPrice.head:
            product_manager.price_bst.delete(current_price.data)
            current_price = current_price.next
        # Remove from the product list
        product_manager.products.remove(product)


product_manager = ProductManager()

flagForWholeProgramme = True

while flagForWholeProgramme:
    inputNumber = int(input("Enter the number: (1.Add new product, 2.Delete a product, 3.Median, 4.List of smallest price , 5.List of biggest price , 6.A range of price, 7.exit) "))

    if inputNumber == 1:
        if int(input("Do you want to add a product or new price of a product:  1=product , 0=New price  :")):
            Add_new_product()
        else:
            nameofproduct = input("Enter the name of product which you want to add price:")
            Add_new_price(nameofproduct)

    elif inputNumber == 2:
        name = input("Enter the name of the product to delete: ")
        Delete_product(name)

    elif inputNumber == 3:
        for product in product_manager.products:
            print(f"Product Name: {product.productName}, Median Price: {product.medianPrice}")

    elif inputNumber == 4:
        product_manager.price_bst.sorted_smallest_price()

    elif inputNumber == 5:
        product_manager.price_bst.sorted_biggest_price()

    elif inputNumber == 6:
        range1 = int(input("Enter the lower range: "))
        range2 = int(input("Enter the upper range: "))
        product_manager.price_bst.range_of_price(range1, range2)

    elif inputNumber == 7:
        break

    else:
        print("Please input a number between 1 to 7, try again:")