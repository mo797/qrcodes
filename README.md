# Bulk QR Code Generator
---
Generate QR codes in bulk from csv files
## Installation
---
	$ pip install qrcode
## Usage
---
### Basic Usage
```
import generator from qrcode-generator

generator.generate_from('table.csv')
```

### CLI Usage
```
bulkqr --file table.csv --out ./qrcodes-dir
```

