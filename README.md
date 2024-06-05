# Orchid

Orchid is a distributed computing library designed to facilitate node-based computations. This project provides both a Python and a Java implementation for processing commands asynchronously across multiple nodes.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/wacksientrist/Orchid/Java
    cd Orchid-Java
    ```

2. **Dependencies**:
    - Java Development Kit (JDK) version 8 or higher
    - Homebrew (for installing Python on macOS)
    - Python 3

## Building the Project

1. **Navigate to the project directory**:
    ```sh
    cd Orchid-Java
    ```

2. **Build the project**:
    ```sh
    make Build [NUM_NODES=<node_count> | <Nothing>]
    ```

3. **Install dependencies**:
    ```sh
    make Install
    ```
    - This will check for and install Homebrew and Python 3 if they are not already installed.

## Running the Java Application

1. **Run the Java program**:
    ```sh
    make RunJava
    ```
    - This will start the Orchid Java instance and continuously process commands.

## Usage

### Python Usage

1. **Import the Lib and Setup the Class**:
    - Import the Library Using "from Public.Orchid import Instance"
    - Setup some nodes using <your variable name> = Instance("<Node ID>")
    - Your node ids go from 1-3 By Default or from 1-<your node count> if you specify it when building

2. **Run Commands**:
    - 

3. **Read Commands**:
    -

## Cleaning the Build Directory

1. **Clean the build directory**:
    ```sh
    make Clean
    ```
## Extra Features

1. **There is a sample program**:
    - The sample program is named Sample.py
    - Sample.py is directly under your build directory, by default ./Build
    - The sample program uses relative paths.
    - To execute it, use this command "make Clean; make Build; cd Build; python3 Sample.py"
    - The sample program is NOT designed for more than 2 nodes, however its easy to expand if you want.
2. **There is a BenchMark script**:
    - The BenchMark script executes the sample program with the minimum number of nodes needed (2)
    - The BenchMark script times this and shuts down the nodes
    - The BenchMark script then executes an identical program that runs locally.
    - The identical program, is different in only that it runs all code directly.
    - This Limits the number of Nodes to 1, but ive seen upto 20x faster runs, so its usually faster

