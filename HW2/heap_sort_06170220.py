#!/usr/bin/env python
# coding: utf-8

# In[1]:


#heapsort

class solution(object):
    def swap(self, arr, i, j):#在一個數組裡小交換地i個和第j個
        temp = arr[i]         #生成一個temp=[i],[i]=[j],[j]=temp,即可完成交換
        arr[i] = arr[j]
        arr[j] = temp
    
    def heapify(self, tree, n, i): # n:節點數 i:第幾個節點
        c1 = 2 * i + 1     # 子節點1 = 2*i + 1 
        c2 = 2 * i + 2     # 子節點2 = 2*i + 2 
        max = i            #假設最大值為i,i是父節點
    
    #c1,c2需比n小,才不會超出範圍
    # 如果c1比i大,max值換成c1
        if c1 < n and tree[c1] > tree[i]: 
            max = c1
  
    # 如果c2比max值大,max值換成c2
        if c2 < n and tree[c2] > tree[max]: 
            max = c2 
    #找出最大值了
    
  
    #如果max不等於i,兩者交換位子
        if max != i: 
             self.swap(tree, max, i)
  
        # 對第max個再一次heapify
             self.heapify(tree, n, max) 
  
    def heap_Sort(self, tree): 
        n = len(tree)   #大小為n
  
    # 建一個堆 
        for i in range(n, -1, -1): 
            self.heapify(tree, n, i)  
    # 一個一個砍斷節點 
        for i in range(n-1, 0, -1): 
            self.swap(tree, i, 0)  # swap 
            self.heapify(tree, i, 0)  #默認節點數量減少,n由i來決定,i代表當前節點個數

