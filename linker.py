#!/usr/bin/env python3
class Obj:
    def __init__(self, magicnumber, nsegs, nsyms, nrels, segs, syms, rels, data):
        self.magicnumber = magicnumber
        self.nsegs = nsegs
        self.nsyms = nsyms
        self.nrels = nrels
        # name start_logic_addr len trait
        self.segs = segs
        # name vlaue seg type
        self.syms = syms
        # loc seg ref type
        self.rels = rels
        # 0x? 0x?
        self.data = data
    def display_info(self):
        print("magicnumber: ", magicnumber)
        print("nsegs: ", nsegs)
        print("nsyms: ", nsyms)
        print("nrels: ", nrels)
        print("segs: ", segs)
        print("syms: ", syms)
        print("rels: ", rels)
        print("data: ", data)
    

with open('obj.txt', 'r') as file:
    magicnumber = -1
    nsegs = -1
    nsyms = -1
    nrels = -1
    segs = []
    syms = []
    rels = []
    data = []
    segidx = 1
    symidx = 1
    for line_number, line in enumerate(file, start=1):
        linedata = line.strip().split()
        # print(linedata)
        if line_number == 1:
            magicnumber = linedata
        elif line_number == 2:
            nsegs, nsyms, nrels = map(int, linedata)
        elif line_number <= 2 + nsegs:
            segs.append([segidx, linedata[0], int(linedata[1]), int(linedata[2]), linedata[3]])
            segidx = segidx + 1
        elif line_number <= 2 + nsegs + nsyms:
            syms.append([symidx, linedata[0], int(linedata[1], 16), int(linedata[2]), linedata[3]])
            symidx = symidx + 1
        elif line_number <= 2 + nsegs + nsyms + nrels:
            rels.append([int(linedata[0], 16), int(linedata[1]), int(linedata[2]), linedata[3]])
        else:
            data.append([int(linedata[0], 16), int(linedata[1], 16)])

    obj = Obj(magicnumber, nsegs, nsyms, nrels, segs, syms, rels, data)
    obj.display_info();