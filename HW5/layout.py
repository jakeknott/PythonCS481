"""
This is the layout of a generic keyboard.  It is a tuple of rows.
Each row is a variable-length tuple of key definitions.  Each key
definition is a tuple consisting of a key label followed by a column
span.  Key labels are strings, matching as closely as possible a real
keyboard: Shifted keys have labels with a newline between the shifted
and unshifted symbols.  Letters have single upper-case letter labels.
Other keys have capitalized names.
"""

layout = (
    ( ('~\n`', 1), ('!\n1', 1), ('@\n2', 1), ('#\n3', 1), ('$\n4', 1),
      ('%\n5', 1), ('^\n6', 1), ('&\n7', 1), ('*\n8', 1), ('(\n9', 1),
      (')\n0', 1), ('_\n-', 1), ('+\n=', 1), ('Backspace', 2),
      ),
    ( ('Tab', 2), ('Q', 1), ('W', 1), ('E', 1), ('R', 1), ('T', 1),
      ('Y', 1), ('U', 1), ('I', 1), ('O', 1), ('P', 1), ('{\n[', 1),
      ('}\n]', 1), ('|\n\\', 1)
      ),
    ( ('CapsLock', 2), ('A', 1), ('S', 1), ('D', 1), ('F', 1), ('G', 1),
      ('H', 1), ('J', 1), ('K', 1), ('L', 1), (':\n;', 1), ('"\n\'', 1),
      ('Enter', 2)
      ),
    ( ('Shift', 2), ('Z', 1), ('X', 1), ('C', 1), ('V', 1), ('B', 1),
      ('N', 1), ('M', 1), ('<\n,', 1), ('>\n.', 1), ('?\n/', 1), ('Shift', 3),
      ),
    ( ('Ctrl', 2), ('Alt', 2), ('Space', 7), ('Alt', 2), ('Ctrl', 2),
      ),
    )