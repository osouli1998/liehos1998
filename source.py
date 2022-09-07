import csv
# For the average
from statistics import mean 

def calculate_averages(grades, mean):
    with open("G:\python\elementary\grades.csv") as infile:
        reader=csv.reader(infile)
        with open("G:\python\elementary\mean.csv" , "w", newline="") as outfile:
            writer = csv.writer(outfile)
            for row in reader:
                name = row[0]
                grade_mean = (float(grade) for grade in row [1:])
                writer.writerow([row[0], mean(grade_mean)])




def calculate_sorted_averages(input_file_name, output_file_name):
    


def calculate_three_best(input_file_name, output_file_name):
    


def calculate_three_worst(input_file_name, output_file_name):
        


def calculate_average_of_averages(input_file_name, output_file_name):
