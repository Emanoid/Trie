class Trie:
    def __init__(self):
        self._head = {}

    def add(self, word):
        node = self._head
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node['*'] = True

    def search(self,word):
        node = self._head
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        if '*' in node:
            return True
        else:
            return False

    def print(self):
        print(self._head)
##########################################################################33
T = Trie()
T.add('head')
T.add('tail')
T.add('hello')
#T.print()
print(T.search('tail'))
print(T.search('hello'))
print(T.search('hell'))
