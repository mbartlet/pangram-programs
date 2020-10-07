## Definition and Requirements of a Valid "Pangram Program"

<sub>_for the purposes of this repository._</sub>

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
│   │   ├── <other language-specific supporting files as needed> 
│   │   ...
│   │   ├── pangram.<language-extension>
│   │   └── validate 
│   ...
...
```

#### `<language-root-directory>`
This might already exist, but if not please create a directory named after your respective implementation language in all lower-case letters (e.g. `python`, `lua`, `rust`, etc.).

_If versioning matters (such as `python2` vs `python3`, `lua-5.1` vs `lua-5.3`, etc.) please do not add the version to the directory name&mdash;instead just use the intended version-specific executable in the `validate` script/executable, either for the #!hashbang or invoked within._

#### `<language-root-directory>/<pangram-directory>`
<descriptive-hyphen-delimited-name> (e.g. all-keywords-builtins-operators)
#### `<language-root-directory>/<pangram-directory>/README.md`
(explain how to execute, how it's a pangram, etc.)
#### `<language-root-directory>/<pangram-directory>/pangram.<language-extension>`
a
#### `<language-root-directory>/<pangram-directory>/<other language-specific supporting files as needed>`
such as a `Makefile` for C
#### `<language-root-directory>/<pangram-directory>/validate`
(this is an executable, such as a shell script, that scans the cleartext of your pangram and somehow verifies it is lexically exhaustive of some aspect of the language)