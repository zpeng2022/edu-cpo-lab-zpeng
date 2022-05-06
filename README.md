# slay_the_dragon - lab #1 - variant 7

This is an example project which demonstrates dic structure and necessary

## Project structure

- `DicHashMap.py` -- implementation of `DicHashMap` class with
- required features
- `SelfHashMap.py` -- implementation of `SelfHashMap` class with
- basic hash map features
- `test_DicHashMap.py` -- tests for dicHashMap
- `localcheck.bash` -- check codestyle and typical python error
- on a local machine

## Features

- PBT: `test_add`
- PBT: `test_set`
- PBT: `test_get`
- PBT: `test_change`
- PBT: `test_remove`
- PBT: `test_size`
- PBT: `test_is_member_for_key`
- PBT: `test_filter_the_value`
- PBT: `test_to_list`
- PBT: `test_from_list`
- PBT: `test_map`
- PBT: `test_reduce`
- PBT: `test_iterator`
- PBT: `test_concat`

## Contribution

- Zhan,Peng (zpeng@hdu.edu.cn) -- write the main class part.
- Zhong,ZhuZhou(212320020@hdu.edu.cn) -- write the test part.

## Changelog

- 06.05.2022 - 11
  - add docstrings for all functions 
- 05.05.2022 - 10
  - update the mutable concat and empty method.
- 26.04.2022 - 9
  - add PBT test for monoid properties
  - fix the bug of iterator
  - updated the check.yml template
  - improved the readability of tests
- 19.04.2022 - 8
  - add tests for different type(None, str, float, text)
  - add more PBT tests
  - explain the difference between `SelfHashMap` and `DicHashMap` in Design note
- 14.04.2022 - 7
  - delete TestDicHashMap.py and add test_DicHashMap.py
  - update README.md and description
- 13.04.2022 - 6
  - add TestDicHashMap.py and update the README
- 13.04.2022 - 5
  - add DicHashMap.py and SelfHashMap.py files
- 11.04.2022 -4
  - update team member's information and group's information.
- 30.03.2022 -3
  - upload my code to github and test the github workflow.
- 29.03.2022 - 2
  - Add test coverage.
- 29.03.2022 - 1
  - Update README. Add formal sections.
- 29.03.2022 - 0
  - Initial

## Design notes

- DicHashMap and SelfHashMap
  - SelfHashMap is a hash map data structure supports dicHashMap
  - dicHashMap is a dic
  - We want to make DicHashMap clear and simple, so we split the
  - implementation into two parts
- Advantages of unit testing:
  - it help us write better code
  - it help us catch bugs earlier
  - it makes us more efficient at writing code
  - it make us detect regression bugs
- Disadvantage of unit testing:
  - it takes time to write cases
  - tests require a lot of time for maintenance
  - it can be challenging to test GUI code
  - unit testing can't catch all errors
- Advantages of PBT testing:
  - the PBT provides a reasonable estimate of the
  - evidential test result within the relevant forensic range
- Disadvantages of PBT testing:
  - it also be challenging to test GUI code
