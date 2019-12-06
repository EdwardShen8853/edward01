class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyHashSet:       

    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        
    def add(self, key):
        key_int = MyHashSet.Hash(self, key)
        idx = key_int % self.capacity
        if not self.data[idx]:
            self.data[idx] = ListNode(key_int)
        else:
            head = self.data[idx]
            while head.val != key_int and head.next:
                head = head.next
            if head.val != key_int:
                head.next = ListNode(key_int)
                    
            return
    def remove(self, key):
        key_int = MyHashSet.Hash(self, key)
        if not self.contains(key):
            return
        idx = key_int % self.capacity
        if self.data[idx].val == key_int:
            self.data[idx] = self.data[idx].next
            return
        head = self.data[idx]
        while head.next.val != key_int:
            head = head.next
        head.next = head.next.next
    def contains(self, key):
        key_int = MyHashSet.Hash(self, key)
        idx = key_int % self.capacity
        if not self.data[idx]:
            return False
        head = self.data[idx]
        while head:
            if head.val == key_int:
                return True
            head = head.next
        return False
    def Hash(self, key):
        from Crypto.Hash import MD5
        h = MD5.new()
        h.update(key.encode('utf-8'))
        new_key=int(h.hexdigest(),16)
        return new_key
      
參考資料:https://leetcode.com/problems/design-hashset/discuss/379193/Python-chaining-hashset-easy-to-understand
