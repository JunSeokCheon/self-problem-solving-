import sys

m, n = map(int, sys.stdin.readline().split())
package_list = []
price_list = []
for _ in range(n):
    package, price = map(int, sys.stdin.readline().split())
    package_list.append(package)
    price_list.append(price)

pack = min(package_list)
pric = min(price_list)

if pack < pric * 6:
    if pack < (m%6)*pric:
        print((m//6)*pack + pack)
    else:
        print((m//6)*pack + (m%6)*pric)
else:
    print(m*pric)