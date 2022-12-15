import sys

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        words = [l.strip() for l in f.readlines()]

        word_length = len(words[0])
        one_counts = [0] * word_length

        for word in words:
            for i in range(word_length):
                if word[i] == "1":
                    one_counts[i] += 1
        
        gamma = 0
        epsilon = 0

        for c in one_counts:
            gamma *= 2
            epsilon *= 2
            if c >= len(words) / 2:
                gamma += 1
            else:
                epsilon += 1
    
        print(f"g: {gamma}, e: {epsilon}, *: {gamma*epsilon}")