"""
Write a Python program to read each row from a given csv file and print a list of strings
"""
import csv

with open("sample.csv", "r") as file:
	csv_reader = csv.reader(file)
	for row in csv_reader:
		print((row))


		Mumma@914076