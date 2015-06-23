#! /usr/bin/env python

"""This is a python  module that converts tmperature

"""
def f_to_k(temp):
	converted = ((temp-32.0)*(5.0/9.0))+273.15
	return converted
print(f_to_k(212))

