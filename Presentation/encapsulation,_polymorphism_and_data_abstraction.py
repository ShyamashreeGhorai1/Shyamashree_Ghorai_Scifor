# -*- coding: utf-8 -*-
"""Encapsulation, polymorphism and Data Abstraction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/148XqM_xc3SOBMxrL2KfHvq60MJcRWry4
"""

from abc import ABC

class Car(ABC):
  def mileage(self):
    pass

class BMW(Car):
  def mileage(self):
    print("The mileage is 23KMPH")

class Suzuki(Car):
  def mileage(self):
    print("The mileage is 34KMPH")






