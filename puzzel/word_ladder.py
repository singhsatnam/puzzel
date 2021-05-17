from collections import defaultdict
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def find_neighbours(cur_word):
            word_list = list(cur_word)
            neighbours = []
            for i in range(l):
                cur_char = word_list[i]
                for char in alphabet:
                    if char == cur_char:
                        continue
                    word_list[i] = char
                    new_word = ''.join(word_list)
                    if new_word in word_set:
                        neighbours.append(new_word)
                word_list[i] = cur_char
            return neighbours

        # get wordlen l
        l = len(beginWord)
        # convert wordlist to wordset
        word_set = set(wordList)
        # create a list containing from a to z
        alphabet = [chr(i + ord('a')) for i in range(26)]
        # BFS
        queue = [beginWord]
        visited = {beginWord}
        # back_edges used to record back edges
        back_edges = defaultdict(list)
        # once endWord is found, set is_end to True
        is_end = False
        while queue:
            # each layer
            level_size = len(queue)
            append_set = set()
            for i in range(level_size):
                # each node
                cur_word = queue.pop(0)
                for next_word in find_neighbours(cur_word):
                    if next_word not in visited:
                        append_set.add(next_word)
                        back_edges[next_word].append(cur_word)
                    if next_word == endWord:
                        is_end = True
            # merge next level's words, using append_set to remove duplicative words
            visited.update(append_set)
            if is_end:
                break
            queue += list(append_set)
        if not is_end:
            return []
        res = []

        # backtracking using DFS
        def DFS(word, route):
            if word not in back_edges:
                route.reverse()
                res.append(route)
                return
            for i in back_edges[word]:
                DFS(i, route + [i])

        DFS(endWord, [endWord])
        return res


soln = Solution()
print(soln.findLadders(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"]))
