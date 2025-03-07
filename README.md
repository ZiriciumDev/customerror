## customerror
A simple tool to make custom errors!

The three functions are:

error(MainMessage, ReturnMessage)
this returns a custom error. Pretty self-explanatory. Both arguments are strings.

trye(errorname, code)
errorname is a string for the error to catch, and code is a string of code to try.

checkerr(errorname)
This returns true if the last error was a error with the error name (string).

Example usage:
```
import customerror

customerror.trye("bigCrashError", "import customerror\ncustomerror.error('bigCrashError', 'CRITICAL!')")

try:
	customerror.error('bigCrashError', 'CRITICAL!')
except customerror.customerror():
	if customerror.checkerr('bigCrashError'):
		print('bigcrasherr')

customerror.error('bigCrashError', 'CRITICAL!')
```

> if you find any bugs, feel free to report them at [ziriciumdev@gmail.com](ziriciumdev@gmail.com)