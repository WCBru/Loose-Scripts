from intcode import Program

def test_point(row, col):
    bot = Program("input.txt")
    bot.add_input(row)
    bot.add_input(col)
    bot.run()
    return bot.last_output

def find_col(row, start=0):
    col = start
    while True:
        if test_point(row, col) == 1:
            return col
        else:
            col += 1

if __name__ == "__main__":
    row = 100
    col = find_col(row)      

    while True:
        row += 1
        col = find_col(row, start=col)
        if test_point(row - 99, col + 99) == 1:
            print((row - 99) * 10000 + col)
            break
        
