import csv
import sys
#import pandas as pd
import io

def main():
    pathname = sys.argv[1]
    
    with open(pathname, "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        csvdata = {}
        num = {}
        for row in reader:
            key = row[1]
            if (key in csvdata) == False:
                csvdata[key] = int(row[2])
            elif (key in csvdata) == True:
                csvdata[key] = csvdata[key] + int(row[2])
                if (key in num) == False:
                    num[key] = 1
                num[key] += 1                
        for i in num:
            csvdata[i] = int(csvdata[i] / int(num[i]))
        csvdata2 = sorted(csvdata.items(), key=lambda x:x[1], reverse=True)
        
        print("rank,player_id,mean_score")
        
        data = csvdata2[:10]
        n = len(data)
        for i in range(0, n):
           print(str(i + 1) + "," + data[i][0] + "," + str(data[i][1]))

          
    
if __name__ == "__main__":
    main()