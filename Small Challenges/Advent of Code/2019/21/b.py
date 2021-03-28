from intcode import Program

def input_command(bot, text):
    for letter in text:
        bot.add_input(ord(letter))

    bot.add_input(ord("\n"))

if __name__ == "__main__":
    # Referred to a soln, not wanting to solve this one
    bot = Program("input.txt")
    input_command(bot, "NOT B J")
    input_command(bot, "NOT C T")
    input_command(bot, "OR T J")
    input_command(bot, "AND D J")
    input_command(bot, "AND H J")
    input_command(bot, "NOT A T")
    input_command(bot, "OR T J")
    input_command(bot, "RUN")
    bot.run()
    print(''.join([chr(c)
                   if c < 255 else str(c)
                   for c in bot.get_outputs()]))

