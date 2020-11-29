


DNA = "ACGACTCGAGCTAGCGTACGAGCTCAGCTAGC"


def create_kmers(sequence, kmer_size, make_lower=False):
	"""
	This function creates a list of kmers of a given length from a given string
	:param sequence: The string to be converted into kmers
	:param kmer_size: The kmer size
	:return: Returns a list of the kmers
	"""
	
	index = 0

	kmers = []

	if make_lower:
		sequence = sequence.lower()

	while index + kmer_size <= len(sequence):

		# Remove the problematic line below
		index = 0

		kmers.append(sequence[index:index + kmer_size])
		
		index += 1
	
	return kmers

print(create_kmers(DNA, 7))


