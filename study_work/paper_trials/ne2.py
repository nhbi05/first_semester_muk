def sum_n(*numbers):
    total = 0
    for n in numbers:
        total += n
    print(f"Sum is {total}")
sum_n(1,3,4,5,6)