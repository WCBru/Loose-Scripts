package main

import (
    "fmt"
    "strings"
    "strconv"
    "bufio"
    "os"
)

const (
    rel_less = -2
    rel_leq = -1
    rel_eq = 0
    rel_geq = 1
    rel_great = 2
)

type IntComp struct {
    program []int
    inputs []int
    index int
    base int
}

func (comp *IntComp) Init(prog []int) {
    comp.program = make([]int, len(prog))
    copy(comp.program, prog)
    comp.inputs = make([]int, 0)
    comp.index = 0
    comp.base = 0
}

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

func (comp *IntComp) Queue(value int) {
    comp.inputs = append(comp.inputs, value)
}

func (comp *IntComp) Dequeue() int {
    if len(comp.inputs) == 0 {
        panic("Queue empty")
    }
    output := comp.inputs[0]
    if len(comp.inputs) > 1 {
        comp.inputs = comp.inputs[1:]
    } else {
        comp.inputs = make([]int, 0)
    }
    return output
}

func (comp *IntComp) ValueAt(ind int) int {
    if (ind >= len(comp.program)) {
        comp.program = append(comp.program, make([]int, (ind + 1) - len(comp.program))...)
        //fmt.Println(comp.program)
    }
    
    return comp.program[ind]
}

func (comp *IntComp) ValueAtIndex(ind int) int {
    return comp.ValueAt(comp.ValueAt(ind))
}

func (comp *IntComp) SetValueAt(ind int, value int) {
    if (ind >= len(comp.program)) {
        comp.program = append(comp.program, make([]int, (ind + 1) - len(comp.program))...)
        //fmt.Println(comp.program)
    }
    
    comp.program[ind] = value
}

func (comp *IntComp) SetValueAtIndex(ind int, value int) {
    comp.SetValueAt(comp.ValueAt(ind), value)
}

func (comp *IntComp) GetParam(ind int, mode int) int {
    switch mode {
        case 2:
            return comp.ValueAt(comp.base + comp.ValueAt(ind))
        case 1:
            return comp.ValueAt(ind)
        default:
            return comp.ValueAtIndex(ind)
    }
}

func (comp *IntComp) Write(ind, value, mode int) {
    if mode == 1 {
        panic("Cannot write to immediate")
    }
    
    switch mode {
        case 2:
            comp.SetValueAt(comp.base + comp.ValueAt(ind), value)
        default:
            comp.SetValueAtIndex(ind, value)
    }
}

func (comp *IntComp) add() {
    p1, p2, p3, _ := split3(comp.ValueAt(comp.index))   
    param1, param2 := comp.GetParam(comp.index + 1, p1), comp.GetParam(comp.index + 2, p2)
    comp.Write(comp.index + 3, param1 + param2, p3)
    comp.index += 4
}

func (comp *IntComp) mult() {
    p1, p2, p3, _ := split3(comp.ValueAt(comp.index))   
    param1, param2 := comp.GetParam(comp.index + 1, p1), comp.GetParam(comp.index + 2, p2)
    comp.Write(comp.index + 3, param1 * param2, p3)
    comp.index += 4
}

func (comp *IntComp) save() {
    mode := (comp.ValueAt(comp.index) / 100) % 10
    if len(comp.inputs) == 0 {
        fmt.Print("Input: ")
        reader := bufio.NewReader(os.Stdin)
        text, _ := reader.ReadString('\n')
        intOut, _ := strconv.Atoi(strings.TrimSpace(text))
        comp.Write(comp.index + 1, intOut, mode)
    } else {
        comp.Write(comp.index + 1, comp.Dequeue(), mode)
    }
    
    comp.index += 2
}

func (comp *IntComp) output() int {
    mode := (comp.ValueAt(comp.index) / 100) % 10
    comp.index += 2
    return comp.GetParam(comp.index - 1, mode) 
}

func (comp *IntComp) bool_jmp(cond bool) {
    mode1, mode2, _ := split2(comp.ValueAt(comp.index))
    
    param1, param2 := comp.GetParam(comp.index + 1, mode1), comp.GetParam(comp.index + 2, mode2)
    
    if (param1 != 0) == cond {
        comp.index = param2
    } else {
        comp.index += 3
    }
}

func (comp *IntComp) cmp(mode int) {
    mode1, mode2, mode3, _ := split3(comp.ValueAt(comp.index))
    
    param1, param2 := comp.GetParam(comp.index + 1, mode1), comp.GetParam(comp.index + 2, mode2)
    
    cond := false
    switch mode {
        case rel_less:
            cond = param1 < param2
        case rel_leq:
            cond = param1 <= param2
        case rel_eq:
            cond = param1 == param2
        case rel_geq:
            cond = param1 >= param2
        case rel_great:
            cond = param1 > param2
    }
    
    if cond {
        comp.Write(comp.index + 3, 1, mode3)
    } else {
        comp.Write(comp.index + 3, 0, mode3)
    }
    
    comp.index += 4
}

func (comp *IntComp) moveBase() {
    comp.base += comp.GetParam(comp.index + 1, 
        (comp.ValueAt(comp.index) / 100) % 10)
    comp.index += 2
}

func (comp *IntComp) Process() (int, int) {
    opcode := comp.ValueAt(comp.index) % 100
    switch opcode {
        case 1:
            comp.add()
        case 2:
            comp.mult()
        case 3:
            comp.save()
        case 4:
            return opcode, comp.output()
        case 5:
            comp.bool_jmp(true)
        case 6:
            comp.bool_jmp(false)
        case 7:
            comp.cmp(rel_less)
        case 8:
            comp.cmp(rel_eq)
        case 9:
            comp.moveBase()
        case 99:
            return 99, 0
        default:
            panic(fmt.Sprintf("Unrecognised op %d", opcode))
    }
    
    return opcode, 0
}

