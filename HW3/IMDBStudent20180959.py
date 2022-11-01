import sys

count = dict()

args = sys.argv[1]
genre2 = 0
f = open(args, "rt")
for line in f:
    result =  line.split("::")
    genre = result[2]
    genre2 =  genre.split("|")
    new_gen = [l.strip() for l in genre2]
    #print(new_gen)
    #final = count_genre(genre2)
    for s in new_gen:
        try:
            count[s] = count[s] + 1
        except:
            count[s] = 1

args2 = sys.argv[2]
sys.stdout = open(args2, 'w')
for s in count:
   print(s, count[s])
f.close()
sys.stdout.close()

