from os import getpid
from multiprocessing import Pool
from time import time


def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def countPrimes(start):
    formatStr = 'process {} processing range ({} {})'
    print(formatStr.format(getpid(), start[0], start[0] + start[1]))
    # explain this part, mostly the [ ]
    return sum([1 for i in range(start[0], start[0] + start[1]) if isPrime(i)])


if __name__ == '__main__':
    n = int(input("Enter number of nodes: "))
    p = Pool(n)
    start = 0
    end = 800000
    # get range
    rng = int(end - start)
    # get blocks per cpu (range with fraction,if any)
    blocks = (int)(rng / n)
    # get fraction from range and seperate the whole number from it
    remainder = (rng % n)
    # temp is the start addrss plus the range so that will be start of the next block
    temp = (start + blocks)
    # start of list, [[start, range][][]...]
    starts = [[start, temp]]
    # while the blocks dont overpass the end (max value)
    while temp < end:
        # add add a list of the start point and it's range into a list
        starts.append([temp, blocks])
        # add range to temp so temp will be next start point
        temp += blocks
        # check if next iteration is the max,
        if ((temp + remainder) == end):
            # last stat points range is the remainder from the mod earlier
            starts.append([temp, remainder])
            # get last start point
            temp += blocks
            # end loop
            break
    t1 = time()
    print(p.map(countPrimes, starts))
    t2 = time()
    p.close()
    print('time take: {} seconds:'.format(t2 - t1))





















    # from os import getpid
    # from multiprocessing import Pool
    # from time import time
    #
    #
    # def isPrime(num):
    #     if num <= 1:
    #         return False
    #     for i in range(2, int(num ** 0.5) + 1):
    #         if num % i == 0:
    #             return False
    #     return True
    #
    #
    # def countPrimes(start):
    #     formatStr = 'process {} processing range ({} {})'
    #     print(formatStr.format(getpid(), start[0], start[0] + start[1]))
    #     # explain this part, mostly the [ ]
    #     return sum([1 for i in range(start[0], start[0] + start[1]) if isPrime(i)])
    #
    #
    # if __name__ == '__main__':
    #     n = int(input("Enter number of nodes: "))
    #     p = Pool(n)
    #     start = 0
    #     end = 800000
    #     # get range
    #     rng = int(end - start)
    #     # get blocks per cpu (range with fraction,if any)
    #     blocks = (int)(rng / n)
    #     # get fraction from range and seperate the whole number from it
    #     remainder = (rng % n)
    #     # temp is the start addrss plus the range so that will be start of the next block
    #     temp = (start + blocks)
    #     # start of list, [[start, range][][]...]
    #     starts = [[start, temp]]
    #     # while the blocks dont overpass the end (max value)
    #     print("BEFORE: ", starts)
    #     while temp < end:
    #         print("IN 1 BEFORE: ", starts)
    #         # add add a list of the start point and it's range into a list
    #         starts.append([temp, blocks])
    #         # add range to temp so temp will be next start point
    #         temp += blocks
    #         print("IN 1 AFTER: ", starts)
    #         # check if next iteration is the max,
    #         if ((temp + remainder) == end):
    #             print("IN 2 DEBUG: ", " TEMP: ", temp, " blocks: ", blocks, " remainder: ", remainder, " overall",
    #                   ((temp + blocks) + remainder))
    #             print("IN 2 BEFORE: ", starts)
    #             # last stat points range is the remainder from the mod earlier
    #             starts.append([temp, remainder])
    #             # get last start point
    #             temp += blocks
    #             print("IN 2 AFTER: ", starts)
    #             # end loop
    #             break
    #     print("final: ", starts)
    #
    #     t1 = time()
    #     # how does this work
    #     # print(p.starmap(countPrimes, zip(starts, repeat(rng))))
    #
    #
    #     print(p.map(countPrimes, starts))
    #
    #     t2 = time()
    #
    #     p.close()
    #     print('time take: {} seconds:'.format(t2 - t1))











































        # n = int(input("Enter number of nodes: "))
    # p = Pool(n)
    # start = 0
    # end = 800000
    # # get range
    # rng = int(end - start)
    # # get blocks per cpu (range with fraction,if any)
    # blocks = (rng / n)
    # # get fraction from range and seperate the whole number from it
    # frac = math.modf(blocks)
    # # fraction
    # rng_r = frac[0]
    # # whole number
    # rng = frac[1]
    # # get the remainder range (so it if is n/x = y.z then it is .z * n
    # last = (int)(math.ceil(rng_r * rng))
    # # get range without fraction
    # temp = (int)(start + blocks)
    # # keep track of loop
    # counter = temp;
    # # start of list, [[start, range][][]...]
    # starts = [[start, temp]]
    #
    # while counter < end:
    #     temp += rng
    #     counter = temp
    #     starts.append([counter, rng])
    #     print("HERE: ", starts)
    # time.sleep(10)
    # t1 = time()
    # # how does this work
    # print(p.starmap(countPrimes, zip(starts, repeat(rng))))
    # t2 = time()
    # p.close()
    # print('time take: {} seconds:'.format(t2 - t1))













    # from os import getpid
    # from multiprocessing import Pool
    # from time import time
    # from itertools import repeat
    #
    #
    # def isPrime(num):
    #     if num <= 1:
    #         return False
    #     for i in range(2, int(num ** 0.5) + 1):
    #         if num % i == 0:
    #             return False
    #     return True
    #
    #
    # def countPrimes(start, rng):
    #     formatStr = 'process {} processing range ({} {})'
    #     print(formatStr.format(getpid(), start, start + rng))
    #     # explain this part, mostly the [ ]
    #     return sum([1 for i in range(start, start + rng) if isPrime(i)])
    #
    #
    # if __name__ == '__main__':
    #     n = int(input("Enter number of nodes: "))
    #     p = Pool(n)
    #     start = 0
    #     end = 800000
    #     rng = int((end - start) / n)
    #     starts = [start]
    #     temp = start + rng
    #     while temp < end:
    #         starts.append(temp)
    #         temp += rng
    #     t1 = time()
    #     # how does this work
    #     print(p.starmap(countPrimes, zip(starts, repeat(rng))))
    #     t2 = time()
    #     p.close()
    #     print('time take: {} seconds:'.format(t2 - t1))
    #
