# Makefile for a simple Python project

# Define the source directory and the main file
SRCDIR = src
MAINFILE = $(SRCDIR)/main.py

# Define the build rule
build:
	@if [ ! -f $(MAINFILE) ]; then \
		exit 1; \
	fi

# Define the run rule
run:
	@python3 $(MAINFILE)

# Default target is 'build'
all: build