with open(r"C:\Users\HP\Desktop\sequence.fasta", "r") as file:
    lines = file.readlines()

sequence = "".join(lines[1:]).replace("\n", "").upper()


gc_count = sequence.count("G") + sequence.count("C")
gc_percentage = (gc_count / len(sequence)) * 100

complement = str.maketrans("ATGC", "TACG")
reverse_complement = sequence.translate(complement)[::-1]

rna = sequence.replace("T", "U")


#translation of the sequence into protein

codon_table = {
    "TTT":"F","TTC":"F","TTA":"L","TTG":"L",
    "TCT":"S","TCC":"S","TCA":"S","TCG":"S",
    "TAT":"Y","TAC":"Y","TAA":"*","TAG":"*",
    "TGT":"C","TGC":"C","TGA":"*","TGG":"W",
    "CTT":"L","CTC":"L","CTA":"L","CTG":"L",
    "CCT":"P","CCC":"P","CCA":"P","CCG":"P",
    "CAT":"H","CAC":"H","CAA":"Q","CAG":"Q",
    "CGT":"R","CGC":"R","CGA":"R","CGG":"R",
    "ATT":"I","ATC":"I","ATA":"I","ATG":"M",
    "ACT":"T","ACC":"T","ACA":"T","ACG":"T",
    "AAT":"N","AAC":"N","AAA":"K","AAG":"K",
    "AGT":"S","AGC":"S","AGA":"R","AGG":"R",
    "GTT":"V","GTC":"V","GTA":"V","GTG":"V",
    "GCT":"A","GCC":"A","GCA":"A","GCG":"A",
    "GAT":"D","GAC":"D","GAA":"E","GAG":"E",
    "GGT":"G","GGC":"G","GGA":"G","GGG":"G"
}
protein = ""
for i in range(0, len(sequence) - 2, 3):
    codon = sequence[i:i+3]
    protein += codon_table.get(codon, "X")

# to find the start codon
start = sequence.find("ATG")
stop = sequence.find("TAA", start)

if start != -1 and stop != -1:
    print("ORF:", sequence[start:stop+3])
else:
    print("No ORF found")

 #stop codons
    for i in range(start, len(sequence), 3):
     if sequence[i:i+3] in ["TAA", "TAG", "TGA"]:
        print("ORF:", sequence[start:i+3])
     break


#amino acid composition
for aa in set(protein):
    print(aa, protein.count(aa))

 #molecular  weight of the protein
weights = {"A":89,"R":174,"N":132,"D":133,"C":121,"E":147,"Q":146,"G":75,"H":155,"I":131,"L":131,"K":146,"M":149,"F":165,"P":115,"S":105,"T":119,"W":204,"Y":181,"V":117}
mw = sum(weights[aa] for aa in protein if aa != "*")

#basic sequence statistics
at = sequence.count("A") + sequence.count("T")
at_percent = (at / len(sequence)) * 100


print("\n=== DNA Sequence Toolkit ===")
print("1. Length")
print("2. GC%")
print("3. Nucleotide composition")
print("4. Reverse complement")
print("5. Transcription")
print("6. Translation")
print("7. ORF")
print("8. Amino-acid composition")
print("9. Molecular weight")
print("10. Motif search")

choice = input("Choose: ")

if choice == "1":
    print("Length:", len(sequence))
elif choice == "2":
    print("GC%:", gc_percentage)
elif choice == "3":
    print("A:", sequence.count("A"))
    print("T:", sequence.count("T"))
    print("G:", sequence.count("G"))
    print("C:", sequence.count("C"))
elif choice == "4":
    print("Reverse complement:", reverse_complement)
elif choice == "5":
    print("RNA:", rna)
elif choice == "6":
    print("Protein:", protein)
elif choice == "7":
    print("ORF:", sequence[start:stop+3])
elif choice == "8":
    for aa in set(protein):
        print(aa, protein.count(aa))
elif choice == "9":
    print("Molecular weight:", mw, "Da")
elif choice == "10":
    motif = input("Motif: ")
    print("Found at:", sequence.find(motif))