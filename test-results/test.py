from splitbill import DebtSimplification

def debt_generator(records, people):
    import random
    debts = []
    for _ in range(records):
        from_person = random.choice(people)
        to_person = random.choice([p for p in people if p != from_person])
        amount = random.randint(1, 100)
        debts.append({"from": from_person, "to": to_person, "amount": amount})
    return debts

def test(testcases:list[tuple[int, int]] = None):
    from time import time
    method_time = {
        "greedy": 0,
        "hedging": 0,
        "hedge_sort": 0
    }

    method_transaction = {
        "greedy": 0,
        "hedging": 0,
        "hedge_sort": 0
    }

    input_data = {
        "debts": []
    }
    
    for p, r in testcases:
        input_data["debts"] = debt_generator(r, list(range(p)))
        
        start = time()
        simplified_debts = DebtSimplification.simplify_debts(input_data["debts"], sorting=False)
        end = time()
        method_time["hedging"] += end - start
        method_transaction["hedging"] += len(simplified_debts)
        # print("Transfer Simplified Debts:")
        # for transaction in simplified_debts:
        #     print(transaction)
        
        start = time()
        simplified_debts = DebtSimplification.simplify_debts(input_data["debts"], sorting=True)
        end = time()
        method_time["hedge_sort"] += end - start
        method_transaction["hedge_sort"] += len(simplified_debts)
        # print("Transfer Simplified Debts:")
        # for transaction in simplified_debts:
        #     print(transaction)
        
        
        # Call the greedy algorithm
        start = time()
        simplified_debts = DebtSimplification.greedy_algorithm(input_data["debts"])
        end = time()
        method_time["greedy"] += end - start
        method_transaction["greedy"] += len(simplified_debts)
        # print("Greedy Simplified Debts:")
        # for transaction in simplified_debts:
        #     print(transaction)
        
        
    method_time["greedy"] /= len(testcases)
    method_time["hedging"] /= len(testcases)
    method_time["hedge_sort"] /= len(testcases)
    
    print("Testcase for {} people and {} records".format(p, r))
    for method, time_taken in method_time.items():
        print(f"Method: {method}, \tTime Taken: {time_taken * 1000:.2f} ms, \tAverage Transaction: {method_transaction[method] / len(testcases)}")

if __name__ == "__main__":
    import sys

    people = int(sys.argv[1])
    records = int(sys.argv[2])
    # Test the performance of the greedy algorithm
    test([ 
        (people, records)
        for _ in range(10)
    ])
