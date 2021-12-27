# EasyCircuit

EasyCircuit is a simple DSL that allows users to draw complicated electric circuit diagram using syntax similar to `dot`

### Design Notes  
  
To avoid potential user confusion of reusing pre-defined variables, we have divided those variables into two categories, atomic and compound.  
  
Atomic variable refers to those (`INPUT`, `OUPUT`, or other gates) that remains the same across different scope. It can be reused more than once  by the means of refering to the same memory address of the first copy created(whenever the Atomic variables are declared at the first time).

Compound variable refers to `CIRCUIT` where each reused `CIRCUIT` will create a new copy which is exactly the same as the `CIRCUIT` defined before.

## Development

### Language
We will be using `python3` together with `antlr` to develop the DSL

## Setup

We have 2 ways to setup the language environment

### Prequisite
Python >== 3.9.7

### Pycharm setup

Download `Pycharm` at https://www.jetbrains.com/pycharm/download/

Set the interpreter in `Pycharm` to be Python 3.9

Open the project in `Pycharm`

Right click the `main.py` and click run

You should be able to see the `EC>` get printed in the your terminal

Another way to run the project through terminal:
### Setup a virtualenv

We will be using `venv` to manage python dependencies: https://docs.python.org/3/library/venv.html

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.
### Create venv
```bash
python -m venv path/to/venv
```

### Activate virtualenv

```bash
# Unix
$ source <venv>/bin/activate
# Windows
path/to/env Scripts/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Setup package structure

https://stackoverflow.com/questions/6323860/sibling-package-imports

```bash
pip install -e .
```

### Run

```bash
python ./src/main.py
```

### Use the DSL

You should have a DSL text written in one file (file_name.txt)

After running the command above, you enter a terminal interface, the way you can access the DSL text is run this:

```bash
EC> load path/to/file.txt

# Try the following entry to get started as a new user.
EC> load examples/practical_use_case.txt
```

`EC` is just some prefix we print in the terminal, `load` is the actual command to evaluate the DSL code

If a check failed or command is invalid, we report it in terminal and continue the loop, so you can simply type another
command.

### Git and Github

- For each development task, a issue is created and
  assigned: [issues](https://github.students.cs.ubc.ca/cpsc410-2021w-t1/Project1Group3/issues),
  in [project](https://github.students.cs.ubc.ca/cpsc410-2021w-t1/Project1Group3/projects), a card is created in each
  task as well, so that we can keep track of the progress of each task.

- For each development task, a branch should be created under following name: `(contributorname)-(featurename)`
  (e.g. `jerry-antlr_grammar`)

- Each merge should open a `Pull Request` from your branch to `master`

### Development Plan

- [x] Develop Grammar (top priority)
- [x] Explore Schemdraw to setup basic drawing
- [x] Implementation
- [x] Video making

### Note!!!

We would like to use this section to clarify an important point about our DSL:

- If we have an input component `INPUT i1` defined, you can refer it in a circuit, however it doesn't always mean the
  same in program semantics, this is something we would like to explain through examples

```dot
  CIRCUIT c1 {
    in1 -> and;
    in1 -> and;
  }
```

We can see that we use `in1` for twice, this doesn't create 2 separate inputs, but is referring to the same inputs. The
repeated statements above does nothing different if you simply write `in1->and` just once.

```dot
  CIRCUIT c1 {
    ...
    in1 -> and;
  }
  CIRCUIT c2 {
    in1 -> and;
  }
  
  CIRCUIT c3 {
    c1 -> or;
    c2 -> or;
  }
```

However, the same repeated statements in 2 different circuit definition, will create a copy of both the input
component `in1` and the and gate `and`. If we draw `c3`, the inputs and gates will be drawed separately for `c1`
and `c2`. Although we use the same variable name, we actually create 2 copy of the components

```dot
CIRCUIT c3 {
  c1 -> or;
  c1 -> or;
}
```

Reuse the sample above, what if we refer to the same circuit variable with the same name twice in a circuit? The rules
for circuit variable (`c1`) is actually different from what we have for `in1`, even in the same circuit scope, referring
to `c1` twice will create 2 copies of `c1` circuit, all the inputs and connects defined in `c1` will be copied.
Therefore, if we draw `c3`, we actually draw all the gates in
`c1` twice

```dot
CIRCUIT c2 {
  ...
  c1 -> or;
}
CIRCUIT c3 {
  ...
  c1 -> xor;
 }
```

Referring to the same circuit in different circuit definition also creates 2 copies of the circuit, here if we draw `c2`
and `c3`
separately or have a `c4` that contains `c2` and `c3`,
`c1` will be drawed separately as well in `c2` and `c3`

We are sorry about the confusion we made in this project, a lot of ambiguity can be improved if we have more time.



