#!/usr/bin/python
code_stra = """
print "Hello, World"
"""
code_strb = """
a = [str(i) for i in range(), 10)]
"""
code_strc = """
[str(i) for i in range(0, 10)]
"""

# As discussed in the exec vs eval. eval only evaluates expressions, no statements.
# something that can amount to a evaluation.
code_cobja = compile(code_stra, '<string>', 'exec')
# The single compile mode only compliles one statement
code_cobjb = compile(code_strb, '<string>', 'single')

code_cobjc = compile(code_strc, '<string>', 'eval')
