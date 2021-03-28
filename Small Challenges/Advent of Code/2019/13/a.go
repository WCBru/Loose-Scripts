package main

import (
    "fmt"
    "io/ioutil"
    "strings"
    "strconv"
)

func main() {
    data, err := ioutil.ReadFile("input.txt")
    if err != nil {
        panic(err)
    }
    
    partsStr := strings.Split(strings.TrimSpace(string(data)), ",")
    original := make([]int, len(partsStr))
    for ind, elm := range partsStr {
        intOut, _ := strconv.Atoi(elm)
        original[ind] = intOut
    }
    
    var comp IntComp
    comp.Init(original)
    counter, value := 0, 0
    
    for exitCode := 0; exitCode != 99; {
        for part := 0; part < 3; part++ {
            exitCode = 0
            for ; exitCode != 4 && exitCode != 99; {
                exitCode, value = comp.Process()
            }
        }
        
        if value == 2 {
            counter++
        }
    }
    
    fmt.Println(counter)
}