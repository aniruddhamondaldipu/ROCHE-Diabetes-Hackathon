# ROCHE-Diabetes-Hackathon
This Repository is made to submit the Hackathon Challenge.

# FizzBuzz Statistics Generator

A simple Python script that allows users to input FizzBuzz parameters and provides statistics on the most frequently used inputs.

## Features

- Generate FizzBuzz output for given parameters.
- View statistics on the most used FizzBuzz inputs.

## Usage

1. Run the script.
2. Input the number of times you want to provide FizzBuzz parameters.
3. Enter FizzBuzz parameters for each iteration.
4. View FizzBuzz output and statistics.

## Example

```bash
$ python ROCHE_Diabetes_Hackathon_Aniruddha.py
Please enter number of times wanted to provide input: 3

Please Enter the Input Value
Fizz Value: 3
Buzz Value: 5
Length Of List: 15
Word 1: Fizz
Word 2: Buzz
['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']

Please Enter the Input Value
Fizz Value: 2
Buzz Value: 7
Length Of List: 10
Word 1: Fizz
Word 2: Buzz
['1', 'Fizz', '3', 'Fizz', '5', 'FizzBuzz', '7', 'Fizz', '9', 'Fizz']

Please Enter the Input Value
Fizz Value: 5
Buzz Value: 8
Length Of List: 20
Word 1: Hello
Word 2: World
['1', '2', '3', '4', 'HelloWorld', '6', '7', 'Hello', '9', 'World', '11', 'Hello', '13', '14', 'HelloWorld', '16', '17', 'Hello', '19', 'World']

Statistics:
{
  "Most Used Input": [
    {
      "Fizz Value:": 3,
      "Buzz Value:": 5,
      "Length Of List:": 15,
      "Word 1:": "Fizz",
      "Word 2:": "Buzz",
      "Hits": 1
    },
    {
      "Fizz Value:": 2,
      "Buzz Value:": 7,
      "Length Of List:": 10,
      "Word 1:": "Fizz",
      "Word 2:": "Buzz",
      "Hits": 1
    },
    {
      "Fizz Value:": 5,
      "Buzz Value:": 8,
      "Length Of List:": 20,
      "Word 1:": "Hello",
      "Word 2:": "World",
      "Hits": 1
    }
  ]
}
