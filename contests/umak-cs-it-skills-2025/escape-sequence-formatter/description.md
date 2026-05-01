# Escape Sequence Formatter
**Topics:** Escape sequences, Output operations, String handling

**Problem Description:**
Write a program that displays a formatted receipt with proper alignment using tabs and newlines. Read item names, quantities, and prices, then display a formatted receipt.

**Input:**
- Integer n (number of items, 1 ≤ n ≤ 5)
- For each item: name (string), quantity (int), price (float)

**Output:**
- Formatted receipt with tabs between columns

**Sample Input:**
```
3
Apple 5 20.50
Banana 10 15.00
Orange 3 25.75
```

**Sample Output:**
```
ITEM		QTY	PRICE	TOTAL
Apple		5	20.50	102.50
Banana		10	15.00	150.00
Orange		3	25.75	77.25
-----------------------------------
GRAND TOTAL:		329.75
```

---
