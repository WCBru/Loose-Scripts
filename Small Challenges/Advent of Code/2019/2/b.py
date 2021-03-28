TARGET = 19690720

if __name__ == "__main__":
    dataFile = open("input.txt")
    data = [int(i) for i in dataFile.read().split(",")]
    dataFile.close()

    for i in range(100):
        for j in range(100):
            nums = data.copy()
            nums[1] = i
            nums[2] = j
            
            try:
                index = 0
                while nums[index] != 99:
                    if nums[index] == 1:
                        nums[nums[index + 3]] = nums[nums[index + 2]] + nums[nums[index + 1]]
                    elif nums[index] == 2:
                        nums[nums[index + 3]] = nums[nums[index + 2]] * nums[nums[index + 1]]
                    else:
                        raise ValueError("Invalid OP Code")

                    index += 4    
            except:
                pass

            if (nums[0] == TARGET):
                    print(100 * i + j)
                    i = 99
                    break
