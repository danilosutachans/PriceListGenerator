import re
import csv

with open('price_list.csv', 'r', encoding="utf8") as original_file:
    csv_reader = csv.reader(original_file)
    
    row_counter = 0
    product_codes = 0
    unuseful_rows = 0
    multiple_rows = 0
    
    
    with open('codes_first_gen.csv', 'w') as cleaned_file:
        
        csv_writer = csv.writer(cleaned_file)
        

        for row in csv_reader:

            description, product_code, product_price = row

            if len(product_code) <= 1:
                unuseful_rows += 1
            elif re.search(r"Part number", product_code) is not None:
                unuseful_rows += 1
            elif re.search(r"List price without tax in EUR", product_price) is not None:
                unuseful_rows += 1
            elif len(re.findall(r",", product_price)) > 1:
                multiple_rows += 1
            elif len(product_price) < 2:
                unuseful_rows += 1
            else:
                product_codes += 1
                print(f"{description}  |  {product_code}  |  {product_price}")
                csv_writer.writerow(row)

            row_counter += 1

print(f"File contains {row_counter} rows.\n")
print(f"{product_codes} rows contain Singular Product Codes.\n")
print(f"{multiple_rows} rows contain Non-Singular Product Codes.\n")
print(f"{unuseful_rows} rows are unuseful or product descriptions")