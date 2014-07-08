# Manservant

Manservant lets you view manpages right in your browser with clickable
references to sections and links.

## Usage

1. Start the local server:

        python manservant.py

2. Point your browser to this URL:

        http://localhost:4321/

   If the port does not suit you, feel free to adjust it in
   `manservant.py`.

## Dependencies

Manservant depends on

- an implementation of `man` that supports the `-w` switch to print the
  location(s) of the cat file(s) that would be displayed without actually
  displaying it/them (If your implementation supports a different switch
  with the same functionality, adjust it in `manservant.py`.) and
- [man2html](http://dcssrv1.oit.uci.edu/indiv/ehood/man2html.html).

The web app itself is a basic Bottle application that spawns processes for
the tools described above every time the users posts a search query.

**Side note**:
Manservant also comes with a SQLite3 database `test.db` and some code
interfacing with it (`createdb.py` and `populatedb.py`). The database is
not required for manpage viewing, but may be used to built in some level of
persistence in the future (tagging manpages or keeping a list of
recently viewed manpages etc.). See all the `tasks`-related routes in
`manservant.py` for an example use case.
