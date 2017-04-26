# HelloCI
Demo implementation for CI


First, I used xrange method and did not use // to get integers from the division. This has caused the build to fail for Python 3.6 but not for Python 2.7.
Then, I changed xrange to range and used the operand // for the division to get integers. This resulted in successful builds for both versions.
