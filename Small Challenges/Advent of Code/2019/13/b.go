package main

import (
    "fmt"
    "io/ioutil"
    "strings"
    "strconv"
    "os"
    "os/exec"
)

func sgn(num int) int {
    if num > 0 {
        return 1
    } else if num < 0 {
        return -1
    } else {
        return 0
    }
}

func print_screen(board [][]int, score int) {
    cmd := exec.Command("cmd", "/c", "cls")
    cmd.Stdout = os.Stdout
    cmd.Run()
    
    fmt.Print("Score: ")
    fmt.Println(score)
    for _, row := range board {
        for _, block := range row {
            switch block {
                case 0:
                    fmt.Print(" ")
                case 1:
                    fmt.Print("#")
                case 2:
                    fmt.Print("+")
                case 3:
                    fmt.Print("=")
                case 4:
                    fmt.Print("o")
            }
        }
        fmt.Print("\n")
    }
}

func add_point(board [][]int, x, y, value int) [][]int {
    if (x >= len(board[0])) {
        for ind, row := range board {
            board[ind] = append(row, make([]int, x - (len(board[0]) - 1))...)
        }
    }
    
    if (y >= len(board)) {
        for i := 0; i < y - (len(board) - 1); i++ {
            board = append(board, make([]int, len(board[0])))
        }
    }
    
    board[y][x] = value
    
    return board
}

// Play's itself
// Uncomment print screen on line 123 for real-time
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
    
    original[0] = 2 // Set by problem
    
    var comp IntComp
    comp.Init(original)
    value, score := 0, 0
    drawn := false
    
    savedx := 0
    
    board := make([][]int, 0)
    board = append(board, []int{0})
    
    for exitCode := 0; exitCode != 99; {
        exitCode, value = comp.Process()
        
        // First output coord
        if exitCode == 4 {
            x := value
            
            // Second coord
            exitCode = 0
            for ; exitCode != 4 && exitCode != 99; {
                exitCode, value = comp.Process()
            }
            if exitCode == 4 {
                y := value
                exitCode = 0
                for ; exitCode != 4 && exitCode != 99; {
                    exitCode, value = comp.Process()
                }
                
                if exitCode == 4 {
                    if value == 3 {
                        savedx = x
                    } else if value == 4 {
                        comp.Queue(sgn(x - savedx))
                    }
                    if x == -1 && y == 0 {
                        score = value
                    } else {
                        board = add_point(board, x, y, value)
                        if drawn {
                            //print_screen(board, score)
                        }
                    }
                }
            }
        }
        
        if exitCode == 3 {
            drawn = true
        }
    }
    
    print_screen(board, score)
}