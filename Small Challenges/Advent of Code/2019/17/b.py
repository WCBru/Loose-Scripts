from intcode import Program

# solved on paper
main = "A,B,A,B,C,A,B,C,A,C\n"
A = "R,6,L,6,L,10\n"
B = "L,8,L,6,L,10,L,6\n"
C = "R,6,L,8,L,10,R,6\n"

if __name__ == "__main__":
    camera = Program("input.txt")
    camera.program[0] = 2
    
    [camera.add_input(ord(c)) for c in main]
    [camera.add_input(ord(c)) for c in A]
    [camera.add_input(ord(c)) for c in B]
    [camera.add_input(ord(c)) for c in C]

    # no camera output
    camera.add_input(ord("n"))
    camera.add_input(ord("\n"))

    camera.run()
    print(camera.get_outputs()[-1])
