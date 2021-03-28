from intcode import Program

def input_command(bot, text):
    for letter in text:
        bot.add_input(ord(letter))

    bot.add_input(ord("\n"))

if __name__ == "__main__":
    # Solved by hand
    bot = Program("input.txt")
    input_command(bot, "NOT D T")
    input_command(bot, "OR C T")
    input_command(bot, "AND A T")
    input_command(bot, "NOT T J")
    input_command(bot, "WALK")
    bot.run()
    print(''.join([chr(c)
                   if c < 255 else str(c)
                   for c in bot.get_outputs()]))

