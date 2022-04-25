import math


class LinkedNode:
    def __init__(self, key, val, predecessor=None, successor=None):
        self.predecessor, self.successor = predecessor, successor
        self.key, self.val = key, val

    def __repr__(self):
        return "['key: " + self.key + " val: " + self.val + "]"


class LinkedList:
    def __init__(self):
        self.head = LinkedNode(None, 'This_is_a_marker_for_header')
        self.tail = LinkedNode(None, 'This_is_a_marker_for_tail')
        self.head.successor = self.tail
        self.tail.predecessor = self.head
        self.size = 0

    def __str__(self):
        return " : ".join(map(str, self.to_list()))

    def delete_node(self, node):
        # delete a node, if and only if this node is not head or tail
        # O(1)
        if node == self.tail or node == self.head:
            return False
        predecessor = node.predecessor
        successor = node.successor
        successor.predecessor, predecessor.successor = predecessor, successor
        self.size -= 1
        return True

    def append_node(self, node):
        # O(1)
        predecessor = self.tail.predecessor
        node.predecessor, node.successor = predecessor, predecessor.successor
        predecessor.successor, node.successor.predecessor = node, node
        self.size += 1

    def get_a_list(self):
        ret = []
        cur_node = self.head.successor
        # return a list
        # # O(n) or O(self.size)
        while cur_node != self.tail:
            ret.append(cur_node)
            cur_node = cur_node.successor
        return ret

    def get_a_list_without_prev_successor(self):
        ret = []
        cur_node = self.head.successor
        # return a list
        # # O(n) or O(self.size)
        while cur_node != self.tail:
            ret.append((cur_node.key, cur_node.val))
            cur_node = cur_node.successor
        return ret

    def get_node_by_key(self, key):
        # find the node with some key in the list
        # O(n) or O(self.size)
        c = (type(key) == int or type(key) == float) and math.isnan(key)
        cur_node = self.head.successor
        while cur_node != self.tail:
            if type(cur_node.key) == type(key):
                if c is True and math.isnan(cur_node.key):
                    return cur_node
                elif cur_node.key == key:
                    return cur_node
            cur_node = cur_node.successor
        return None


class SelfHashMap:
    def __init__(self, capacity=64, load_factor=5):
        # the capacity is the power of 2
        # load_factor is used to balance the hashmap
        self.capacity = capacity
        self.load_factor = load_factor
        self.size = 0
        # initialize the buckets of the hashmap
        # the object in bucket is a LinkedList
        self.array_node = [LinkedList() for _ in range(capacity)]

    def get_hash_key(self, key):
        # use the built-in hash function to calculate the hash value of a key
        # hash(key) % capacity is same as hash(key) & (self.capacity - 1)
        # when capacity is the pow of 2.
        return hash(key) & (self.capacity - 1)

    def put_in_hashmap(self, key, val):
        hash_key = self.get_hash_key(key)
        linked_list = self.array_node[hash_key]
        if linked_list.size >= self.capacity * self.load_factor:
            self.reset_a_bucket()
            hash_key = self.get_hash_key(key)
            linked_list = self.array_node[hash_key]
        node = linked_list.get_node_by_key(key)
        if node is not None:
            # if node already exists, we need to update the value
            node.val = val
        else:
            self.size += 1
            node = LinkedNode(key, val)
            linked_list.append_node(node)

    def get_from_hashmap(self, key):
        hash_key = self.get_hash_key(key)
        linked_list = self.array_node[hash_key]
        node = linked_list.get_node_by_key(key)
        if node is not None:
            return node.val
        else:
            return None

    def get_from_hashmap_with_node(self, key):
        hash_key = self.get_hash_key(key)
        linked_list = self.array_node[hash_key]
        node = linked_list.get_node_by_key(key)
        return node

    def get_to_list(self):
        head = []
        for i in range(self.capacity):
            linked_list = self.array_node[i]
            # we need to show this result to customer
            # the information of prev and successor in not necessary
            nodes = linked_list.get_a_list_without_prev_successor()
            head.extend(nodes)
        return head

    def reset_a_bucket(self):
        # when the nodes in a bucket is to big
        # we need to resize buckets
        # and change the position of bucket
        # in buckets according to their hash_value
        old_capacity = self.capacity
        resize_headers = [LinkedList() for _ in range(old_capacity * 2)]
        self.capacity = self.capacity * 2
        for i in range(old_capacity):
            linked_list = self.array_node[i]
            nodes = linked_list.get_a_list()
            for u in nodes:
                # recalculate the hash_key
                # and hash_key of each node
                # is changing due to the increase of capacity
                hash_key = self.get_hash_key(u.key)
                head = resize_headers[hash_key]
                head.append_node(u)
        self.array_node = resize_headers

    def delete_node_in_hashmap(self, key):
        node = self.get_from_hashmap_with_node(key)
        if node is None:
            return False
        hash_key = self.get_hash_key(key)
        linked_list = self.array_node[hash_key]
        linked_list.delete_node(node)
        self.size -= 1
        return True
