import unittest
import cProfile

fizzbuzz = []

for num in xrange(1,101):
    if num % 5 == 0 and num % 3 == 0:
        print "FizzBuzz"
    elif num % 3 == 0:
        print "Fizz"
    elif num % 5 == 0:
        print "Buzz"
    else:
        print num

class ExampleTests(unittest.TestCase):
    def fizzbuzz_goodtest(f):
        output = []
        for n in range(100):
            output.append(str(f(n) + "\n"))

        expected = open("fizzbuzz-output.txt", "r")
        i = 0
        for line in expected:
            if line == output[i]:
                print("Success!")
                i += 1
            else:
                print("Nope. Try Again.")
if __name__ == "__main__":
    unittest.main()
	
cProfile.runctx('fizzbuzz', globals(), locals(), 'myProfilingFBFile.pstats')

python gprof2dot -f pstats myProfileFBFile | dot -Tpng -o image_output.png