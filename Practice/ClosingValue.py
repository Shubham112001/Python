N = int(input())
lst1 = []
lst2 = []
for i in range(N):
    TradeId, TradeType, StockName, Price, Quantity = input().split(" ")
    lst1.append(int(TradeId))
    lst1.append(TradeType)
    lst1.append(StockName)
    lst1.append(int(Price))
    lst1.append(int(Quantity))
    lst2.append(lst1)

print(lst2)

