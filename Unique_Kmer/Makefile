CC = g++

SEQUENCE_OBJ = Sequence.o
SEQHASH_OBJ = SeqHash.o
OPTIONS_OBJ = Options.o
ERROR_OBJ = Error.o

BUILD_OBJ = Kmer_build.o
UNIQUE_OBJ = Kmer_unique.o
COMMON_OBJ = Kmer_common.o

COMMON_OBJS = $(SEQUENCE_OBJ) $(SEQHASH_OBJ) $(OPTIONS_OBJ) $(ERROR_OBJ)
OBJS = $(BUILD_OBJ) $(UNIQUE_OBJ) $(COMMON_OBJ) $(COMMON_OBJS)

BUILD = Kmer_build
UNIQUE = Kmer_unique
COMMON = Kmer_common

TARGET = $(BUILD) $(UNIQUE) $(COMMON)

FLAGS = -std=c++11

.SUFFIXES = .cc .o

all: $(TARGET)

clean:
	rm -f $(OBJS) $(TARGET)

# programs

$(BUILD) : $(BUILD_OBJ) $(COMMON_OBJS)
	$(CC) -o $@ $(BUILD_OBJ) $(COMMON_OBJS)

$(UNIQUE) : $(UNIQUE_OBJ) $(COMMON_OBJS)
	$(CC) -o $@ $(UNIQUE_OBJ) $(COMMON_OBJS)

$(COMMON) : $(COMMON_OBJ) $(COMMON_OBJS)
	$(CC) -o $@ $(COMMON_OBJ) $(COMMON_OBJS)

#object

$(SEQHASH_OBJ) : SeqHash.h SeqHash.cc
	$(CC) $(FLAGS) -c -o $@ SeqHash.cc
