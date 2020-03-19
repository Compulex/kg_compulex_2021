# kg_compulex_2021

Question: Determine whether a one-to-one character mapping exists from one string, s1, to another string, s2.
For example: 
s1 = abc	s2 = bcd => print true a:b b:c c:d
s1 = foo	s2 = bar => print false character 'o' cannot map to two characters
s1 = bar	s2 = foo => print true b:f a:o r:o


Test Cases:

a b c
b c d
True

f o o
b a r
False

b a r
f o o
True

w i i i
s b b b
True

a b r a c a d a b r a
a b a c a d a b a
False

s u p e r c a l i f r a g i l i s
t i c e x p i a l i d o c i o u s
False

a b c d e f g h i j k l m n o p q r s t u v w x y z
z y x w v u t s r q p o n m l k j i h g f e d c b a
True
