# python3

def parallel_processing(n, m, data):
    output = []
    seconds = 0
    datacount = 0
    threads = [0]*n

    for i in range (m):
        for j in range (n):
            if threads[j] == 0:
                if datacount < len(data):
                    output.append(j)
                    output.append(seconds)
                    threads[j] = data[datacount]
                    datacount = datacount+1
                else: threads[j]=0
            threads[j] = threads[j]-1
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
    #print(result)
    for i in range(0, len(result), 2):
        print(result[i], end=' ')
        if i+1 < len(result):
            print(result[i+1])
        else:
            print()
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
