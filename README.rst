TVShow Mover
--------

To use (with caution), simply do::

    >>> from cdrom.mover import Mover
    >>> mover = Mover('/source', '/destination')
    >>> mover.move()

It also provides a command-line interface::

    tvmv move /source /destination

You can also list all files in the source::

    tvmv ls /source