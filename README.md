# FindSquare

This program is about finding the biggest square in a 2 dimension map like this :
```
.oo.....
o.....o.
........
...o....

```
where "." are free spaces and "o" are obstacles.
The goal is to find the biggest square possible among free spaces, and replace characters by "x" for the square, like this :
```
.ooxxx..
o..xxxo.
...xxx..
...o....

```

The main program "find_square" can be used with as many maps in arguments as possible :
```
python find_square.py map_example_1.txt map_example_2.txt map_example_3.txt
```

The unit test file can be launched as well with :
```
python unittest_find_square
```
