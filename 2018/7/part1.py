from collections import defaultdict


class Parser(object):

    def __init__(self, lines):
        self.lines = lines
        self.tree = defaultdict(set)
        self.all_letters = set()
        self.answer = ''

    def build_tree(self):
        for line in self.lines:
            self.all_letters.add(line[0])
            self.all_letters.add(line[1])
            self.tree[line[1]].add(line[0])

    def build_string(self):
        all_letters_sorted = list(self.all_letters)
        print all_letters_sorted
        all_letters_sorted.sort()
        print all_letters_sorted
        while len(self.answer) < len(all_letters_sorted):
            for i in range(len(all_letters_sorted)):
                if self.can_be_placed(all_letters_sorted[i]):
                    self.answer += all_letters_sorted[i]
                    break

    def can_be_placed(self, letter):
        if letter in self.answer:
            return False
        for condition in self.tree[letter]:
            if condition not in self.answer:
                return False
        return True

    def perform_work(self):
        self.build_tree()
        self.build_string()
        print self.answer


lines = set([(x[5], x[36]) for x in open("input.txt").read().strip().split('\n')])
parser = Parser(lines)
parser.perform_work()
