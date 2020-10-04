#!/usr/bin/python

n = int(input())
a = set(input().split())
N = int(input())
b = set(input().split())
print(len(a.union(b)))