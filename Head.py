from pystyle import Colors, Colorate, Write, Add, Box
import subprocess
import requests, string, random, argparse, sys, os, time
os.system('cls')

name =  Write.Input("---------------------------------Name the result file-------------------------------- : ", Colors.blue_to_green, interval=0.01)
amount = Write.Input("--------------------------------How many accounts would you like to generate?---------------------------------:", Colors.blue_to_green, interval=0.01)
file_path = "main.py"
print(Box.DoubleCube(Colorate.Horizontal(Colors.blue_to_green, "Results will be saved in " + (name) + ".txt")))
#python spotify_generator.py -n AMOUNT -o OUTPUT_FILE
time.sleep(5)
build = ('python' + " " + file_path + " " + "-n" + " "+ amount + " " + "-o" + " " + name + ".txt")
os.system((build))






