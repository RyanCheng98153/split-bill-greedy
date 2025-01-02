import heapq
from collections import defaultdict

class DebtSimplification:
    @staticmethod
    def heap_optimized_algorithm(debts):
        """
        Simplify debts using a heap-based optimization approach.
        """
        # Step 1: Calculate net balances
        balance = defaultdict(int)
        for debt in debts:
            balance[debt['from']] -= debt['amount']
            balance[debt['to']] += debt['amount']

        # Step 2: Separate creditors and debtors, using heaps for efficient processing
        creditors = []  # Max-heap for creditors (positive balances)
        debtors = []    # Max-heap for debtors (negative balances)

        for person, amount in balance.items():
            if amount > 0:
                heapq.heappush(creditors, (-amount, person))  # Use negative for max-heap
            elif amount < 0:
                heapq.heappush(debtors, (-amount, person))  # Use negative for max-heap

        # Step 3: Optimize debt settlement
        transactions = []

        while creditors and debtors:
            credit_amount, creditor = heapq.heappop(creditors)
            debt_amount, debtor = heapq.heappop(debtors)

            # Convert back to positive values
            credit_amount = -credit_amount
            debt_amount = -debt_amount

            # Settle the minimum amount
            settled_amount = min(credit_amount, debt_amount)
            transactions.append({"from": debtor, "to": creditor, "amount": settled_amount})

            # Update remaining amounts and push back to heaps if needed
            if credit_amount > settled_amount:
                heapq.heappush(creditors, (-(credit_amount - settled_amount), creditor))
            if debt_amount > settled_amount:
                heapq.heappush(debtors, (-(debt_amount - settled_amount), debtor))
                
        # switch from to if the amount is negative
        for i in range(len(transactions)):
            if transactions[i]["amount"] < 0:
                transactions[i]["from"], transactions[i]["to"] = transactions[i]["to"], transactions[i]["from"]
                transactions[i]["amount"] = -transactions[i]["amount"]

        return transactions

    @staticmethod
    def greedy_algorithm(debts):
        """
        Simplify debts using a greedy algorithm approach with improvements.
        """
        # Calculate net balances
        balances = {}
        for debt in debts:
            balances[debt['from']] = balances.get(debt['from'], 0) - debt['amount']
            balances[debt['to']] = balances.get(debt['to'], 0) + debt['amount']

        # Remove zeros (closed loops)
        balances = {k: v for k, v in balances.items() if v != 0}
        
        # If all balances are zero, return an empty transaction list
        if not balances:
            return []

        # Sort balances
        positive = [(k, v) for k, v in balances.items() if v > 0]
        negative = [(k, -v) for k, v in balances.items() if v < 0]

        # Transactions list
        transactions = []

        # Process debts
        while negative and positive:
            debtor, debt = negative.pop(0)
            creditor, credit = positive.pop(0)
            # Settle the minimum amount
            settled_amount = min(debt, credit)
            transactions.append({
                "from": debtor,
                "to": creditor,
                "amount": settled_amount
            })

            # Update remaining balances
            if credit > settled_amount:
                positive.insert(0, (creditor, credit - settled_amount))
            if debt > settled_amount:
                negative.insert(0, (debtor, debt - settled_amount))

            # Re-sort to ensure global balance optimization
            positive.sort(key=lambda x: x[1], reverse=True)
            negative.sort(key=lambda x: x[1], reverse=True)

        return transactions
    
    @staticmethod
    def greedy_algorithm(debts):
        """
        Simplify debts using a greedy algorithm approach with improvements.
        """
        # Calculate net balances
        balances = {}
        for debt in debts:
            balances[debt['from']] = balances.get(debt['from'], 0) - debt['amount']
            balances[debt['to']] = balances.get(debt['to'], 0) + debt['amount']

        # Remove zeros (closed loops)
        balances = {k: v for k, v in balances.items() if v != 0}
        
        # If all balances are zero, return an empty transaction list
        if not balances:
            return []

        # Sort balances
        positive = [(k, v) for k, v in balances.items() if v > 0]
        negative = [(k, -v) for k, v in balances.items() if v < 0]

        # Transactions list
        transactions = []

        # Process debts
        while negative and positive:
            debtor, debt = negative.pop(0)
            creditor, credit = positive.pop(0)
            # Settle the minimum amount
            settled_amount = min(debt, credit)
            transactions.append({
                "from": debtor,
                "to": creditor,
                "amount": settled_amount
            })

            # Update remaining balances
            if credit > settled_amount:
                positive.insert(0, (creditor, credit - settled_amount))
            if debt > settled_amount:
                negative.insert(0, (debtor, debt - settled_amount))

            # Re-sort to ensure global balance optimization
            positive.sort(key=lambda x: x[1], reverse=True)
            negative.sort(key=lambda x: x[1], reverse=True)

        return transactions
    
    
    @staticmethod
    def simplify_debts(debts, sorting=True):
        from collections import defaultdict

        # 步驟 1: 計算每個人的淨債務（正數代表應收款，負數代表應付款）
        balance = defaultdict(int)
        for debt in debts:
            balance[debt['from']] -= debt['amount']
            balance[debt['to']] += debt['amount']

        # 步驟 2: 將非零的債務平衡值分為兩組（應收款和應付款）
        creditors = []  # 應收款者
        debtors = []    # 應付款者
        
        for person, amount in balance.items():
            if amount > 0:
                creditors.append((person, amount))
            elif amount < 0:
                debtors.append((person, -amount))
        
        # sort creditors and debtors by amount
        if sorting:
            creditors.sort(key=lambda x: x[1], reverse=True)
            debtors.sort(key=lambda x: x[1], reverse=True)
        
        # 步驟 3: 優化償還債務的次數
        simplified_transfers = []
        i, j = 0, 0
        while i < len(creditors) and j < len(debtors):
            creditor, credit_amount = creditors[i]
            debtor, debt_amount = debtors[j]

            # 償還的金額是兩者中較小的那個
            transfer_amount = min(credit_amount, debt_amount)
            simplified_transfers.append({"from": debtor, "to": creditor, "amount": transfer_amount})

            # 更新剩餘金額
            creditors[i] = (creditor, credit_amount - transfer_amount)
            debtors[j] = (debtor, debt_amount - transfer_amount)

            # 如果某人的債務已完全償還，移動到下一個人
            if creditors[i][1] == 0:
                i += 1
            if debtors[j][1] == 0:
                j += 1

        return simplified_transfers

# Example usage
# input_data = {
#     "debts": [
#         {"from": 0, "to": 1, "amount": 10},
#         {"from": 1, "to": 2, "amount": 20},
#         {"from": 2, "to": 3, "amount": 30},
#         {"from": 3, "to": 0, "amount": 10},
#         {"from": 0, "to": 2, "amount": 20},
#         {"from": 1, "to": 3, "amount": 30},
#     ]
# }

if __name__ == "__main__":
    import sys
    import json
    
    with open(sys.argv[1], "r") as file:
        input_data = json.load(file)

    # simplified_debts = DebtSimplification.simplify_debts(input_data["debts"], sorting=True)
    # simplified_debts = DebtSimplification.greedy_algorithm(input_data["debts"])
    simplified_debts = DebtSimplification.heap_optimized_algorithm(input_data["debts"])
    print("Transfer Simplified Debts:")
    for transaction in simplified_debts:
        print(transaction)
