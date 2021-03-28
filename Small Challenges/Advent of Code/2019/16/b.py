def apply_transform(signal, start):
    output = [0 for x in signal]

    # Uses integral array, whose elements are the cumulative sum of elements
    # in the signal. This turns which group of additions and substractions into
    # a single operation: the difference between endpoints
    integral = [signal[0] for x in range(len(signal) + 1)]
    for x in range(1, len(integral)):
        integral[x] = integral[x - 1] + signal[x - 1]

    # Iterate through each starting element
    for ind in range(len(signal)):
        curr = ind # index in output
        runLength = start + ind # length of each run
        total = 0 # current run total
        
        while curr < len(signal):
            addmax = min(len(integral) - 1, curr+runLength)
            submin = min(len(integral) - 1, curr+2*runLength)
            submax = min(len(integral) - 1, curr+3*runLength)
            
            total += integral[addmax] - integral[curr]
            total -= integral[submax] - integral[submin]

            curr += 4*runLength

        # Update ouptut array
        output[ind] = abs(total) % 10
    
    return output

if __name__ == "__main__":
    signal = [int(x) for x in open("input.txt").read().strip()]
    #signal = [int(x) for x in "02935109699940807407585447034323"]
    
    fullSig = [0 for x in range(len(signal)*10000)]
    for i in range(10000):
        fullSig[i*len(signal):(i+1)*len(signal)] = signal
    start = int(''.join([str(x) for x in signal[:7]]))
    truncSig = fullSig[start:] # truncate at skipped digits

    for x in range(100):
        print(x)
        truncSig = apply_transform(truncSig, start)
        
    print(''.join([str(x) for x in truncSig[0:8]]))
