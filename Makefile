# Makefile for a simple Python project

# Define the source directory and the main file
SRCDIR = src
MAINFILE = $(SRCDIR)/main.py

# Define the build rule
build:
	@echo "Checking if $(MAINFILE) exists..."
	@if [ ! -f $(MAINFILE) ]; then \
		echo "Error: $(MAINFILE) not found."; \
		exit 1; \
	fi
	@echo "Build successful."

# Define the run rule
run:
	@echo "Installing required Python packages..."
	@pip install antlr4-python3-runtime
	@echo "Running $(MAINFILE)..."
	@python3 $(MAINFILE)

# Default target is 'build'
all: build

# Clean up
clean:
	@echo "Nothing to clean."