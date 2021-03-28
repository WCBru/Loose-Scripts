def flipAtIndex(lst, index):
    toFlip = lst[:index]
    flipped = [toFlip[-1-char] for char in range(len(toFlip))]
    return flipped + lst[index:]

if __name__ == "__main__":
    bottom = int(input().strip())
    nums = [int(char) for char in input().strip().split()]
    flips = [[str(num) for num in nums[:]]]
    
    while bottom > 1:
        maximum = max(nums[:bottom])
        if maximum != nums[bottom-1]: # If the end value is not already max
            targetIndex = nums.index(maximum) # Find where max is

            # Extra flip to move max to top
            if targetIndex != 0:
                nums = flipAtIndex(nums, targetIndex+1) 
                flips.append([str(num) for num in nums[:]])

            # Move top to lowest current postition
            nums = flipAtIndex(nums, bottom)
            flips.append([str(num) for num in nums[:]])
            
        bottom -= 1

    print(str(len(flips)) + " flips: "
          + " -> ".join([",".join(flip) for flip in flips]))
