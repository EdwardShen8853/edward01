 # Hash Table
## Hash function 
Hash Table希望能夠將存放資料的「Table」的大小(size)降到「真正會存放進Table的資料的數量」，也就是「有用到的Key的數量」
每串文字甚至是一個字，只要經過hash function加密後，出來的東西只會是唯一。
一方面是用來將文字轉換成另一個形式，另一方面更是為了防止在做資料區分的時候，去與其他不同的資料作辨別。
這裡是用MD5去做轉換，並把轉成16進位的結果再轉為10進位。

概念圖

![image](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Hash_table_3_1_1_0_1_0_0_SP.svg/473px-Hash_table_3_1_1_0_1_0_0_SP.svg.png)



## Hash table 學習歷程
參考資料:https://leetcode.com/problems/design-hashset/discuss/379193/Python-chaining-hashset-easy-to-understand
按作業要求要用MD5，將一般文字轉換成一串亂碼，也就是key。key/5的餘數就是index的編號。依照編號放進去。

