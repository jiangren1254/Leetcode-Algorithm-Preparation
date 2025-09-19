def main():
    T = int(input())
    for _ in range(T):
        n, m, x, y = map(int, input().split())
        prices = list(map(int, input().split()))
        
        sold = 0
        total_income = 0
        
        for i in range(m):
            price = prices[i]
            if price >= y and sold < n:  # 贪心
                total_income += price
                sold += 1
        
        profit = total_income - n * x
        print(profit)

main()