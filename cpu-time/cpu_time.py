# This program calculate the cpu time
# To determine the quantity of cicles needed on machine A for execute the program
# To determine the program time that will be spent on the machine

from converses_lib import *;

def cicles_quantity(runtime, frequency):
    return runtime * frequency;

def speedup(old_execution_time, expected_speedup):
    return old_execution_time / expected_speedup;

# Coin is cicles of clock for the machine not to die =( default = 1 (100%)
def new_frequency(cicles_quantity, speedup, coin=1):
    return coin * (cicles_quantity/speedup);


runtime = 10; # in nanoseconds
frequency = 400; # in MHz
old_execution_time = runtime; # in nanoseconds
expected_speedup = 1.5; # in seconds
      
cicles_quantity = cicles_quantity(runtime, frequency);
speedup = speedup(old_execution_time, expected_speedup);
new_frequency = new_frequency(cicles_quantity, speedup, 1.2);
    
print(f'{new_frequency:.2f} MHz');
new_frequency = mega_to_giga(new_frequency)
print(f'{new_frequency:.2f} GHz');