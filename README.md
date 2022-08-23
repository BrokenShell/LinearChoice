# Linear Choice Algorithm
***When flat uniform distributions aren't good enough.***

We'll be creating a component to generate random values from a given collection. This collection could be a list, tuple, set or possibly an iterator, and it could hold any type of value. Our algorithm should be able to produce distributions of output that matches each of the standard linear distributions.

- Front: values at the front of the collection are more common
- Middle: values at the middle of the collection are more common
- Back: values at the back of the collection are more common


### Linear Choice: Front
```
Output Analysis: LinearChoice.front()
Typical Timing: 776 ± 62 ns
Distribution of 100000 samples:
 A: 26.429%
 B: 22.362%
 C: 18.447%
 D: 14.299%
 E: 10.225%
 F: 6.213%
 G: 2.025%
```

### Linear Choice: Middle
```
Output Analysis: LinearChoice.middle()
Typical Timing: 1086 ± 182 ns
Distribution of 100000 samples:
 A: 3.954%
 B: 12.241%
 C: 20.537%
 D: 26.521%
 E: 20.484%
 F: 12.258%
 G: 4.005%
```

### Linear Choice: Back
```
Output Analysis: LinearChoice.back()
Typical Timing: 846 ± 67 ns
Distribution of 100000 samples:
 A: 2.021%
 B: 6.056%
 C: 10.152%
 D: 14.364%
 E: 18.4%
 F: 22.529%
 G: 26.478%
```
