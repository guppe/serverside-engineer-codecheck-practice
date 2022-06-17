import csv
import sys

def main():
    pathname = sys.argv[1]
    #with open(file=pathname) as csvfile:
        #reader = csv.DictReader(csvfile, lineterminator="\n")
    
    with open(pathname, "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        A = []
        for row in reader:
            A.append(row)
        
        #for i in range(len(row)):
            
    
if __name__ == "__main__":
    main()