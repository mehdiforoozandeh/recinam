README
======

'Nucleic Acid Memory Reciprocal Converter' converts any file to a DNA sequence and vice versa.

>>> This package is developed to convert any type of file into DNA sequence and reversely back to the first file.
As nucleic acids are more stable when they have a reach ‘G+C’ content, this code attempts to set G and C as the most frequent nucleotides in the DNA output. Hence, a key is generated to address the origin of each nucleotide and this key file is requisite for the “sequence_to_file (name, Format)” function.

It contains two separate functions. 

>>> First one “file_to_sequence (name, Format)” gets two arguments. The name of your file and the format. For example (‘music’,’.mp3’) and it generates two files, one is the DNA sequence (.nuc) and the other is the key (key.nky).

>>> The second function “sequence_to_file (name, Format)”  brings back the initial file. It gets two arguments, the name of the DNA file (.nuc) and the output format (for example ‘.mp3’). 


Thanks for reading.
