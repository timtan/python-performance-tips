#python-performance-tips

##Total Requirements

###Platform Dependency
* mac
  * XCode
  * libevent
    


##Profile

#### Analyze profile_sample1
* python -m cProfile -s cumulative profile_sample1.py 
  * -m means directly invoke the module
  * -s is the sort order.  
  
  you will see output like the following:
  
	         5400283 function calls (5400273 primitive calls) in 5.527 seconds
	
	   Ordered by: cumulative time
	
	   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
	        1    1.062    1.062    5.527    5.527 profile_sample1.py:1(<module>)
	   900000    1.352    0.000    4.441    0.000 profile_sample1.py:3(find_domain)
	   900000    0.521    0.000    1.900    0.000 re.py:188(compile)
	   900000    1.104    0.000    1.380    0.000 re.py:229(_compile)
	   900000    0.958    0.000    0.958    0.000 {built-in method match}
	   900000    0.262    0.000    0.262    0.000 {method 'get' of 'dict' objects}
	   900000    0.231    0.000    0.231    0.000 {built-in method group}
	        1    0.024    0.024    0.024    0.024 {range}
	        1    0.000    0.000    0.013    0.013 sre_compile.py:495(compile)
	        1    0.000    0.000    0.013    0.013 sre_compile.py:480(_code)

	
	        
	        
   functions are ordered by cumulative execution time. and you have a rough idea what function cost much time. it this example. the candidates are find_domain, re.compile. 
   
   with the about clue, first we can try compile the pattern just once. 
   
	    2700286 function calls (2700276 primitive calls) in 2.780 seconds
	
	   Ordered by: cumulative time
	
	   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
	        1    0.950    0.950    2.780    2.780 profile_sample2.py:1(<module>)
	   900000    0.810    0.000    1.806    0.000 profile_sample2.py:3(find_domain)
	   900000    0.812    0.000    0.812    0.000 {built-in method match}
	   900000    0.184    0.000    0.184    0.000 {built-in method group}
	        1    0.024    0.024    0.024    0.024 {range}
	        1    0.000    0.000    0.000    0.000 re.py:188(compile)
	        1    0.000    0.000    0.000    0.000 re.py:229(_compile)
   
### How Profile Works
 to read the doc, [what-is-deterministic-profiling][1], we can know cProfile monitor function call, function return and exception events. the profiling is fine gran. because python automatically provides hooks for each event. 
   
   
 [1]:http://docs.python.org/library/profile.html#what-is-deterministic-profiling
 
### what if I have no knowledge that compile can be reduced to once

there are some reason that you cannot adopt the above process

 * you don't have knowledge about how to accerlate.
 * you are lack of time
 
## Some lazy approach
  
  
the original python
  
    time python2.7 profile_sample1.py 
	
	finish
	
	real	0m3.910s
	user	0m3.748s
	sys	    0m0.134s
	
	
the amazing pypy	

	time pypy profile_sample1.py 
	finish
	
	real	0m0.947s
	user	0m0.543s
	sys	    0m0.058s


### drawback of pypy

will you open ppt from keynote?

the pypy cannot using c module. (don't be scare, standard library written in c is rewrite)

### cython 
[reference](http://docs.cython.org/src/userguide/tutorial.html)

uncomment all the comment in setup.py

before using cython
	
	time profile_sample1
	finish
	
	real	0m2.938s
	user	0m2.912s
	sys	0m0.024s
 
 after using cython
 
	time profile_sample1clone
	finish
	
	real	0m3.680s
	user	0m3.631s
	sys	0m0.046s
	
	
