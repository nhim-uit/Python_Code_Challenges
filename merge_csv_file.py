# Linked Learning - Python Code Challenges
# 22 Jul, 2025
# merge csv file
import csv


def merge_csv(*files):
    all_rows = []
    all_headers = set()

    for i in files:
        with open(i, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            all_headers.update(reader.fieldnames)
            for row in reader:
                all_rows.append(row)

    with open('output.csv', 'w', encoding='utf-8', newline='') as out_f:
        writer = csv.DictWriter(out_f, fieldnames=all_headers)
        writer.writeheader()
        for row in all_rows:
            writer.writerow(row)


if __name__ == '__main__':
    merge_csv('file1.csv', 'file2.csv')
