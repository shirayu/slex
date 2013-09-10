# A Python module for the Java Stanford Parser
---------------------------

This is a Python interface to [Stanford Parser](http://nlp.stanford.edu/software/lex-parser.shtml).

## Download and Usage

You can install this module in the general way.

    sudo python setup.py install

This requires the following Python packages.
- [JPype](http://jpype.sourceforge.net/)

After install this module and unzip of downloaded [Stanford Parser](http://nlp.stanford.edu/software/lex-parser.shtml),
you can use ``slex`` command like this using the unzipped files.
To get ``englishPCFG.ser.gz``, you should unzip ``stanford-parser-X.Y.Z-models.jar``.

    slex stanford-parser.jar englishPCFG.ser.gz

To know the typical usage of the module ``slex``, see ``scripts/slex``.


## Developer
- Yuta Hayashibe

## License
- GNU GENERAL PUBLIC LICENSE Version 3
- Except for the following third party's sources
    - [ClassPathModifier.java](http://blog.daisukeyamashita.com/post/207.html)
    - [singleton.py](http://python.g.hatena.ne.jp/nelnal_programing/20080225/1203927879)


