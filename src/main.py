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
                csvdata[key] = row[2]
            elif (key in csvdata) == True:
                csvdata[key] = int(csvdata[key]) + int(row[2])
                if (key in num) == False:
                    num[key] = 1
                num[key] += 1                
        #print(csvdata)
        #print(num)
        
        for i in num:
            csvdata[i] = str(int(int(csvdata[i]) / int(num[i])))
        print(csvdata)

          
    
if __name__ == "__main__":
    main()