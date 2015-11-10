CC = g++

PROGS = Unique_Kmer

all: $(PROGS)

clean:
	rm -f *.o $(PROGS)

# programs

Unique_Kmer: Unique_Kmer.o Sequence.o SeqHash.o Options.o Error.o
	$(CC) -o Unique_Kmer Unique_Kmer.o Sequence.o SeqHash.o Options.o Error.o

#objects
Sequence.o: Sequence.cc Sequence.h
	$(CC) -c Sequence.cc

SeqHash.o: SeqHash.cc SeqHash.h
	$(CC) -c SeqHash.cc

Options.o: Options.cc Options.h
	$(CC) -c Options.cc

Error.o: Error.cc Error.h
	$(CC) -c Error.cc

Unique_Kmer.o: Unique_Kmer.cc
	$(CC) -c Unique_Kmer.cc
