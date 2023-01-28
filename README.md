# Kumaragunachandrarajamahanti_HW1
execution- Packages Used: "import re"

Used to perform regular expression.
----------------
As mention in the assignment, 4 Modules have been created to perform respective tasks
currency.py -> To Validate currency
date.py -> To Validate date
phone_numbers.py -> To Validate phone numbers
tags.py -> To Remove Tags in string

input.txt file Will have all input strings separated by new Lines
output of each string will be shown on terminal screen
Execution Command: `python driver.py`
driver.py iterate over input.txt file lines and perform 4 Modules on each string.

input - there is a sample input in input.txt file if we wanted to change the input we need to make changes in that file.

sample input-
$954.49
$10,724.00
$1,000,000,023.45
-$250,000,456
+$234,922.99
USD45M
$25K
$4B 
January 05, 1960
6/1/00
04-Jul, 2004
2021-20-01 
6012664949
+1 601 266-4949
(601)-266-4949
001-601-266-4949 
January 05, 1960 was a cold day, I suppose
I do remember 04-Jul, 2004!!
<html>
<body>
<div>
<img>
  
  desiredoutput-
  Valid Currency: $954.49
Valid Currency: $10,724.00
Valid Currency: $1,000,000,023.45
Valid Currency: -$250,000,456
Valid Currency: +$234,922.99
Valid Currency: USD45M
Valid Currency: $25K
Valid Currency: $4B
Valid Date: January 05, 1960
Valid Date: 6/1/00
Valid Date: 04-Jul, 2004
Valid Date: 2021-20-01
Valid Currency: 6012664949
Valid PhoneNumber: +1 601 266-4949
Valid PhoneNumber: (601)-266-4949
Valid PhoneNumber: 001-601-266-4949
Valid Date: January 05, 1960 was a cold day, I suppose
Valid Date: I do remember 04-Jul, 2004!!
