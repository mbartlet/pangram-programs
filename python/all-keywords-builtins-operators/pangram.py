#!/usr/bin/env python3

try:
	# a = (a := round(0x10,0b100)) & a - a + a << a >> a * a ** a // a % a == a < a > a <= a >= a
	a = (a := 100) & a - a + a << a >> a * a ** a // a % a < a > a <= a >= a | a
	assert a==a 
	a != a,
	a %= 0b1
	a &= a
	a **= a
	a *= a
	a += a
	a -= a
	a //= 0x1
	a >>= a
	a <<= a
	a |= a
	a /= 10e10
	a = "str"
except (
  SyntaxError,
  ArithmeticError,
  AssertionError,
  AttributeError,
  BlockingIOError,
  BrokenPipeError,
  BufferError,
  ChildProcessError,
  ConnectionAbortedError,
  ConnectionAbortedError,
  ConnectionError,
  ConnectionRefusedError,
  ConnectionResetError,
  EnvironmentError,
  EOFError,
  Exception,
  FileExistsError,
  FileNotFoundError,
  FloatingPointError,
  ImportError,
  IndentationError,
  IndexError,
  InterruptedError,
  IOError,
  IsADirectoryError,
  KeyError,
  LookupError,
  MemoryError,
  ModuleNotFoundError,
  NameError,
  NotADirectoryError,
  NotImplementedError,
  OSError,
  OverflowError,
  PermissionError,
  ProcessLookupError,
  RecursionError,
  ReferenceError,
  RuntimeError,
  SystemError,
  TabError,
  TimeoutError,
  TypeError,
  UnboundLocalError,
  UnicodeDecodeError,
  UnicodeEncodeError,
  UnicodeError,
  UnicodeTranslateError,
  ValueError,
  ZeroDivisionError) as e:
	print(e)
  
  # RuntimeWarning, # BytesWarning, # DeprecationWarning, # FutureWarning, # ImportWarning, # PendingDeprecationWarning, # ResourceWarning, # RuntimeWarning, # SyntaxWarning, # UnicodeWarning, # UserWarning, # Warning, # SystemExit , NotImplemented,) as e:

"""













@
@=
ArithmeticError
AssertionError
AttributeError
BaseException
BlockingIOError
BrokenPipeError
BufferError
ChildProcessError
ConnectionAbortedError
ConnectionError
ConnectionRefusedError
ConnectionResetError
EOFError
Ellipsis
EnvironmentError
Exception
False
FileExistsError
FileNotFoundError
FloatingPointError
GeneratorExit
IOError
ImportError
IndentationError
IndexError
InterruptedError
IsADirectoryError
KeyError
KeyboardInterrupt
LookupError
MemoryError
ModuleNotFoundError
NameError
None
NotADirectoryError
NotImplemented
NotImplementedError
OSError
OverflowError
PANGRAM_FILE
PermissionError
ProcessLookupError
RecursionError
ReferenceError
RuntimeError
StopAsyncIteration
StopIteration
SyntaxError
SystemError
SystemExit
TabError
TimeoutError
True
TypeError
UnboundLocalError
UnicodeDecodeError
UnicodeEncodeError
UnicodeError
UnicodeTranslateError
ValueError
ZeroDivisionError
[]
^
^=
__annotations__
__build_class__
__builtins__
__cached__
__debug__
__doc__
__file__
__import__
__loader__
__name__
__package__
__spec__
abs
all
and
any
as
ascii
assert
async
await
bin
bool
break
breakpoint
bytearray
bytes
callable
chr
class
classmethod
compile
complex
continue
copyright
credits
def
del
delattr
dict
dir
divmod
elif
else
enumerate
eval
except
exec
exit
filter
finally
float
for
format
from
frozenset
g
getattr
global
globals
hasattr
hash
help
hex
id
if
import
in
input
int
is
isinstance
issubclass
iter
keyword
lambda
len
license
list
locals
map
max
memoryview
min
next
nonlocal
not
object
oct
open
operator
or
ord
pass
pow
print
property
python_lexemes
quit
raise
range
re
repr
return
reversed
round
set
setattr
slice
sorted
staticmethod
str
sum
super
try
tuple
type
unittest
vars
while
with
yield
zip
|
|=
~
"""