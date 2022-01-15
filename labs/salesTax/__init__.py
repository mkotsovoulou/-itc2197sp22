import check50
import check50.c

@check50.check()
def exists():
    """salesTax.cpp exists."""
    check50.exists("salesTax.cpp")

@check50.check(exists)
def compiles():
    """salesTax.cpp compiles."""
    check50.run("g++ salesTax.cpp -o salesTax").exit(0)


@check50.check(compiles)
def produces_correct_output():
    """produces correct output for sample input"""
    check50.run(
        "./salesTax ").stdin("100").stdin(".20").stdin("0.24").stdout("100 0.3 0.24 130 31.2 161.2").exit(0)

