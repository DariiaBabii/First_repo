# real_len підраховує та повертає довжину рядка без наступних керівних символів: [\n, \f, \r, \t, \v]

def real_len(text):
    cleaned_string = text.replace("\n", "").replace("\f", "").replace("\r", "").replace("\t", "").replace("\v", "")

    return len(cleaned_string) 
        
