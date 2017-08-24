import csv
import  pandas as pd

with open('data.csv','r') as datafile:
    file_reader = csv.reader(datafile)
    msg_list = list(file_reader)


# print(msg_list)

sub = '38='

for element in msg_list:
    print(element)
    if sub in element:
        print(element)
        print("\n")





# mylist = ['abc123', 'def456', 'ghi789', 'ABC987', 'aBc654']
# sub = 'abc'
#
# print("\n".join(s for s in mylist if sub.lower() in s.lower()))

# # Read the CSV into a pandas data frame (df)
# #   With a df you can do many things
# #   most important: visualize data with Seaborn
# df = pd.read_csv('filename.csv', delimiter=',')
#
# # Or export it in many ways, e.g. a list of tuples
# tuples = [tuple(x) for x in df.values]
#
# # or export it as a list of dicts
# dicts = df.to_dict().values()
