# Makefile for C utils library

CC = gcc
CFLAGS = -Wall -fPIC
LDFLAGS = -shared

# Directories
UTILS_DIR = utils
BUILD_DIR = build

# Targets
MATH_SRC = $(UTILS_DIR)/math_utils.c
STRING_SRC = $(UTILS_DIR)/string_utils.c

MATH_LIB = $(BUILD_DIR)/libmath_utils.so
STRING_LIB = $(BUILD_DIR)/libstring_utils.so

all: $(MATH_LIB) $(STRING_LIB)

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

$(MATH_LIB): $(MATH_SRC) | $(BUILD_DIR)
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $<

$(STRING_LIB): $(STRING_SRC) | $(BUILD_DIR)
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $<

clean:
	rm -rf $(BUILD_DIR)
