import sys
import os


class alkuler:
    def __init__(self, name):
        self.name = name
        # One element of column means an half hour
        self.table = [[0 for col in range(maxtime)] for row in range(5)]

    def __lt__(self, other):
        return self.name < other.name


def read_input(input_str):

    try :
        ifs=open(input_str, 'r')
    except :
        print("failed to open file %s. There might be no input files."%input_str)
        exit()

    lines = ifs.read().splitlines()

    # parse Name, Monday Table ----- Friday Table
    yoil = 0
    snulife = False
    for i, line in zip(range(len(lines)), lines):
        if i % 6 == 0:
            name = line

            # If the values of table mean Absolute time
            if(name[-1] == 's'):
                snulife = True
                name = name[:len(name)-1]
            else:
                snulife = False

            newalkuler = alkuler(name)
        else:
            tempTable = [CLASS_NOT_EXIST for row in range(maxtime)]
            Timevalues = line.split(' ')
            for Timevalue in Timevalues:
                Timelist = Timevalue.split(':')
                if Timelist[0] == 'x' or Timelist[0] == 'X':
                    break
                else:
                    startTime = int(float(Timelist[0])*2)
                    # length = int(float(Timelist[1])*2)
                    endTime = int(float(Timelist[1])*2)

                    if snulife:
                        startTime -= 8*2
                        endTime -= 8*2

                    for j in range(startTime, endTime):
                        tempTable[j] = CLASS_EXIST

            newalkuler.table[yoil] = tempTable.copy()
            yoil += 1
            if yoil%5 == 0 :
                Alkulers.append(newalkuler)
                yoil = 0
    ifs.close()

def print_alkulers_table(alkulers, mode = "시간표"):

    for i, yoil in zip(range(5),["월요일","화요일","수요일","목요일","금요일"]):
        print(yoil)
        for j in range(maxtime):
            print("%.1f ~ %.1f시 : \t"%(float(j)/2 + 8, float(j)/2 + 8.5), end = "")
            for alkuler in alkulers:
                if mode == "시간표":
                    if alkuler.table[i][j] == CLASS_EXIST:
                        print(alkuler.name + " ", end="")
                else:
                    if alkuler.table[i][j] == CLASS_NOT_EXIST:
                        print(alkuler.name + " ", end="")
            print("")
        print("------------------------------------------------")


if __name__ == "__main__":

    import glob
    import sys
    inputs = glob.glob("*.txt")

    maxtime = 28
    CLASS_NOT_EXIST = 0
    CLASS_EXIST = 1
    Alkulers = []

    for filename in inputs:
        read_input(filename)

    Alkulers_sorted = sorted(Alkulers)

    print("시간표 제출자 : ", end="")
    for alkuler in Alkulers_sorted:
        print(alkuler.name + " ", end = "")
    print("")

    print_alkulers_table(Alkulers_sorted,"공강")


# Print each person's result
    for alkuler in Alkulers_sorted:
        os.makedirs("results", exist_ok=True)
        sys.stdout = open("Results\\" + alkuler.name + ".txt", 'w')
        print_alkulers_table([alkuler])
        sys.stdout.close()

    exit()
