import sys
from io import StringIO

class stdout2string:
    """
    Context manager for redirecting stdout to string.

    >>> with stdout2string() as p:
    ...     print("Nothing is printed. ")
    ...     print("These strings are saved to p. ")
    >>> p
    ['Nothing is printed. \\nThese strings are saved to p. \\n']
    >>> print("Outside the context manager, string is printed normally to stdout")
    Outside the context manager, string is printed normally to stdout
    """
    def __init__(self):
        self.container = []

    def __enter__(self):
        self.backup_stdout = sys.stdout
        self.string_stdout = StringIO()
        sys.stdout = self.string_stdout
        return self.container

    def __exit__(self,  exc_type, exc_val, traceback):
        if exc_val is not None:
            print(exc_type, exc_val, traceback)
        sys.stdout = self.backup_stdout
        self.container.append(self.string_stdout.getvalue())
        self.string_stdout.close()

if __name__=="__main__":
    import doctest
    doctest.testmod(verbose=True)