"""
At a lemonade stand, each lemonade costs $5.
Customers are standing in a queue to buy from you and order one at a time
(in the order specified by bills).
Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.
You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you do not have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith customer pays,
return true if you can provide every customer with the correct change, or false otherwise.
------------------------
В лимонадном ларьке каждый лимонад стоит $5.
Клиенты стоят в очереди, чтобы купить у вас, и заказывают по одному за раз
(в порядке, указанном в bills).
Каждый клиент будет покупать только один лимонад и платить либо $5, либо $10, либо $20.
Вы должны предоставить клиенту правильную сдачу, чтобы чистая транзакция составляла $5.

Обратите внимание, что вначале у вас нет никакой сдачи.

Учитывая целочисленный массив bills, где bills[i] - это счет, который платит i-й клиент,
вернуть true, если вы можете обеспечить каждому клиенту правильную сдачу, и false в противном случае.
------------------------
EASY
"""
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0

        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1
            else:  # bill == 20
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False

        return True


"""
Чтобы решить задачу и определить, сможете ли вы предоставить каждому клиенту правильную сдачу, 
можно следовать следующим шагам:

    Следите за доступной сдачей: Отслеживайте количество купюр номиналом $5 и $10, которые у вас есть.

    Обрабатывайте каждый счет: Для каждой купюры, которую дает клиент:
        Если клиент дает купюру $5, сдачу давать не нужно, просто увеличьте количество купюр $5.
        Если клиент дает купюру $10, нужно дать ему сдачу в размере $5. Поэтому проверьте, 
        есть ли у вас купюра $5:
            Если у вас есть купюра $5, дайте ее в качестве сдачи, 
            уменьшите количество купюр $5 и увеличьте количество купюр $10.
            Если у вас нет купюры $5, вы не сможете дать правильную сдачу, поэтому верните False.
        Если клиент дает купюру $20, нужно дать ему сдачу в размере $15. 
        Лучший способ сделать это - дать одну купюру $10 и одну купюру $5 (если они у вас есть). 
        Если нет, попробуйте дать три купюры $5. Если ни один из вариантов невозможен, верните False.

    Окончательная проверка: Если вам удалось дать сдачу всем клиентам, верните True.
"""

bills = [5,5,5,10,20]
sol = Solution()
res = sol.lemonadeChange(bills)
print(res)
assert res == True

bills = [5,5,10,10,20]
sol = Solution()
res = sol.lemonadeChange(bills)
print(res)
assert res == False
