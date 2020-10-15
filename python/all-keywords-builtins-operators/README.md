# Python Pangram
The pangram featured here exhaustively makes use of (i.e. interprets and executes, not just parses as a string) all valid python lexemes. This includes keywords/reserved words, builtins, and all unique tokens which are identified through regex while parsing. If there is a function, feature, or grammar you can think of having used in a valid Python program, that pattern should be present here (and if not, feel free to open a pull request correcting that).

## Execution
You can execute the pangram by running `python3 pangram.py`. It itself does not serve any practical use or do anything interesting. The `validate` program included here will execute the program for you, and print its execution trace. You may as well run that instead, it is at least more colorful.

## Validation
Simply run `python3 validate`; `validate` is programmed to (through a constant `PANGRAM_FILE` at the top) target `pangram.py` and parse the python code present within. It will scan this code to ensure all valid lexemes are represented at least once, and also execute the code to make sure it exits without raising any exceptions (a criterion I think is sufficient to indicate it is a "valid" python program).

This script uses the standard test-suite library. As such, if any of the tests needed to qualify a script as a python pangram fail, you will see output similar to:

```
$ python3 validate  
F..


==================
FAIL: test_pangram_has_all_python_lexemes (__main__.TestPangramAuthenticity)
------------------
'isinstance' not present in pangram.py.



==================
Ran 3 tests in 0.026s

FAILED (failures=1)
```

Otherwise, if the program is deemed to have satisfied all criteria to be a pangram, you will see:

```
$ python3 validate  

< more pangram execution trace >

pangram.py(90): 	  x = ','.join(str(s) for s in l)
pangram.py(91): 	  return x

...

Ran 3 tests in 0.025s

OK

```

## Ideas for Expansion
* A pangram which also makes use of all extra lexemes added by the python standard modules
* Turn the pangram into a practical script
* Quine pangram