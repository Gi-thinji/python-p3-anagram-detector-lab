# your code goes here!
class Anagram:
    def __init__(self,word):
        self.word = word

    # def is_anagram(self, word1, word2):
    #     return sorted(word1) == sorted(word2)
    
    def match(self,input_list):
        anagram_list=[]
        for word in input_list:
            if sorted(word) == sorted(self.word):
                anagram_list.append(word)
        return anagram_list
        
print(Anagram("enlist").match(["listen", "poison", "hello"]))
