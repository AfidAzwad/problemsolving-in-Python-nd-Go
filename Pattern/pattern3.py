#     *
#    * *
#   * * *
#  * * * *
# * * * * *

n = int(input("n = ").strip())

for i in range(1, n +1):
    for j in range(1, n-i+1):
        print(end=" ")
    for x in range(i, 0, -1):
        print("*", end= " ")
    print()