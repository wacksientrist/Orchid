# Number of nodes to build
NUM_NODES ?= 3

# Directories
BUILD_DIR := Build
PUBLIC_DIR := Orchid/Public
COMP_DIR := Orchid/Comp

# Java sources
JAVA_SRC := Main.java Instance.java

# Build target for Python and Java
Build: build_python build_java

# Build target for Python
build_python:
	mkdir -p $(BUILD_DIR)
	$(eval NODES := $(shell seq 1 $(NUM_NODES)))
	for node in $(NODES); do \
		mkdir -p $(BUILD_DIR)/Comp$$node; \
		cp -R $(COMP_DIR)/ $(BUILD_DIR)/Comp$$node; \
	done
	mkdir -p $(BUILD_DIR)/Public
	cp -R $(PUBLIC_DIR)/ $(BUILD_DIR)/Public/
	cp Orchid/int.sh $(BUILD_DIR)/
	cp Orchid/Sample.py $(BUILD_DIR)/

# Build target for Java
build_java:
	javac -d $(BUILD_DIR) $(JAVA_SRC)

# Install target for dependencies
Install: install_brew install_python

install_brew:
	@if ! command -v brew >/dev/null 2>&1; then \
		echo "Homebrew not found. Installing Homebrew..."; \
		/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"; \
	else \
		echo "Homebrew is already installed."; \
	fi

install_python:
	@if ! command -v python3 >/dev/null 2>&1; then \
		echo "Python3 not found. Installing Python3..."; \
		brew install python3; \
	else \
		echo "Python3 is already installed."; \
	fi

# Run the Java application

RunJava:

	cd $(BUILD_DIR); java -Xms512m -Xmx1024m -XX:+UseG1GC -cp ./ Main

# Clean the build directory
Clean:
	rm -rf $(BUILD_DIR)
