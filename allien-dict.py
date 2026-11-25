class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        rank={ch:idx for idx,ch in enumerate(order)}

        for i in range(len(words)-1):
            w1,w2=words[i],words[i+1]
            min_len=min(len(w1),len(w2))
            found_diff=False

            for j in range(min_len):
                if w1[j]!=w2[j]:
                    if rank[w1[j]]>rank[w2[j]]:
                        return False
                    found_diff=True
                    break

            if not found_diff and len(w1)>len(w2):
                return False
        return True