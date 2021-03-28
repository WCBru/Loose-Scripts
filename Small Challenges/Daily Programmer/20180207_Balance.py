if __name__ == "__main__":
    length = input()
    numbers = [int(num) for num in input().split()]
    
    if (length == len(numbers)):
        outputs = []
        leftSum, rightSum = (0,sum(numbers))
        
        # Track the changes in sums through each element
        for index in range(len(numbers)):
            leftSum += numbers[index-1] if index > 0 else 0
            rightSum -= numbers[index]
            if leftSum == rightSum:
                outputs.append(str(index))
    
        print(" ".join(outputs))
    else:
        print("Length given and inputs given don't match")
