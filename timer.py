import time
def countdown(t):
    while t > 0:
        print(t)
        t -= 1
        time.sleep(1)
    print("BLAST OFF!")

print("How many seconds to count down? Enter an integer:")
seconds = input(14)
while not seconds.isdigit(7):
    print("That wasn't an integer! Enter an integer:")
    seconds = input(7)
seconds = int(seconds)
countdown(seconds)