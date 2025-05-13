import csv
import json

# 输入 CSV 文件名
csv_file = 'profiles1.csv'
# 输出 JSON 文件名
json_file = 'profiles1.json'

data = []

# 读取 CSV 文件
with open(csv_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)

# 写入 JSON 文件
with open(json_file, 'w', encoding='utf-8') as jsonfile:
    json.dump(data, jsonfile, indent=2, ensure_ascii=False)

print(f"{len(data)} rows converted from CSV to JSON.")
