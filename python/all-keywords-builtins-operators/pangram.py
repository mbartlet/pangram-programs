#!/usr/bin/env python3
from random import randint
import asyncio

try:
	errors=[[ BaseException, SystemExit, KeyboardInterrupt, GeneratorExit, Exception, StopIteration, StopAsyncIteration, ArithmeticError, FloatingPointError, OverflowError, ZeroDivisionError, AssertionError, AttributeError, BufferError, EOFError, ImportError, ModuleNotFoundError, LookupError, IndexError, KeyError, MemoryError, NameError, UnboundLocalError, OSError, BlockingIOError, ChildProcessError, ConnectionError, BrokenPipeError, ConnectionAbortedError, ConnectionRefusedError, ConnectionResetError, FileExistsError, FileNotFoundError, InterruptedError, IsADirectoryError, NotADirectoryError, PermissionError, ProcessLookupError, TimeoutError, ReferenceError, RuntimeError, NotImplementedError, RecursionError, SyntaxError, IndentationError, TabError, SystemError, TypeError, ValueError, UnicodeError, UnicodeDecodeError, UnicodeEncodeError, UnicodeTranslateError, Warning, DeprecationWarning, PendingDeprecationWarning, RuntimeWarning, SyntaxWarning, UserWarning, FutureWarning, ImportWarning, UnicodeWarning, BytesWarning, ResourceWarning ]]
	raise errors[randint(0,len(errors))]
except Exception as e:
	pass
finally:
	pass

string_prefixes = [Rb'', br"""""", Fr'''''', f"{hex(3)}", U"", b"", rB"", BR"", bR"", fr"", r"", RB"", RF"", R"", FR"", Rf"", u"", rb"", F"", Br"", rf"{oct(4)}", fR"", B"", rF"", ] 

dunders = [__name__, __debug__, __loader__, __doc__, __import__, __build_class__, __package__, __spec__]

a = (a := 100) & a - a ^ a + a << a >> a * a ** a // a % a < a > a <= a >= a | a
a != a
a %= 0b1
a &= int(bin(a),2)
a **= 0o1
a *= min(a,max(a, 10))
a |= a
a //= 0x1
a >>= a
a <<= a
a ^= a
a /= float(10e1)
a += 0.0
a -= a+0j
a, = [any((divmod(abs(a),2345678) + tuple(list()+[])))]

assert a == a 

if a or a:
	a
elif bool(a) and ... ==  Ellipsis or False or True:
	a
else:
	a

while True:
	with open('/dev/null','w') as f:
		f.write(str(bytes(bytearray(ascii(ord(chr(a))), 'utf-8')).decode("utf-8").encode("utf-8")))
	break
	continue

a = filter(all, map(callable,[breakpoint, license, credits, exit, help, input]))
a=dict()

for i,v in enumerate([ x for x in range(3)]):
	a[i]=v

a=frozenset(set(a))
memoryview(bytes(a))
a=repr(type(sum(a)))
a = (sorted(zip(locals().items(), globals().items())))[slice(1,4)]
eval("a")
exec("a")



def gen():
	global dunders
	for i in range(10):
		yield a

a=next(iter(list(gen())))
	     

class A(object):
	_a=0
	def __init__(self):
		_a=asyncio.run(self.f2())
		super()

	@classmethod
	def fromlist(cls, l):
	  x = cls()
	  x = ','.join(str(s) for s in l)
	  return x

	async def f1(self):
		return 3
		print("async")

	async def f2(self):
		await self.f1()

	@property
	def a(self):
		return self._a

	@staticmethod
	def f():
		return "static"

	def __matmul__(a,b):
		a._a *= -b._a
		return a

a=A()
a @= a @ a
setattr(a, "b", a.f())
getattr(a, "b", 0)
hasattr(a, "b")
delattr(a, "b")
a=a.fromlist(['a'])

if __name__ == "__main__":
	print("Execed!")



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