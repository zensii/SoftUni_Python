import re

is_valid_barcode_regex = r'@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+'
digits_regex = r'\d'
num_of_barcodes = int(input())

for i in range(num_of_barcodes):
    barcode = input()
    if re.findall(is_valid_barcode_regex, barcode):
        product_group = ''.join(re.findall(digits_regex, barcode))
        if not product_group:
            product_group = '00'
        print(f'Product group: {product_group}')
    else:
        print('Invalid barcode')
