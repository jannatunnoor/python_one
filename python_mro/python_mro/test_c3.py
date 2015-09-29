## http://sebastianraschka.com/Articles/2014_deep_python.html#c3_class_res
## http://python-history.blogspot.ru/2010/06/method-resolution-order.html
## https://www.python.org/download/releases/2.3/mro/
#
# Python has known at least three different MRO algorithms: classic, Python 2.2 
# new-style, and Python 2.3 new-style (a.k.a. C3). Only the latter survives in Python 3.
#
# 1. Classic classes used a simple MRO scheme: when looking up a method, base classes
# were searched using a simple 'depth-first left-to-right' scheme.
# problems: a) Method lookup under "diamond inheritance."
#
## Point 1: The C3 class resolution algorithm for multiple class inheritance

# #######################################
# # Example: 1 
# # (search order: C, A, B, object)
# #######################################
# class A(object):
#     def foo(self):
#         print("class A")

# class B(object):
#     def foo(self):
#         print("class B")

# class C(A, B):
#     pass

# C().foo()
# print type.mro(type(C()))

# #######################################
# # Example: 2 (Nested)
# #######################################
# ## new class hiererchy: (D, B, C, A, object)
# class A(object):
#    def foo(self):
#       print("class A")

# class B(A):
#    pass

# class C(A):
#    def foo(self):
#       print("class C")

# class D(B,C):
#    pass

# D().foo()
# # print type.mro(type(D()))

# ## classical class hiererchy: (D, B, A, C, A)
# class A:
#    def foo(self):
#       print("class A")

# class B(A):
#    pass

# class C(A):
#    def foo(self):
#       print("class C")

# class D(B,C):
#    pass

# D().foo()

# #######################################
# # Example: 3 (Nested - different)
# # (search order: E, C, A, D, B, object)
# #######################################
# class A(object):
#    def foo(self):
#       print("class A")

# class B(object):
#    def foo(self):
#       print("class B")

# class C(A):
#    pass

# class D(B):
#    def foo(self):
#       print("class D")

# class E(C, D):
#    pass

# E().foo()
# print type.mro(type(E()))

# #######################################
# # Example: 4 (Nested - different)
# #######################################
# class A(object):
# 	def foo(self):
# 		print("class A")

# class B(object):
# 	def foo(self):
# 		print("class B")

# class C(A):
# 	pass

# class D(B):
# 	def foo(self):
# 		print("class D")

# class E(A):
# 	def foo(self):
# 		print("class E")

# # # this gives: Cannot create a consistent method resolution order (MRO) for bases E, A
# # class F(D, A, E):
# # 	pass

# # # this gives: Cannot create a consistent method resolution order (MRO) for bases E, A
# # class F(A, E):
# # 	pass

# # search order: F, C, D, B, E, A, object
# class F(C, D, E):
# 	pass

# F().foo()
# print type.mro(type(F()))

# #######################################
# # Example: 5 (Nested - diamond)
# #######################################
# class A(object):
# 	def foo(self):
# 		print("class A")

# class B(A):
# 	def foo(self):
# 		print("class B")

# class C(A):
# 	def foo(self):
# 		print("class C")

# class D(B):
# 	def foo(self):
# 		print("class D")

# class E(C):
# 	def foo(self):
# 		print("class E")

# # search order: F, D, B, E, C, A, object
# class F(D, E):
# 	pass

# F().foo()
# print type.mro(type(F()))

#######################################
# Example: 6 (C3 ambiguity)
#######################################
# F=type('Food',(),{'remember2buy':'spam'})
# E=type('Eggs',(F,),{'remember2buy':'eggs'})
# G=type('GoodFood',(F,E),{}) # under Python 2.3 this is an error!

F=type('Food',(),{'remember2buy':'spam'})
E=type('Eggs',(F,),{'remember2buy':'eggs'})
G=type('GoodFood',(E,F),{})
print G.remember2buy
print type.mro(G)

# Finally, two lessons we have learned from this example:
#
# 1. despite the name, the MRO determines the resolution order of attributes,
#	 not only of methods;
# 2. the default food for Pythonistas is spam ! (but you already knew that ;-)
