import sys
import bitarray
import bitarray.util

versions = 0


def parse_literal(data):
    value = 0
    offset = 0
    while True:
        value = value << 4
        value += bitarray.util.ba2int(data[offset+1:offset+5])
        if data[offset] == 1:
            offset += 5
        else:
            return value, offset+5


def parse_packet(data):
    global versions
    version = bitarray.util.ba2int(data[0:3])
    versions += version
    type = bitarray.util.ba2int(data[3:6])
    if type == 4:
        value, offset = parse_literal(data[6:])
        return value, offset+6
    else:
        lengthtype = data[6]
        parsed = 0
        values = []
        
        if lengthtype == 0:
            length = bitarray.util.ba2int(data[7:22])
            while parsed < length:
                value, offset = parse_packet(data[22+parsed:])
                values.append(value)
                parsed += offset
            parsed += 22
        else:
            subpacketcount = bitarray.util.ba2int(data[7:18])
            parsed = 0
            while subpacketcount > 0:
                value, offset = parse_packet(data[18+parsed:])
                values.append(value)
                parsed += offset
                subpacketcount -= 1
            #print(values)
            parsed += 18

        value = 0
        if type == 0:
            #print("sum", values, sep='', end='')
            value = sum(values)
        elif type == 1:
            #print("prod", values, sep='', end='')
            value = values[0]
            for v in values[1:]:
                value *= v
        elif type == 2:
            #print("min", values, sep='', end='')
            value = min(values)
        elif type == 3:
            #print("max", values, sep='', end='')
            value = max(values)
        elif type == 5:
            #print(">", values, sep='', end='')
            if values[0] > values[1]:
                value = 1
            else:
                value = 0
        elif type == 6:
            #print("<", values, sep='', end='')
            if values[0] < values[1]:
                value = 1
            else:
                value = 0
        elif type == 7:
            #print("==", values, sep='', end='')
            if values[0] == values[1]:
                value = 1
            else:
              value = 0
        #print(" ->", value)

        return value, parsed


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = [l.strip() for l in f.readlines()]
        for line in lines:
            print(line)
            bits = bitarray.util.hex2ba(line)
            result = parse_packet(bits)
            print(result)