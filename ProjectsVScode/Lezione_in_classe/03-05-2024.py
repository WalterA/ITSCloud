"""Verifica lezione 4"""
def blackjack(cards: list[int]) -> int:
    """Gioco del blackjack"""
    cards_sum: int = sum(cards)
    num_aces: int = cards.count(1) + cards.count(11)
    while cards_sum > 21 and num_aces > 0:
        cards_sum -= 10
        num_aces -= 1
    return cards_sum
#print(blackjack([1,10]))

def costruct_rectangle(area: float) -> list[float]:
    combos = []
    for width in range(1, area +1):
        for height in range(1, area +1):
            if width * height == area and width >=height:
                return [width , height] #cancella tutto cio che ce sotto
    #             combos.append([width, height])
    # min_diff:float=float("inf")
    # index_diff: int=0
    # for i in range(len(combos)):
    #     curr_diff:float =combos[i][0] - combos[i][1]
    #     if curr_diff <= min_diff:
    #         min_diff =curr_diff
    #         index_diff=i
    # return combos[index_diff]
# print(costruct_rectangle(4))
# print(costruct_rectangle(37))
# print(con_ret_opti(122122))

def con_ret_opti (area:float)-> list[int]:
    sqrt_area=int(area ** 0.5)
    for height in range (sqrt_area, 0, -1):
        if area % height == 0:
            width = area // height
            return [width, height]
#print(con_ret_opti(122122))
import re
def word_frequency (text:str, stopwords:list[str])->dict[str,int]:
    text = re.sub(r'[^\w\s]', '', text.lower()) #toglie da un stringa toglie tutti i simboli e rimpiazza con vuoto
    words=list()
    for word in text.split():
        if word not in stopwords:
            words.append(word)
    result={}
    #alternativa for word in words:
        #result[word] = result.get(word,0) +1
    for word in words:
        if word not in result:
            result[word]=1
        else:
            result[word]+=1
    return result
    #alternativa 2 result=counter(words)
    #return dict (result)
mus=[1,1,2,2,3,4,5,6,2,2,2]
from collections import Counter
def find_lhs(notes:list[int])->int:
    num_freq = dict(Counter(notes))
    max_lenght =0
    for num in num_freq:
        if num +1 in num_freq:
            max_lenght=max(max_lenght, num_freq[num] + num_freq[num+1])
    return max_lenght
#print(find_lhs(mus))

def third_max(gems:list[int]) -> int:
    gems = sorted(list(set(gems)), reverse=True)
    if len(gems) >= 3:
        return gems[2]
    else:
        return gems[0]
    
#print(third_max([3,2,1,4]))

def is_subsequence(s:str, t:str)-> bool:
    if s == "":
        return True
    s_pointer=0
    t_pointer=0
    while s_pointer < len(s) and t_pointer < len(t):
        if s[s_pointer] == t[t_pointer]:
            s_pointer += 1
        t_pointer += 1
    return s_pointer == len(s) 



