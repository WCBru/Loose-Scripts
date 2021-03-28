REQUIRED = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

class Document:
    def __init__(self, rawStr):
        fields = rawStr.split()
        self.fields = {f.split(":")[0]: f.split(":")[1] for f in fields}

    def has_fields(self, names):
        return all([name in self.fields.keys() for name in names])

if __name__ == "__main__":
    data = open("input.txt").read().strip().split('\n\n')
    docs = [Document(f) for f in data]
    print(sum([d.has_fields(REQUIRED) for d in docs]))
