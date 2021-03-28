import math

def calculateTotalProfit(nestedRevenues, nestedExpenses):
    comm = [0 for person in range(len(nestedRevenues[0]))]
    for rev in range(len(nestedRevenues)):
        itemProfits = calculateItemProfit(nestedRevenues[rev], nestedExpenses[rev])
        comm = [comm[i] + itemProfits[i] for i in range(len(comm))]
    
    return comm

def calculateItemProfit(reven, expen):
    return [max(0, reven[i] - expen[i]) for i in range(len(reven))]

if __name__ == "__main__":
    revenues = [
        [190, 140, 1926, 14, 143],
        [325, 19, 293, 1491, 162],
        [682, 14, 852, 56, 659],
        [829, 140, 609, 120, 87]
        ]

    expenses = [
        [120, 65, 890, 54, 430],
        [300, 10, 23, 802, 235],
        [50, 299, 1290, 12, 145],
        [67, 254, 89, 129, 76]
        ]

    profits = calculateTotalProfit(revenues, expenses)
    print([round(profits[i]*0.062, 2)
           for i in range(len(revenues[0]))])
