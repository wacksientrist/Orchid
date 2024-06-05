# Orchid

Orchid is a distributed computing library designed to facilitate node-based computations. This project provides both a Python and a Java implementation for processing commands asynchronously across multiple nodes.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/orchid-java.git
    cd orchid-java
    ```

2. **Dependencies**:
    - Java Development Kit (JDK) version 8 or higher
    - Homebrew (for installing Python on macOS)
    - Python 3

## Building the Project

1. **Navigate to the project directory**:
    ```sh
    cd orchid-java
    ```

2. **Build the project**:
    ```sh
    make Build
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

1. **Start the Python nodes**:
    - Place commands in `Comp<UUID>/Instrc_r.txt` where `<UUID>` is the node identifier.
    - Commands should be formatted as `<A> <B> <Type>` where `Type` can be `A`, `S`, `M`, `D`, `IF=`, `IF!`, `IF>`, or `IF<`.

2. **Run the Python sample**:
    ```sh
    python3 Build/Sample.py
    ```

### Java Usage

- **Command Processing**:
  - Place commands in `Build/Comp<UUID>/Instrc_r.txt` where `<UUID>` is the node identifier.
  - Commands should be formatted as `<A> <B> <Type>` where `Type` can be `A`, `S`, `M`, `D`, `IF=`, `IF!`, `IF>`, or `IF<`.

- **Output Retrieval**:
  - Orchid writes the result to `Build/Comp<UUID>/Instrc_s.txt`.

## Cleaning the Build Directory

1. **Clean the build directory**:
    ```sh
    make Clean
    ```