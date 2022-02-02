import csv
from pathlib import Path

import qrcode


QR_DIR: str = './qrcodes'
CSV_FILE: str = './csv/list.csv'

def read_csv(filepath: str) -> None:
	with open(CSV_FILE) as csv_file:
		reader = csv.reader(csv_file, delimiter=',')
		next(reader)
		for line in reader:
			url: str = line[0]
			filename: str = line[1]
			img = qrcode.make(url)
			img.save(Path(QR_DIR) / filename)

if __name__ == '__main__':
	read_csv(CSV_FILE)