import barcode 
bar = barcode.get("ean13","12345678901234")
bar.save("bar.jpg")