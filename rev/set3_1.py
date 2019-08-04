# part 1
def word_count(s):
   word_dict = {}
   list = s.split()
   for ch in list:
       word_dict[ch] = word_dict.get(ch, 0) + 1
   return word_dict
   
# part 2
def word_count(s):
   word_dict = {}
   list = s.split()
   for ch in list:
       word_dict[ch.lower()] = word_dict.get(ch.lower(), 0) + 1
   return word_dict

# part 3
def word_count(s):
   word_dict = {}
   list = s.split()
   for ch in list:
       word_dict[ch.lower()] = word_dict.get(ch.lower(), 0) + 1
   max_dict = {}
   max = 0
   for i in word_dict:
       if word_dict[i] > max:
           max = word_dict[i]
           max_dict.clear()
           max_dict[i] = word_dict[i]
       elif word_dict[i] == max:
           max_dict[i] = word_dict[i]
   return max_dict
