package main

import (
    "fmt"
)

const LOWERLIMIT int = 273025
const UPPERLIMIT int = 767253

func count_valid_substrings(length int, lastInt int, doubleDone bool) int {
    // Final digit
    if (length == 1) {
        if (doubleDone) { // Can be any int >= lastInt
            return 10 - lastInt
        } else { // Require double digit
            return 1
        }
    } else { // Not final digit, iterate through
        sum := 0
        for i := lastInt; i < 10; i++ {
            sum += count_valid_substrings(length - 1, i, doubleDone || (i == lastInt))
        }
        return sum
    }
}

func main() {
    total1 := count_valid_substrings(5, 7, false)
    for i := 3; i < 7; i++ {
        total1 += count_valid_substrings(5, i, false)
    }
    //total += count_upper_digit(UPPERLIMIT)
    fmt.Println(total1)
}