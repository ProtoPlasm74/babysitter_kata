This is a python script to solve the kata below.

Python 3.8.9

Unit tests are located in the tests.py.
The solution is in main.py.

This is written with the asumption that bedtime is 9pm and there is no daylight savings time to not overcomplicate (that would require datetime objects). I converted the the hours to be 0-11 for easier calculations without datetime.

Hours in a range:
5 0
6 1
7 2
8 3
9 4
10 5
11 6
12 7
1 8
2 9
3 10
4 11

Babysitter Kata

## Background

This kata simulates a babysitter working and getting paid for one night. The rules are pretty straight forward:

The babysitter

- starts no earlier than 5:00PM
- leaves no later than 4:00AM
- gets paid $12/hour from start-time to bedtime
- gets paid $8/hour from bedtime to midnight
- gets paid $16/hour from midnight to end of job
- gets paid for full hours (no fractional hours)

Feature:
As a babysitter
In order to get paid for 1 night of work
I want to calculate my nightly charge


