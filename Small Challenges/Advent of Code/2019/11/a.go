package main

import (
    "fmt"
    "io/ioutil"
    "strings"
    "strconv"
)


//   0
// 3 X 1
//   2
type Bot struct {
    x, y, dir int
}

func (bot *Bot) move(dir int) {
    if dir == 0 {
        bot.dir = (bot.dir + 3) % 4
    } else if dir == 1 {
        bot.dir = (bot.dir + 1) % 4
    }
    
    switch bot.dir {
        case 0:
            bot.y -= 1
        case 2:
            bot.y += 1
        case 1:
            bot.x += 1
        case 3:
            bot.x -= 1
    }
}

func renew_board(board [][]int, bot *Bot) [][]int {
    // Bot underflows off board
    if bot.x < 0 {
        for ind, row := range board {
            board[ind] = append([]int{2}, row...)
        }
        bot.x += 1
    } else if bot.y < 0 {
        // Add row to start and fill with 2
        board = append([][]int{make([]int, len(board[0]))}, board...)
        for i := 0; i < len(board[0]); i++ {
            board[0][i] = 2
        }
        bot.y += 1
    // Bot overflows off board
    } else if bot.x >= len(board[0]) {
        for ind, row := range board {
            board[ind] = append(row, 2)
        }
    } else if bot.y >= len(board) {
        // Add row to end and fill with 2
        board = append(board, [][]int{make([]int, len(board[0]))}...)
        for i := 0; i < len(board[0]); i++ {
            board[len(board) - 1][i] = 2
        }
    }
    
    return board
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
    
    var comp IntComp
    comp.Init(original)
    
    // Create board
    var bot Bot // defaults as 0
    board := make([][]int, 1)
    board[0] = []int{2}
    
    for exitCode := 0; exitCode != 99; {
        if board[bot.y][bot.x] == 1 {
            comp.Queue(1)
        } else {
            comp.Queue(0)
        }
        
        var value int
        // Loop 1
        for exitCode = 0; exitCode != 99 && exitCode != 4; {
            exitCode, value = comp.Process()
        }
        
        // Loop 2
        if exitCode == 4 {
            board[bot.y][bot.x] = value
            for exitCode = 0; exitCode != 99 && exitCode != 4; {
                exitCode, value = comp.Process()
            }
            if exitCode == 4 {
                bot.move(value)
                board = renew_board(board, &bot)
                //for _, row := range board {
                //    fmt.Println(row)
                //}
                
            }
        }
    
        
        //fmt.Println(comp.base)
    }
    
    paintCounter := 0
    for _, row := range board {
        for _, pt := range row {
            if pt != 2 {
                paintCounter++
            }
        }
    }
    
    fmt.Println(paintCounter)
}