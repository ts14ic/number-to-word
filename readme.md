# number-to-word
## Overview
There was a task to take an integer and generate it's word representation following a set of rules in Romanian.
So this was the prototype written in Python.  
The generated sequences might sound unnatural, but that is how they were supposed to be.  

The implementation depends on a list of "magnitude/order" words, which currently end at trillions.
So given a number that is quadrillions or higher, the implementation will start wrap and compose using lower orders.
For example, for a quadrillion it will say "a thousand of trillions" instead of "a quadrillion".
The list of magnitudes can be extended though.

This was a proof of concept, so no future work is planned here.
