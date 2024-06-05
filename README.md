# Orchid
Orchid was my first attempt at a distributed computing software. though it turned out as more of a library.

# Installation
1. Build with "make Build"
2. Install with "make Install"
    #it will ask for sudo, this is to install brew, which is a requirement

# First Steps
start in the folder "Comp1"
next, youll need to run start.sh with "sh start.sh" in order to run any commands. this turns on the node "Comp1"
for debug purposes you can run "sh -v Build/int.sh" this will turn on all nodes locally

# Docs
    # Comp Number must be either 1, 2, or 3.
    # Input1 and Input2 can be variables, constants, or strings
First this is a library. you can import it using "from Public.Orchid import Instance"
to instantiate a node in your program you can use "C<Comp number> = Instance('<Comp number>')"
to send a command to a node you can use "C<Comp number>.Process(<Input1>, <Input2>, '<Operation type>')"
to read the output use "C<Comp number>.Read()" it will return either a boolean or a string containing your value

# Operation Types
1. A is Add
2. S is subtract
3. M is multiply
4. D is divide
5. IF= is an if statement it will output a boolean
=======

Orchid is a distributed computing library designed to facilitate node-based computations. This project was my first foray into distributed computing, evolving into a versatile library.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/my-chatbot-repo.git
    cd my-chatbot-repo
    ```

2. **Install dependencies**:
    ```sh
    make Install
    ```
    - This will check for the presence of Homebrew and Python3, installing them if necessary.

3. **Build the project**:
    ```sh
    make Build
    ```
    - By default, this will set up 3 nodes.

4. **Specify a different number of nodes** (optional):
    ```sh
    make Build NUM_NODES=5
    ```
    - Replace `5` with the desired number of nodes.

## Getting Started

1. Navigate to the `Comp1` directory:
    ```sh
    cd Comp1
    ```

2. Run `start.sh` to activate the node `Comp1`:
    ```sh
    sh start.sh
    ```

3. For debugging purposes, you can run `int.sh` to activate all nodes locally:
    ```sh
    sh -v Build/int.sh
    ```

## Documentation

### Usage

Orchid is a library that can be imported into your Python program.

1. **Import the library**:
    ```python
    from Public.Orchid import Instance
    ```

2. **Instantiate a node**:
    ```python
    C<CompNumber> = Instance('<CompNumber>')
    ```
    - `<CompNumber>` must be either `1`, `2`, or `3`.

3. **Send a command to a node**:
    ```python
    C<CompNumber>.Process(<Input1>, <Input2>, '<OperationType>')
    ```
    - `<Input1>` and `<Input2>` can be variables, constants, or strings.
    - `<OperationType>` specifies the operation to be performed (see Operation Types below).

4. **Read the output from a node**:
    ```python
    result = C<CompNumber>.Read()
    ```
    - This will return either a boolean or a string containing the computed value.

### Operation Types

- **A**: Add
- **S**: Subtract
- **M**: Multiply
- **D**: Divide
- **IF=**: If statement (outputs a boolean)