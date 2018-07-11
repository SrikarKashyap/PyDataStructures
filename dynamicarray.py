import ctypes
class Array:
    """
    An dynamically allocated array implementation
    """
    
    def __init__(self, typ):
        """
        Initialize Array element with specifying the type and length
        typ: str
        """
        self.typ = typ
        self.length = 0
        self.capacity = 2
        self.A = self.make_array(self.capacity)
        
    def make_array(self,new_capacity):
        """
        Create and allocate memory for a new array using ctypes
        """
        return (new_capacity * ctypes.py_object)()
        
    def _resize(self,new_capacity):
        """
        Dynamically (re)create a new array with the new capacity
        """
        B = self.make_array(new_capacity)
        for i in range(self.length):
            B[i] = self.A[i]
        self.A = B
        del(B)
        self.capacity = new_capacity
        
        
    def des(self):
        """
        Brief summary of the array. Print's the type and length.
        """
        print("Type is {} and Length is {}".format(self.typ,self.length))
        
    def get_length(self):
        """
        Returns current length of the array
        """
        return self.length
    
    def is_empty(self):
        """
        Returns if the array is empty (length=0)
        """
        return self.length==0
    
    def at(self, index):
        """
        Return the element at the given index. Raise exception if not found
        """
        if index > self.length or index < 0:
            raise ArithmeticError("Index out of bounds!")
        return self.A[index]
    
    def push(self, item):
        """
        Push new elements into the Array. Resize array if full
        """
        if self.length>=self.capacity:
            self._resize(2*self.capacity)
            print("New capacity is {}".format(self.capacity))
            #self.length += 1
        self.A[self.length] = item
        self.length += 1
        
    def find(self, item):
        """
        Find if a given element is present in the array. Return -1 otherwise
        """
        for i in range(self.length):
            if self.A[i]==item:
                return i
        return -1
    
    def pop(self):
        """
        Pop the outermost element (last element)
        """
        if self.length==0:
            raise IndexError("No more elements!")
        tobedel = self.A[self.length-1]
        self.A[self.length-1] = None
        self.length -= 1
        return tobedel
    
    def print_elements(self):
        """
        Print the elements of the array
        """
        for i in range(self.length):
            print(self.A[i])
            
    def prepend(self,item):
        """
        Append an item at the first location (zero)
        """
        if self.length >= self.capacity-1:
            self._resize(self, self.capacity*2)
        for i in range(self.length-1,-1,-1):
            #if self.length == self.capacity-1:
            #    self._resize(self, self.capacity*2)
            self.A[i+1] = self.A[i]
        self.A[0] = item
        self.length += 1
        
    def delete(self, index):
        """
        Delete the item at the given index. Raise error otherwise
        """
        if (self.length == 0) or (index > self.length):
            raise ArithmeticError("Invalid Index!")
        if self.length >= self.capacity-1:
            self._resize(self, self.capacity*2)
        eletodel = self.A[index]
        for i in range(index,self.length-1):
            self.A[i] = self.A[i+1]
        self.length -= 1
        return eletodel
    
    def insert(self, index, item):
        """
        Insert element at the given index
        """
        if (self.length == 0) or (index > self.length):
            raise ArithmeticError("Invalid Index!")
        if self.length >= self.capacity-1:
            self._resize(self.capacity*2)
        for i in range(self.length-1,index-1,-1):
            #if self.length == self.capacity-1:
            #    self._resize(self, self.capacity*2)
            self.A[i+1] = self.A[i]
        self.A[index] = item
        self.length += 1
        
    def remove(self, value):
        """
        Remove a specified item from the list (if exists)
        """
        element = -1
        if self.length==0:
            raise ArithmeticError("No Elements to remove!")
        for i in range(self.length):
            if self.A[i]==value:
                element = self.delete(i)
        return element
            
        