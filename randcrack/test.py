import random
import time
from randcrack import RandCrack

random.seed(time.time())

unknown = [random.getrandbits(32) for _ in range(10)]

cracker = RandCrack()

for _ in range(624):
    cracker.submit(random.getrandbits(32))

cracker.offset(-624)  # Go back -624 states from submitted numbers
cracker.offset(-10)   # Go back -10 states to the start of `unknown`

print("Unknown:", unknown)
print("Guesses:", [cracker.predict_getrandbits(32) for _ in range(10)])
