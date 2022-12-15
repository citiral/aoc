import sys

def binary_to_number(b):
    v = 0
    for c in b:
        v *= 2
        if c == "1":
            v += 1
    return v


def calc_ones(words):
    one_counts = [0] * word_length

    for word in words:
        for i in range(word_length):
            if word[i] == "1":
                one_counts[i] += 1
    return one_counts

def find_rating(words, find_biggest):
    i = 0
    while (len(words) > 1):
        count = len(words)
        one_counts = calc_ones(words)
        if one_counts[i] >= count / 2:
            most_common = "1"
        else:
            most_common = "0"
        
        if find_biggest:
            words = [w for w in words if w[i] == most_common]
        else:
            words = [w for w in words if w[i] != most_common]

        i += 1
    return binary_to_number(words[0])

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        words = [l.strip() for l in f.readlines()]

        word_length = len(words[0])
        one_counts = calc_ones(words)        

        oxygen_rating = find_rating(words, True)
        co2_rating = find_rating(words, False)

        print(oxygen_rating)
        print(co2_rating)

        gamma = ""
        epsilon = ""

        for c in one_counts:
            if c >= len(words) / 2:
                gamma += "1"
                epsilon += "0"
            else:
                gamma += "0"
                epsilon += "1"
    
        gamma = binary_to_number(gamma)
        epsilon = binary_to_number(epsilon)

        print(f"oxy: {oxygen_rating}, co2: {co2_rating}, *: {oxygen_rating*co2_rating}")