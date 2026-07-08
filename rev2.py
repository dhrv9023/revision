# valid anagram
def anagram(s,t):
    return sorted(s)==sorted(t)
            


s = "anagram" 
t = "nagaram"
print(anagram(s,t))