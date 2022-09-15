#!/usr/bin/python python
import os

# Functions
def banner():
  print ("\033[1;32;40mSimple Hash Encrypter")
  print ("---------------------")
  print ("Made by Hyp_r!")
  print ("\033[1;37;40m")
  print ("Input the algorithm you would like to use. Type \"supported\" to see supported algorithms")
  print ("")
banner()

def algorithms():
  print ("")
  print("\033[1;32;40mSUPPORTED ALGORITHMS")
  print ("\033[1;37;40m")
  print ("md5, sha, sha1, sha256, sha384, sha512")
  print ("")

# Getting desired algorithm and string from user
algo = input ("($): ")
if algo == ("supported"):
  algorithms()
  algo = input ("($): ")
print ("")
print ("Input the string you would like to hash")
string = input("($): ")

# Hashing process
print (f"Hashing \033[1;33;40m{string}\033[1;37;40m with \033[1;35;40m{algo}")
print ("\033[1;37;40m")
os.system(f"echo {string} | {algo}sum")

# Credits!
print ("")
print ("Made by Hyp_r!")
print ("\033[1;36;40mhttps://github.com/hyperninja303")
