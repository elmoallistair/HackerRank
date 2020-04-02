# Written: 12-Jan-2020
# https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formatted(number):
    for i in range(1, n+1):
        dec = str(i)
        octa = oct(i)[2:]
        hexa = hex(i)[2:]
        binary = bin(i)[2:]
        width = len(bin(n)[2:])
        
        print (' '.join(map(lambda x: x.rjust(width), [dec, octa, hexa, binary])))
        # print("{} {} {} {}".format(dec.rjust(width), octa.rjust(width), hexa.rjust(width).upper(), binary.rjust(width)))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
