n,m,k=map(int,input().split())
diff = k - 3
idx = m - 1
next_idx = (idx + diff % n + n) % n
next_number = next_idx + 1

print(next_number)
