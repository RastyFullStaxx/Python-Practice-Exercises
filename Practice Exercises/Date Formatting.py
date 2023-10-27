# Write a function that converts a date string from one format to another.
import datetime

def format_date(input_date, input_format, output_format):
    parsed_date = datetime.datetime.strptime(input_date, input_format)
    formatted_date = parsed_date.strftime(output_format)
    return formatted_date

input_date = "2022-10-27"
input_format = "%Y-%m-%d"
output_format = "%d/%m/%Y"
formatted_date = format_date(input_date, input_format, output_format)
print(formatted_date)
