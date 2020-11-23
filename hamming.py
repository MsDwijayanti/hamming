def distance(strand_a, strand_b):
    if len(strand_a)!=len(strand_b):
        raise Exception("The length of both strand must be equal")
    else:
        count=0
        for letter1, letter2 in zip(strand_a, strand_b):
            if letter1 != letter2:
                count += 1
        print("The Hamming distance is :"+str(count))

distance ("TTTACATAGAATACACAGCCGGGACAGGGTATAAC", "TTTACATATGTTTTATCGTCAAGACGCTGTATAAC")

