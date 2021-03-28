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
    
    for exitCode := 0; exitCode != 99; {
        var value int
        //fmt.Println(comp.base)
        exitCode, value = comp.Process()
        if exitCode == 4 {
            fmt.Println(value)
        }
    }
}