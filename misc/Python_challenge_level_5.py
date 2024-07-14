import pickle

dbfile = open('banner.pkl', 'rb')
db = pickle.load(dbfile)
print(db)

for line in db:
    # print(line)
    print(''.join([k*v for k, v in line]))
