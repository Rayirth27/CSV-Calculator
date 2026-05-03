import csv
import os

csv_path = os.path.join(os.path.dirname(__file__), 'calc.csv')      #Input File Path
output_path = os.path.join(os.path.dirname(__file__),'output.txt')  #Output File Path

def read():
    with open(csv_path, 'r', encoding='utf-8') as f:
        reading_cursor = csv.DictReader(f,fieldnames=['num1','operator','num2'])
        copy = list(reading_cursor) #converted the csv file into a dictionary
    return copy

def write(cp):
    with open(output_path,'w',encoding='utf-8',newline="") as out:
        write_obj = csv.DictWriter(out, fieldnames=['num1','operator','num2'],extrasaction='ignore')
        out.write("The data from the CSV file\n")
        write_obj.writeheader()
        write_obj.writerows(cp)
        
        result="\nCalculations begin\n"
        print(result)
        out.write(result)
    
        for row in cp:
            if not any(v.strip() for v in row.values() if isinstance(v,str) and v):   # skip empty rows
                continue
            try:
                n1 = float(row['num1'].strip())
                op = row['operator'].strip()
                n2 = float(row['num2'].strip())
            except ValueError:
                result = f"Value Error Exception received in {row}"
                print(result)
                out.write(result+"\n")
                continue
            if op == '+':
                result = f"Addition of {n1} + {n2} = {n1+n2}"
            elif op == '-':
                result = f"Subtraction of {n1} - {n2} = {n1-n2}"
            elif op == '*':
                result = f"Multiplication of {n1} * {n2} = {n1*n2}"
            elif op == '/':
                try:
                    result = f"Division of {n1} / {n2} = {n1/n2}"
                except ZeroDivisionError:
                    result ="Issue as 0 cannot be divisor"
            else:
                result = "Wrong Operator"
            print(result)
            out.write(result+"\n")
        
# def calc():
def main():
    data = read()
    write(data)
    print(f"\nResults are saved to : {output_path}")
main()