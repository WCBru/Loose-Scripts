package main

import (
    "fmt"
    "bufio"
    "os"
    "strings"
    "sort"
)

const input string = "input.txt"

type Wire struct {
    X1, X2, Y1, Y2 int
}

func (w Wire) vert() bool {
    return w.X1 == w.X2
}

func checkError(ex error) {
    if ex != nil {
        fmt.Println(ex.Error())
        panic(ex)
    }
}

// A gripe: the lack of built-in simple functions like Python,
// and ternary statements makes writing your own simple functions necssary,
// taking up space in the file, making it less readable by cluttering an otherwise succinct file
func min (x, y int) int {
    if x < y {
        return x
    }
    return y
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}

func max (x, y int) int {
    if x > y {
        return x
    }
    return y
}

func createWires(reader *bufio.Reader) []Wire {
    line, err := reader.ReadString('\n')
    checkError(err)
    instr := strings.Split(strings.TrimSpace(line), ",")
    var output = make([]Wire, len(instr)) // Makes an array with zeroed elements
    
    x1, y1 := 0, 0
    var x2, y2 int
    
    for ind, elm := range instr { // For loop range extracts index and element
        x2, y2 = x1, y1
        
        var delta int
        _, err := fmt.Sscanf(string(elm[1:]), "%d", &delta)
        checkError(err)
        
        
        switch string(elm[0]) { // No breaks required
            case "U":
                y2 += delta
            case "D":
                y2 -= delta
            case "L":
                x2 -= delta
            case "R":
                x2 += delta
            default:
                panic("Instr direction not recognised")
        }
        
        output[ind] = Wire{x1, x2, y1, y2}
        x1, y1 = x2, y2
    }
    
    return output
}

func (wire Wire) printWire() {
    fmt.Printf("(%d, %d), (%d, %d)\r\n", wire.X1, wire.Y1, wire.X2, wire.Y2)
}

func printWires(wires []Wire) {
    for _, elm := range wires {
        elm.printWire()
    }
}

func diffProd(base, a, b int) int {
    return (base - a) * (base - b)
}

func (w1 Wire) findIntersection(w2 Wire) (int, int) {
    if w1.vert() {
        if w2.vert() && w1.X1 == w2.X1 {
            yInt := make([]int, 0, 4)
            if diffProd(w1.Y1, w2.Y1, w2.Y2) <= 0 {
                yInt = append(yInt, w1.Y1)
            }
            if diffProd(w1.Y2, w2.Y1, w2.Y2) <= 0 {
                yInt = append(yInt, w1.Y2)
            }
            if diffProd(w2.Y1, w1.Y1, w1.Y2) <= 0 {
                yInt = append(yInt, w2.Y1)
            }
            if diffProd(w2.Y2, w1.Y1, w1.Y2) <= 0 {
                yInt = append(yInt, w2.Y2)
            }
            
            if len(yInt) > 0 {
                sort.Ints(yInt)
                return w1.X1, yInt[0]
            }
        } else if !w2.vert() && diffProd(w1.X1, w2.X1, w2.X2) <= 0 && diffProd(w2.Y1, w1.Y1, w1.Y2) <= 0 {
            return w1.X1, w2.Y2
        }
    } else if !w2.vert() && w1.Y1 == w2.Y1 {
        xInt := make([]int, 0, 4)
        if diffProd(w1.X1, w2.X1, w2.X2) <= 0 {
            xInt = append(xInt, w1.X1)
        }
        if diffProd(w1.X2, w2.X1, w2.X2) <= 0 {
            xInt = append(xInt, w1.X2)
        }
        if diffProd(w2.X1, w1.X1, w1.X2) <= 0 {
            xInt = append(xInt, w2.X1)
        }
        if diffProd(w2.X2, w1.X1, w1.X2) <= 0 {
            xInt = append(xInt, w2.X2)
        }
        
        if len(xInt) > 0 {
            sort.Ints(xInt)
            return xInt[0], w1.Y1
        }
    } else if w2.vert() && diffProd(w2.X1, w1.X1, w1.X2) <= 0 && diffProd(w1.Y1, w2.Y1, w2.Y2) <= 0 {
        return w2.X1, w1.Y1
    }
    
    return 0, 0
}

func dist(x, y int) int {
    return abs(x) + abs(y)
}

func main() {
    // If an output is not used, place _ on the output
    file, err := os.Open(input)
    defer file.Close() // will execute when main exits
    // If a deferred function takes args, they are evaluated at deferral call
    checkError(err)
    
    fileReader := bufio.NewReader(file)
    
    wire1 := createWires(fileReader)
    wire2 := createWires(fileReader)
    
    bestDist := 0
    for ind, w1 := range wire1 {
        for _, w2 := range wire2[ind:] {
            crossX, crossY := w1.findIntersection(w2)
            if crossX != 0 || crossY != 0 {
                if bestDist == 0 {
                    bestDist = dist(crossX, crossY)
                } else {
                    bestDist = min(bestDist, dist(crossX, crossY))
                }
            }
        }
    }
    
    fmt.Println(bestDist)
}