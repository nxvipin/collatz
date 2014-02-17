Collatz
=======

Collatz solver using gevent. 

Requirements
============

Gevent library is used in calculations. Flask is used in the http server. Requests library is used by client.

```
pip install requests
pip install flask
pip install gevent
```

Try
===

Start collatz server :
```
python collatz_server.py
```

Start collatz client in another terminal window.
```
python collatz_client.py
```

Input
=====

Enter space seperated pair of numbers follwed by a new line character.
Indicate end of input by entering two new line caharacters. Example : 
```
-- Collatz Server Client -- 

Enter a pair of numbers followed by a new line character for each test case.
Indicate end of input by entering two new line characters.
 
10 20
30 40
100 110

```
Output
======

For each input pair, output will be a triple. Example : 
```
10 20 21
30 40 107
100 110 114

```

Details
=======

Collatz cycle length of a number is calculated using a recursive memoized algorithm. All calculated cycle lengths are stored in Hash table. Recursive function is stopped if the number reduces to any number present in the HT.

##### Collatz Server
Collatz server is a http server that takes a json input as a ```GET``` parameter named ```data```

Example server call : 
```
http://localhost:5000/?data=[[10,20],[20,30]]
```

##### Collatz Client

Collatz client takes the input from the user, converts it to the JSON form. A request is sent to the server and the result is formatted and displayed to the user.


Concurrency using Gevent
========================

Each test case is ```concurrently``` executed by the server. Within a test case, cycle length for each number in the input range in executed ```serially```.

Concurrent cycle length calculation for each number in a range was tried along with concurrent execution of each test case but it harmed the throughput.

Serial execution resulted in similar execution time. This can be explained by the fact that the task is pure computation and not IO bound.

Raw Timings
===========

#####Input Range : 1, 100000
```
raw times: 11 10.6 10.6 10.6 10.6
5 loops, best of 5: 2.11 sec per loop
```

Replicate the above test :
```
python -mtimeit -n 5 -r 5 -v -s'import collatz' 'collatz.p_range_collatz((1,100000))'
```

