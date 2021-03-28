REQUIRED = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

class Document:
    def __init__(self, rawStr):
        fields = rawStr.split()
        self.fields = {f.split(":")[0]: f.split(":")[1] for f in fields}

    def validate(self):
        try:
            b = self.fields["byr"]
            i = self.fields["iyr"]
            e = self.fields["eyr"]
            h = self.fields["hgt"]
            hc = self.fields["hcl"]
            ec = self.fields["ecl"]
            p = self.fields["pid"]

            flags = [False for t in REQUIRED]
            flags[0] = len(b) == 4 and int(b) >= 1920 and int(b) <= 2002
            flags[1] = len(i) == 4 and int(i) >= 2010 and int(i) <= 2020
            flags[2] = len(e) == 4 and int(e) >= 2020 and int(e) <= 2030

            if h[-2:] == "cm":
                flags[3] = int(h[:-2]) >= 150 and int(h[:-2]) <= 193
            elif h[-2:] == "in":
                flags[3] = int(h[:-2]) >= 59 and int(h[:-2]) <= 76
            else:
                return False

            flags[4] = (len(hc) == 7 and hc[0] == "#"  and
                        all([(ord(c) <= 102 and ord(c) >= 97) or
                             int(c) > -1 for c in hc[1:]]))

            flags[5] = ec in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            flags[6] = len(p) == 9 and int(p) >= 0

            return all(flags)
        except Exception:
            return False

if __name__ == "__main__":
    data = open("input.txt").read().strip().split('\n\n')
    docs = [Document(f) for f in data]
    print(sum([d.validate() for d in docs]))
