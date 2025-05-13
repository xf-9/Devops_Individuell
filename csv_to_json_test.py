import unittest
import csv
import json
import os
import atexit

# 全局变量保存信息
info = {
    "csv_columns": None,
    "csv_rows": None,
    "json_fields": None,
    "json_records": None
}

# 退出时统一输出
def print_summary():
    print("\n[CSV] Number of columns:", info["csv_columns"])
    print("[CSV] Number of data rows:", info["csv_rows"])
    print("[JSON] Sample record fields:", info["json_fields"])
    print("[JSON] Number of records:", info["json_records"])

atexit.register(print_summary)


class TestCSVtoJSON(unittest.TestCase):
    def setUp(self):
        self.csv_file = 'profiles1.csv'
        self.json_file = 'data.json'
        
        self.assertTrue(os.path.exists(self.csv_file), "CSV file not found")
        self.assertTrue(os.path.exists(self.json_file), "JSON file not found")

        with open(self.csv_file, encoding='utf-8') as f:
            self.csv_data = list(csv.reader(f))
        
        with open(self.json_file, encoding='utf-8') as f:
            self.json_data = json.load(f)

    def test_csv_has_12_columns(self):
        header = self.csv_data[0]
        info["csv_columns"] = len(header)
        self.assertEqual(info["csv_columns"], 12)

    def test_csv_has_over_900_rows(self):
        info["csv_rows"] = len(self.csv_data) - 1
        self.assertGreaterEqual(info["csv_rows"], 900)

    def test_json_has_required_fields(self):
        required_fields = set(self.csv_data[0])
        sample_record = self.json_data[0]
        info["json_fields"] = set(sample_record.keys())
        self.assertTrue(required_fields.issubset(info["json_fields"]))

    def test_json_has_over_900_records(self):
        info["json_records"] = len(self.json_data)
        self.assertGreaterEqual(info["json_records"], 900)


if __name__ == '__main__':
    unittest.main()
