# Orchid

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