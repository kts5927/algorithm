from collections import deque
import sys
input = sys.stdin.read
write = sys.stdout.write


class AhoCorasick:
    def __init__(self):
        self.trie = [{}]  
        self.fail = [-1] 
        self.output = [False]  

    def insert(self, pattern):
        node = 0
        for char in pattern:
            if char not in self.trie[node]:
                self.trie.append({})
                self.fail.append(-1)
                self.output.append(False)
                self.trie[node][char] = len(self.trie) - 1
            node = self.trie[node][char]
        self.output[node] = True

    def build(self):
        queue = deque()
        for char, next_node in self.trie[0].items():
            self.fail[next_node] = 0
            queue.append(next_node)

        while queue:
            current_node = queue.popleft()
            for char, next_node in self.trie[current_node].items():
                fail_node = self.fail[current_node]
                while fail_node != -1 and char not in self.trie[fail_node]:
                    fail_node = self.fail[fail_node]
                self.fail[next_node] = self.trie[fail_node][char] if fail_node != -1 else 0
                self.output[next_node] |= self.output[self.fail[next_node]]
                queue.append(next_node)

    def search(self, text):
        node = 0
        for char in text:
            while node != -1 and char not in self.trie[node]:
                node = self.fail[node]
            if node == -1:
                node = 0
                continue
            node = self.trie[node][char]
            if self.output[node]:
                return "YES"
        return "NO"


data = input().splitlines()
N = int(data[0])
ac = AhoCorasick()

for i in range(1, N + 1):
    ac.insert(data[i])
ac.build()

Q = int(data[N + 1])
results = []

for i in range(N + 2, N + 2 + Q):
    results.append(ac.search(data[i]))

write("\n".join(results) + "\n")
