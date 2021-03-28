from intcode import Program

if __name__ == "__main__":
    total = 0
    for x in range(50):
        for y in range(50):
            bot = Program("input.txt")
            bot.add_input(x)
            bot.add_input(y)
            bot.run()
            total += bot.last_output

    print(total)
