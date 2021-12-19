
with open('inputs/day16','r') as f:
    inputs = [int(i.strip(),16) for i in f]



def decode_packet(binStr, cur=0, convert=True):
    if convert:
        binStr = bin(binStr)[2:]
        tmp = (4-len(binStr)%4)%4
        while tmp:
            binStr = '0' + binStr   # add leading 0s
            tmp -= 1

    version = int(binStr[cur: cur+3], 2)
    cur += 3
    pktType = int(binStr[cur: cur+3], 2)
    cur += 3

    if pktType == 4:    # literal
        literal = ''
        prefix = 1
        while prefix:
            prefix = int(binStr[cur], 2)
            cur += 1
            val = binStr[cur:cur+4]
            cur += 4
            literal += val
        value = int(literal, 2)
        return dict(values=[value], versions=[version], cursor=cur)

    else:               # operator
        output = {'values': [],
                  'versions': [version],
                  'cursor': -1}

        lenTypeId = int(binStr[cur], 2)
        cur += 1
        if lenTypeId:   # 11 bits represent how many sub packets
            numSubPackets = int(binStr[cur:cur+11], 2)
            cur += 11
            values = []
            for _ in range(numSubPackets):
                tmp = decode_packet(binStr, cur, convert=False)
                cur = tmp['cursor']
                output['values'].extend(tmp['values'])
                output['versions'].extend(tmp['versions'])

        else:           # 15 bits represent total len in bits
            totalLen = int(binStr[cur:cur+15], 2)
            cur += 15
            endCur = cur + totalLen
            while cur < endCur:
                tmp = decode_packet(binStr, cur, convert=False)
                cur = tmp['cursor']
                output['values'].extend(tmp['values'])
                output['versions'].extend(tmp['versions'])

        output['cursor'] = cur
        return output







# Example
tmp = """\
D2FE28
38006F45291200
EE00D40C823060
8A004A801A8002F478
620080001611562C8802118E34
C0015000016115A2E0802F182340
A0016C880162017C3686B18A3D4780"""

exampleInputs = [int(i.strip(),16) for i in tmp.split('\n')]

print(decode_packet(exampleInputs[0])['values'][0])
print(decode_packet(exampleInputs[1])['values'])
print(decode_packet(exampleInputs[2])['values'])
print(sum(decode_packet(exampleInputs[3])['versions']))
print(sum(decode_packet(exampleInputs[4])['versions']))
print(sum(decode_packet(exampleInputs[5])['versions']))
print(sum(decode_packet(exampleInputs[6])['versions']))


# Part 1
print(sum(decode_packet(inputs[0])['versions']))


# Part 2

