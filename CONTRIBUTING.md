# Contributing

### Definition and Requirements of a Valid "Pangram Program"
<center><sub> <i>for the purposes of this repository.</i> </sub></center>


In short, an ideal pangram program should strive to exhaustively implement, instantiate, invoke, or however otherwise expose as valid source code (**commented or plain string content doesn't count!**) that gets parsed by an interpretter and/or compiler for a given programming language the following features of said language:
* Reserved and/or key words that cannot be used for variable or subroutine names (commonly words like `if`, `else`, `return`, etc.)
* Objects of all class-types (if the language is typed) implemented in the **standard libraries** of a given language (that is, the libraries that come out of box with a default installation)
  * This includes making calls to each public method and referencing all public variables of each distinctly-classed object.
* All "n-ary" symbolic operators (e.g. =, >, !, &&, etc.)
* All other syntactic snippet constructs that aren't captured in the above. Examples:
  * All forms of comprehensions in Python (`[ i for i in iterable ]`)
  * Javascript arrow-functions and promise-chaining
  * For functional languages, an example of each term in the lexicon of functional programming jargon


Notice I said "ideal" above, as this is a tall order to implement in some languages. The rule of thumb is, if you make a reasonable effort and represent the decent majority of a language's features then it will suffice&mdash;this is intended to be more fun than it is rigorous :)

>**Note**: it is perfectly valid if your pangram program itself is generated programmtically, just please include the generator code and an invokation of it in the validation executabutable explained below.


## Pangram Module Directory Structure


In order for a pangram module to be deemed valid in this repository, it should mirror this directory structure:
```
.
├── CONTRIBUTING.md (you are here!)
├── LICENSE
├── README.md
...
├── <language root directory>
│   ├── <pangram-directory>
│   │   ├── README.md
│   │   ...
│   │   ├── <other implementation-specific supporting files as needed> 
│   │   ...
│   │   ├── pangram.<language-extension>
│   │   └── validate 
│   ...
...
```

* `<language-root-directory>`

  This might already exist, but if not please create a directory named after your respective implementation language in all lower-case letters (e.g. `python`, `lua`, `rust`, etc.).

  _If versioning matters (such as `python2` vs `python3`, `lua-5.1` vs `lua-5.3`, etc.) please do not add the version to the directory name&mdash;instead just use the intended version-specific executable in the `validate` script/executable, either for the #!hashbang or invoked within._

* `<language-root-directory>/<pangram-directory>`

    This is where the magic happens. Please name this as descriptively but succinctly as reasonably possible. For example, my Python sample is [`/python/all-keywords-builtins-operators`](/python/all-keywords-builtins-operators/README.md)
  
* `<language-root-directory>/<pangram-directory>/README.md`

    Should explain why the code should count as a pangram, and more importantly how to run the program and/or run the validation (explained below).
    
* `<language-root-directory>/<pangram-directory>/pangram.<language-extension>`
    
    Your actual pangram source code.
    
* `<language-root-directory>/<pangram-directory>/<other implementation-specific supporting files as needed>`

    If your pangram and/or its execution needs supporting files. For example, a C implementation may provide a Makefile for convenience.
    
* `<language-root-directory>/<pangram-directory>/validate`

    This should be an executable, such as a shell script, that scans the cleartext of your pangram and somehow verifies it is lexically exhaustive of some aspect of the language. In the case of Python this is relatively easy since Python exposes methods to get lists of keywords and "builtins" as strings. Other languages may require consulting reference manuals or other documentation to get such a list. If that is necessary, please include links to those documents (or better yet, scrape them programmatically!). This sript should make sure all the language lexemes are present in the source code (and not just as comments!).