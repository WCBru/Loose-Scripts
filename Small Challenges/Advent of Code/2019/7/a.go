package main

import (
    "fmt"
    "io/ioutil"
    "strings"
    "strconv"
    "bufio"
    "os"
)

const LESS, LEQ, EQ, GEQ, GREAT int = -2, -1, 0, 1, 2

func split3(inp int) (int, int, int, int) {
    p3 := (inp / 10000) % 10
    p2 := (inp / 1000) % 10
    p1 :=  (inp / 100) % 10
    op := inp % 100
    return p1, p2, p3, op
}

func split2(inp int) (int, int, int) {
    p2 := (inp / 1000) % 10
    p1 :=  (inp / 100) % 10
    op := inp % 100
    return p1, p2, op
}

func add(src []int, ind int, mode1 int, mode2 int, mode3 int) {
    if mode3 == 1 {
        panic("Cannot write add result to immediate")
    }
    
    param1, param2 := src[ind + 1], src[ind + 2]
    if mode1 != 1 {
        param1 = src[src[ind + 1]]
    }
    
    if mode2 != 1 {
        param2 = src[src[ind + 2]]
    }
    
    src[src[ind + 3]] = param1 + param2
}

func mult(src []int, ind int, mode1 int, mode2 int, mode3 int) {
    if mode3 == 1 {
        panic("Cannot write multiply result to immediate")
    }
    
    param1, param2 := src[ind + 1], src[ind + 2]
    if mode1 != 1 {
        param1 = src[src[ind + 1]]
    }
    
    if mode2 != 1 {
        param2 = src[src[ind + 2]]
    }
    
    src[src[ind + 3]] = param1 * param2
}

func save(src []int, ind int, userInput bool, userValue int) {
    if userInput {
        fmt.Print("Input: ")
        reader := bufio.NewReader(os.Stdin)
        text, _ := reader.ReadString('\n')
        intOut, _ := strconv.Atoi(strings.TrimSpace(text))
        src[src[ind + 1]] = intOut
    } else {
        src[src[ind + 1]] = userValue
    }
    
}

func output(src []int, ind int) int {
    mode := (src[ind] / 100) % 10
    if mode == 1 {
        //fmt.Printf("%d\n", src[ind + 1])
        return src[ind + 1]
    } else {
        //fmt.Printf("%d\n", src[src[ind + 1]])
        return src[src[ind + 1]]
    }    
}

func bool_jmp(src []int, ind *int, cond bool) {
    mode1, mode2, _ := split2(src[*ind])
    
    param1, param2 := src[*ind + 1], src[*ind + 2]
    if mode1 != 1 {
        param1 = src[src[*ind + 1]]
    }
    
    if mode2 != 1 {
        param2 = src[src[*ind + 2]]
    }
    
    if (param1 != 0) == cond {
        *ind = param2
    } else {
        *ind += 3
    }
}

func cmp(src []int, ind int, mode int) {
    mode1, mode2, mode3, _ := split3(src[ind])
    
    if mode3 == 1 {
        panic("Cannot write compare result to immediate")
    }
    
    param1, param2 := src[ind + 1], src[ind + 2]
    if mode1 != 1 {
        param1 = src[src[ind + 1]]
    }
    
    if mode2 != 1 {
        param2 = src[src[ind + 2]]
    }
    
    cond := false
    switch mode {
        case LESS:
            cond = param1 < param2
        case LEQ:
            cond = param1 <= param2
        case EQ:
            cond = param1 == param2
        case GEQ:
            cond = param1 >= param2
        case GREAT:
            cond = param1 > param2
    }
    
    if cond {
        src[src[ind + 3]] = 1
    } else {
        src[src[ind + 3]] = 0
    }
}

func intcode_process(src []int, currentInd *int, userInput bool, userValue int) (int, int) {
    opcode := src[*currentInd] % 100
    switch opcode {
        case 1:
            p1, p2, p3, _ := split3(src[*currentInd])
            add(src, *currentInd, p1, p2, p3)
            *currentInd += 4
        case 2:
            p1, p2, p3, _ := split3(src[*currentInd])
            mult(src, *currentInd, p1, p2, p3)
            *currentInd += 4
        case 3:
            save(src, *currentInd, userInput, userValue)
            *currentInd += 2
        case 4:
            val := output(src, *currentInd)
            *currentInd += 2
            return opcode, val
        case 5:
            bool_jmp(src, currentInd, true)
        case 6:
            bool_jmp(src, currentInd, false)
        case 7:
            cmp(src, *currentInd, LESS)
            *currentInd += 4
        case 8:
            cmp(src, *currentInd, EQ)
            *currentInd += 4
        default:
            panic(fmt.Sprintf("Unrecognised op %d", opcode))
    }
    
    return opcode, 0
}

func intcode_loop(src []int, inputs []int) int {
    inpInd, progInd := 0, 0
    for ; progInd < len(src); {
        var op, val int
        if (inpInd < len(inputs)) {
            op, val = intcode_process(src, &progInd, false, inputs[inpInd])
            if op == 3 {
                inpInd++
            }
        } else {
            op, val = intcode_process(src, &progInd, true, 0)
        }
        
        if op == 4 {
            return val
        }
    }
    
    return 0
}

func chain_loops(src []int, inputs []int) int {
    nextInp := 0
    progCopy := make([]int, len(src))
    copy(progCopy, src)
    for _, amp := range inputs {
        nextInp = intcode_loop(progCopy, []int{amp, nextInp})
    }
    return nextInp
}

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
    
    // Heaps alg
    amps, states := make([]int, 5), make([]int, 5)
    for i := 0; i < 5; i++ {
        amps[i] = i
        states[i] = 0
    }
    
    highest := chain_loops(original, amps)
    
    for i := 0; i < 5; {
        if states[i] < i {
            temp := amps[i]
            if i % 2 == 0 {
                amps[i] = amps[0]
                amps[0] = temp
            } else {
                amps[i] = amps[states[i]]
                amps[states[i]] = temp
            }
            
            newVal := chain_loops(original, amps)
            if newVal > highest {
                highest = newVal
            }
            
            states[i]++
            i = 0
        } else {
            states[i] = 0
            i++
        }
    }
    
    fmt.Println(highest)
}