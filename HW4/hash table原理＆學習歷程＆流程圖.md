 # Hash Table
## Hash function 
Hash Table希望能夠將存放資料的「Table」的大小(size)降到「真正會存放進Table的資料的數量」，也就是「有用到的Key的數量」：

* 若有用到的Key之數量為n，Table的大小為m，那麼目標就是m=Θ(n)。
要達到這個目標，必須引入Hash Function，將Key對應到符合Table大小m的範圍內，index=h(Key)，即可成為Hash Table的index。

觀念圖（這裡的index就像是一個個的抽屜，依照你的編號進入你該去的抽屜裡。）

![image](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Hash_table_3_1_1_0_1_0_0_SP.svg/473px-Hash_table_3_1_1_0_1_0_0_SP.svg.png)



## Hash table 學習歷程
參考資料:https://leetcode.com/problems/design-hashset/discuss/379193/Python-chaining-hashset-easy-to-understand
案作業要求要用MD5，將一般文字轉換成一串亂碼，也就是key。key/5的餘數就是index的編號。依照編號放進去。
