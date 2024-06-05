Build:
	mkdir Build
	mkdir Build/Comp1
	cp -R Orchid/Comp/ Build/Comp1
	mkdir Build/Comp2
	cp -R Orchid/Comp/ Build/Comp2
	mkdir Build/Comp3
	cp -R Orchid/Comp/ Build/Comp3
	mkdir Build/Public
	cp -R Orchid/Public/ Build/Public/
	cp Orchid/int.sh Build/
	cp Orchid/Sample.py Build/
Install:
	/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
	brew install python3
	
=======
# Number of nodes to build
NUM_NODES ?= 3

# Build target
Build:
	mkdir -p Build
	$(eval NODES := $(shell seq 1 $(NUM_NODES)))
	for node in $(NODES); do \
		mkdir -p Build/Comp$$node; \
		cp -R Orchid/Comp/ Build/Comp$$node; \
	done
	mkdir -p Build/Public
	cp -R Orchid/Public/ Build/Public/
	cp Orchid/int.sh Build/
	cp Orchid/Sample.py Build/

# Install target
Install:
	@if ! command -v brew >/dev/null 2>&1; then \
		echo "Homebrew not found. Installing Homebrew..."; \
		/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"; \
	else \
		echo "Homebrew is already installed."; \
	fi
	@if ! command -v python3 >/dev/null 2>&1; then \
		echo "Python3 not found. Installing Python3..."; \
		brew install python3; \
	else \
		echo "Python3 is already installed."; \
	fi