import sys

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        instructions = f.readlines()
        
        x = 0
        y = 0
        
        for i in instructions:
            words = i.split(' ')

            instr = words[0]
            val = int(words[1])
            
            if instr == "forward":
                x += val
            elif instr == "down":
                y += val
            elif instr == "up":
                y -= val
            else:
                print(f"invalid instruction {i}")
    
        print(f"x: {x}, y: {y}, mul: {x*y}")