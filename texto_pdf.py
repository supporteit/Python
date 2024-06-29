 

import aspose.words as aw


doc = aw.Document("documento.txt")


doc.save("ficheiro.pdf", aw.SaveFormat.PDF)