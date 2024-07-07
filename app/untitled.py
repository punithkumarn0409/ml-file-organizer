import docx

document = Document("Data set/Salts.docx")

for p in document.paragraphs:
	print(p)