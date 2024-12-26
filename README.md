# It is a Split Bill Method

### Usage
```bash
python ./splitbill.py ./samples/input.json
```


### Sample Input: 
 - `input.json`
    ```json
    {
        "debts": [
        {"from": 0, "to": 1, "amount": 100},
        {"from": 1, "to": 2, "amount": 50},
        {"from": 2, "to": 3, "amount": 30},
        {"from": 3, "to": 4, "amount": 40},
        {"from": 4, "to": 5, "amount": 25},
        {"from": 5, "to": 6, "amount": 75},
        {"from": 6, "to": 0, "amount": 60},
        {"from": 0, "to": 2, "amount": 15},
        {"from": 1, "to": 3, "amount": 20},
        {"from": 2, "to": 4, "amount": 10},
        {"from": 3, "to": 5, "amount": 35},
        {"from": 4, "to": 6, "amount": 45},
        {"from": 5, "to": 0, "amount": 50},
        {"from": 6, "to": 1, "amount": 90},
        {"from": 1, "to": 4, "amount": 85},
        {"from": 3, "to": 0, "amount": 65}
        ]
    }
    ```