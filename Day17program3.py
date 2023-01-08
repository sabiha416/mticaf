import sys
print("coding through stdout")

save_stdout=sys.stdout
fh=open(r"d:mtica\test.txt","w")
sys.stdout=fh
print("This line goes to test.txt")
print(input())
sys.stdout=save_stdout
fh.close()

