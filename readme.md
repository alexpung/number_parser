# number_parser
Convert a Chinese or Japanese number of various notations to a number.

Usage:
------
The function read a string starting with a number, and return a value based on the representation of Kanji.
It will stop reading if it see any non numerical letter.

It does not support English notation such as 'k' (thousand), 'M'/'MM' (Million) etc

Example:
------
parse_number('百八十一')  
181.0

parse_number('六千三百二十一億千五百十一万二千百八十一')  
632115112181.0

parse_number('0.6千株')  
600.0

parse_number('7.28千株')  
7280.0

parse_number('1億1511万2181')  
115112181.0

parse_number('三十萬零二百五十')  
300250.0

parse_number('66,728千株')  
66728000.0

parse_number('12 566 728千株')  
12566728000.0