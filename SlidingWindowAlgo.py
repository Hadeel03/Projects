#Ghadeer Al Jufout

import sys

def sum_of_digits(n):
    total = 0
    while n:
        total += n % 10
        n //= 10
    return total

def main(filename):

        with open(filename, 'r') as file:
            numbers = [int(line.strip()) for line in file]

        temp = {}
        maxLen = 0
        i = 0

        for j in range(len(numbers)):
            num_sum = sum_of_digits(numbers[j])
            if num_sum in temp:
                i = max(i, temp[num_sum])
            maxLen = max(maxLen, j - i + 1)
            temp[num_sum] = j + 1

        print(maxLen)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        pass
    else:
        main(sys.argv[1])
