class Group:
    def __init__(self, rows):
        self.size = len(rows)
        self.ans = {}
        for row in rows:
            for c in row:
                if c in self.ans:
                    self.ans[c] += 1
                else:
                    self.ans[c] = 1

    def sum(self):
        return len(self.ans.keys())

    def all_sum(self):
        return sum([self.ans[g] == self.size for g in self.ans.keys()])

if __name__ == "__main__":
    groups = [Group(g.split('\n')) for g in
              open("input.txt").read().strip().split("\n\n")]

    print(sum([g.sum() for g in groups]))
    print(sum([g.all_sum() for g in groups]))
