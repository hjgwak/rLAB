CC = g++

SEQUENCE_OBJ = Sequence.o
SEQHASH_OBJ = SeqHash.o
OPTIONS_OBJ = Options.o
ERROR_OBJ = Error.o

BUILD_OBJ = Kmer_build.o
UNIQUE_OBJ = Kmer_unique.o
COMMON_OBJ = Kmer_common.o
KMER_OBJ = Kmer.o

COMMON_OBJS = $(SEQUENCE_OBJ) $(SEQHASH_OBJ) $(OPTIONS_OBJ) $(ERROR_OBJ)
OBJS = $(BUILD_OBJ) $(UNIQUE_OBJ) $(COMMON_OBJ) $(KMER_OBJ) $(COMMON_OBJS)

BUILD = Kmer_build
UNIQUE = Kmer_unique
COMMON = Kmer_common
KMER = Kmer

TARGET = $(BUILD) $(UNIQUE) $(COMMON) $(KMER)

FLAGS = -std=c++11 -stdlib=libc++

.SUFFIXES = .cc .o

all: $(TARGET)

clean:
	rm -f $(OBJS) $(TARGET)

# programs

$(BUILD) : $(BUILD_OBJ) $(COMMON_OBJS)
	$(CC) $(BUILD_OBJ) $(COMMON_OBJS) -o $@ $(FLAGS)

$(UNIQUE) : $(UNIQUE_OBJ) $(COMMON_OBJS)
	$(CC) $(UNIQUE_OBJ) $(COMMON_OBJS) -o $@ $(FLAGS)

$(COMMON) : $(COMMON_OBJ) $(COMMON_OBJS)
	$(CC) $(COMMON_OBJ) $(COMMON_OBJS) -o $@ $(FLAGS)

$(KMER) : $(KMER_OBJ) $(COMMON_OBJS)
	$(CC) $(KMER_OBJ) $(COMMON_OBJS) -o $@ $(FLAGS)

#object

$(SEQHASH_OBJ) : SeqHash.h SeqHash.cc
	$(CC) $(FLAGS) -c -o $@ SeqHash.cc
