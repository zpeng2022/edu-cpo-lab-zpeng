from SelfHashMap import SelfHashMap


# Add a new element
# set an element with specific index

# remove an element by:
# - index for lists
# - key for dictionaries
# - value for sets value

# Access:
# - size()
# - is member()
# - reverse()

# Conversion from/to built-in list
# - from_list
# - to_list

# Filter data structure by specific predicate
# Map structure by specific function
# Reduce:
# Data structure should be an iterator
# mutable version
# Data structure should be a monoid and implement empty and concat methods,

# extra attention to return values and corner cases like:
# puts None value to the data structure
# what should happen, if a user puts elements with different types.

class Dic(object):
    def __init__(self):
        """initialize the Dic"""
        self.__hashmap = SelfHashMap()
        self.__lst = []
        self.__pos = 0
        self.__len = 0

    def __str__(self):
        """for str() implementation for printing"""
        return " : ".join(map(str, self.to_list()))

    # Add a new element
    def add(self, key, value):
        """add an element to Dic"""
        self.__hashmap.put_in_hashmap(key, value)

    # set an element with specific index
    def set(self, key, value):
        """set an element to Dic"""
        self.__hashmap.put_in_hashmap(key, value)

    # get an element with specific key
    def get(self, key):
        """get an element form Dic according
           to its key"""
        return self.__hashmap.get_from_hashmap(key)

    # change the value of a specific key
    def change(self, key, value):
        """change an element's value according
           to its key"""
        self.__hashmap.put_in_hashmap(key, value)

    # delete a node in dic according to the key
    def remove(self, key):
        """remove an element"""
        return self.__hashmap.delete_node_in_hashmap(key)

    # size
    def size(self):
        """get the size of Dic"""
        siz = self.__hashmap.size
        return siz

    # is member
    def is_member(self, key, value):
        """whether [key, value] is an element in Dic"""
        val = self.__hashmap.get_from_hashmap_with_node(key)
        return True if val is not None else False

    def is_member_for_key(self, key):
        """check the member only for key"""
        val = self.__hashmap.get_from_hashmap_with_node(key)
        return True if val is not None else False

    # reverse
    # there is no order in dict
    def reverse(self):
        """reverse the Dic
           but Dic have no order
           so, the function always
           return True"""
        return True

    # from_list
    def from_list(self, lst):
        """get elements from a list"""
        if len(lst) == 0:
            return
        for e in lst:
            self.__hashmap.put_in_hashmap(e[0], e[1])

    # to_list
    def to_list(self):
        """output elements in Dic to a list"""
        return self.__hashmap.get_to_list()

    # filter
    def filter_the_value(self, f):
        """filter elements' value according to
           the function f"""
        lst = self.to_list()
        capacity = self.__hashmap.capacity
        load_factor = self.__hashmap.load_factor
        self.__hashmap = SelfHashMap(capacity, load_factor)
        # there is a pair in list
        tem_len = len(lst)
        for i in range(tem_len):
            cur = lst[i]
            if f(cur[1]) is True:
                self.__hashmap.put_in_hashmap(cur[0], cur[1])

    # map
    def map(self, f):
        """map elements' value according to the
           function f"""
        lst = self.to_list()
        capacity = self.__hashmap.capacity
        load_factor = self.__hashmap.load_factor
        self.__hashmap = SelfHashMap(capacity, load_factor)
        # there is a pair in list
        tem_len = len(lst)
        for i in range(tem_len):
            cur = lst[i]
            tem_cur = f(cur[1])
            self.__hashmap.put_in_hashmap(cur[0], tem_cur)

    # reduce
    def reduce(self, f, initial_state):
        """reduce elements' value according to
           the function f and the initial_state"""
        state = initial_state
        lst = self.to_list()
        capacity = self.__hashmap.capacity
        load_factor = self.__hashmap.load_factor
        self.__hashmap = SelfHashMap(capacity, load_factor)
        # there is a pair in list
        tem_len = len(lst)
        for i in range(tem_len):
            cur = lst[i]
            tem_cur = f(cur[1], state)
            self.__hashmap.put_in_hashmap(cur[0], tem_cur)

    # monoid
    # empty
    def empty(self):
        """let the Dic be empty"""
        self.__hashmap = SelfHashMap()
        return None

    # concat
    def concat(self, a, b):
        """concat two Dic"""
        result = None
        if b is None:
            if a is None:
                result = Dic()
                # return Dic()
            elif isinstance(a, Dic) is True:
                result = a
                # return a
            elif isinstance(a, Dic) is False:
                tem_dic = Dic()
                tem_dic.set(a[0], a[1])
                result = tem_dic
                # return tem_dic
        elif a is None:
            if isinstance(b, Dic) is True:
                result = b
                # return b
            elif isinstance(b, Dic) is False:
                tem_dic = Dic()
                tem_dic.set(b[0], b[1])
                result = tem_dic
                # return tem_dic
        elif isinstance(a, Dic) and isinstance(b, Dic):
            a.from_list(b.to_list())
            result = a
            # return a
        elif isinstance(a, Dic) is False and isinstance(b, Dic) is False:
            tem_dic = Dic()
            tem_dic.set(a[0], a[1])
            tem_dic.set(b[0], b[1])
            result = tem_dic
            # return tem_dic
        self = result
        return self


# iteration
def iterator_element(a):
    """iterator elements in Dic
       the function return the
       temporary object of Dic
       with information about position"""
    if isinstance(a, Dic) is False:
        return None
    tem = Dic()
    tem.from_list(a.to_list())
    tem.__lst = tem.to_list()
    tem.__pos = 0
    tem.__len = tem.size()
    return tem


def next_element(tem):
    """return the next element's value"""
    if tem.__pos >= tem.__len:
        return 0
    tmp = tem.__lst[tem.__pos]
    tem.__pos += 1
    return tmp
