# python3
import numpy as np

def parallel_processing(n, m, data):
    output = []
    seconds = 0
    datacount = 0
    threads = np.zeros(n)

    for i in range (m+1):
        for i in range (n):
            if threads[i] == 0:
                output.append(i)
                output.append(seconds)
                threads[i] = data[datacount]
                datacount = datacount+1
            threads[i] = threads[i]-1
        seconds = seconds+1
                
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    
    numbers = input()
    numbers = numbers.split()
    numbers = map(int, numbers)
    numbers = list(numbers)
    n = numbers[0]
    m = numbers[1]

    data = input()
    data = data.split()
    data = map(int, data)
    data = list(data)
    

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    #data = []

    # TODO: create the function
    result = parallel_processing(n,m,data)
    print(result)
    for i in range(0, len(result), 2):
        print(result[i], end=' ')
        if i+1 < len(result):
            print(result[i+1])
        else:
            print()
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
