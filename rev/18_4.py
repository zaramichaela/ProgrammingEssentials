matches_dict = {
 'GroupA': [
 {
 'Russia' : 5,
 'Saudi Arabia' : 0
 },
 {
 'Egypt' : 0,
 'Uruguay' : 1
 },
 {
 'Russia' : 3,
 'Egypt' : 1
 },
 {
 'Uruguay' : 1,
 'Saudi Arabia' : 0
 }
 ] ,
 'GroupB': [
 {
 'Morocco' : 0,
 'Iran' : 1
 },
 {
 'Portugal' : 3,
 'Spain' : 3
 },
 {
 'Portugal' : 1,
 'Morocco' : 0
 },
 {
 'Iran' : 0,
 'Spain' : 2
 }
 ]
}

t_russia = 0
t_uruguay = 0
t_saudi = 0
t_egypt = 0

for i in matches_dict:
    if i == "GroupA":
        listA = matches_dict[i]
        print(listA)
        for j in listA:
            t_russia += j.get("Russia", 0)
            t_uruguay += j.get("Uruguay", 0)
            t_saudi += j.get("Saudi Arabia", 0)
            t_egypt += j.get("Egypt", 0)
        print("Group A Result: ")
        print("-" * 6)
        print("Russia  %d" % t_russia)
        print("Uruguay  %d" % t_uruguay)
        print("Saudi Arabia  %d" % t_saudi)
        print("Egypt  %d" % t_egypt)

        dictA = {
        "Russia" : t_russia,
        "Uruguay" : t_uruguay,
        "Saudi Arabia" : t_saudi ,
        "Egypt": t_egypt
        }

highest = 0
highest_dict = {}
for i in dictA:
    if dictA[i] > highest:
        highest = dictA[i]
        highest_dict.clear()
        highest_dict[i] = highest

for i in highest_dict:
    print("-" * 6)
    print(i , "has the highest score in Group A with" , highest_dict[i] , "goals")
