#! /usr/bin/env python

"""This is a python  module that converts tmperature
This is the idea when I need to change something
	Soudagor mara gelo!

"""
def f_to_k(temp):
	converted = ((temp-32.0)*(5.0/9.0))+273.15
	return converted
print(str(f_to_k(212))+"LMAO")

def k_to_c(temp):
	return temp-273.15

def f_to_c(temp):
	return (k_to_c(f_to_k(temp)))

