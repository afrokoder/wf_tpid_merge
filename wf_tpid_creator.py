import csv

monthly_scorecards = open("/Users/XLNTMedia/Desktop/monthly_scorecardb.csv", "r")
wfcf = open("/Users/XLNTMedia/Desktop/wfcf.csv", "r")
results = open("/Users/XLNTMedia/Desktop/results.csv", "w")

csv_m = csv.reader(monthly_scorecards)
csv_w = csv.reader(wfcf)
# csv_r = csv.writer(results)

# for row in csv_m:
#     print(row)
#
# print('++===++++=++=++++++++')
# for row in csv_w:
#     print(row)
#
# print('++===++++=++=++++++++')

with results:
    writer = csv.writer(results)

    for m in csv_m:
        if m[0] != 'Wells Fargo Capital Finance':
            print(m)
            writer.writerow(m)

        else:
            for w in csv_w:
                if w[1] == m[1]:
                    z = [w[0],m[1]]
                    print(z)
                    writer.writerow(z)
