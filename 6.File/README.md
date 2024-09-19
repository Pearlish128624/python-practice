# File

## Homework
Based on previous homework, there will be new teams to handle your orders.
They will collect orders by different customers, and place them into `.\orders`.
You should read all of them and place them into `.\products`.

## Example
```
|--main.py
|--orders
|  |--Amy_20240101.txt
|  |--Bob_20240525.txt
|  |--Cater
|     |--2024
|     |  |--0205.txt
|     |--2025
|     |  |--1009.txt
|     |  |--1122.txt
|     |--20231231.txt
|--products
   |--Ladder.txt
   |--Tree.txt
   |--LetterV.txt
```

# Optional
Can you display more information at products?
For example, who orders what in which date.
You can also display their orders into different folder based on the customer's name.

# Hint
- [os.walk](https://blog.gtwang.org/programming/python-list-all-files-in-directory/#google_vignette)