
# LAB - Class 09 

# Project: Ten-thousand V4

## Authors || Group Names

- Al-masri, Al-mothana
- Areeda, Ibraheem
- Alzabn, Lina

## Setup and Requirements

To set up and run the provided code and tests for the Ten-thousand game, follow these steps:

 1. Clone the repository
 2. Navigate to the project directory
 3. Run the tests using the following command
 `
 pytest
 `

The tests will be executed, and the results will be displayed in the terminal.

### Dependencies

The following dependencies are required to run the code and execute the tests:

- Python x
- pytest==7.3.1

In addition to the Python standard library, the code uses the `random` module, which is a built-in module for generating random dice rolls in the `roll_dice` method.

### Installation

To install the required dependencies, follow these steps:

1. Make sure you have Python x installed on your system.
2. Open a terminal (Ubuntu) and run the following command to install pytest:

   ```
   pip install pytest
   ```

## initializing and running the Ten Thousand
To initialize and run the Ten Thousand game:
1. create environment (contaner):
```
python -m venv .venv
```
if nothing appear that means ecry thing is ok , to make sure type `la` to see the invisable venv file

2. activate the environment:
```
source .venv/bin/activate
```
now it will appear like this `(.venv)` will appear in the starting of the line which will indicate that your environment is activated, when you want to deactivate it just type the command `deactivate`

3. install packages:   
now inside the environment we will install all the packages we need using `pip` 
```
pip install
```
## To run the Ten Thousand game 

to run the code type:
```
python ten_thousand/game.py
```


## Tests

To run the tests for the Ten Thousand game:

- Make sure you have installed pytest as mentioned in the "Setup and Requirements" section.

- Open a terminal (Ubuntu).
- Navigate to the directory where the code is located.
- Activate the virtual environment if you created one during the setup by use this command : <br>
`source .venv/bin/activate`

Run the following command to execute the tests:

 ```

 pytest

```
 This will run all the tests in the code and display the test results.


The Testing include :

- `test_single_five()`: Tests scoring for a single 5.
- `test_single_one()`: Tests scoring for a single 1.
- `test_three_fives()`: Tests scoring for three 5s.
- `test_three_ones()`: Tests scoring for three 1s.
- `test_straight()`: Tests scoring for a straight sequence 
     (1, 2, 3, 4, 5, 6).
- `test_six_ones()`: Tests scoring for six 1s.
