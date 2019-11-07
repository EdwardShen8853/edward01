#!/usr/bin/env python
# coding: utf-8

# In[5]:


#mergesort

class solution(object):
    def mergesort(self,lists):
        
        if len(lists) <= 1: #如果lists長度小於等於1,直接回傳
            return lists
        mid = len(lists)//2 #找出中間值
        left = self.mergesort(lists[:mid]) #分左右兩邊
        right = self.mergesort(lists[mid:])
        return self.mergeList(left,right)
    def mergeList(self,left, right):
    # 判斷左右兩邊的list，如果只有一邊有值，就可直接回傳
        if len(left) == 0: 
            return right 
        elif len(right) == 0: 
            return left 
     # 比較兩邊list的第一個值，如果右邊大於左邊，那麼就將左邊的第一個值放入，後面的值繼續進行合併和排序，直到比完為止
        elif left[0] < right[0]:
            return [left[0]] + self.mergeList(left[1:], right)
     # 與上一段做的工作相同，方向相反
        else: 
            return [right[0]] + self.mergeList(left, right[1:])

