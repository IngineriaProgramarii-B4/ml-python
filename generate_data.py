import csv
from random import randint


def get_subjects():
    f = open('./courses.csv', 'r')
    reader = csv.reader(f, delimiter=',')
    line_count = 0
    subjects = set()

    for row in reader:
        if line_count == 0:
            line_count += 1
            continue

        subjects.add(row[5])
        line_count += 1

    return subjects


def data_generator():
    data = []
    header = ['subject', 'hours', 'credits']
    data.append(header)

    row = []
    subjects = get_subjects()
    for subject in subjects:
        row.append(subject)
        credits = randint(4, 6)
        row.append(randint(0, 70) + credits * 2)
        row.append(credits)
        data.append(row)
        row = []

    return data


def write_data():
    f = open('./generated_data.csv', 'w')
    writer = csv.writer(f)
    data = data_generator()
    for row in data:
        writer.writerow(row)
    f.close()
    pass
