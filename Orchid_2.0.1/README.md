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