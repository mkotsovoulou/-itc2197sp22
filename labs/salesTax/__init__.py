import check50
import check50.c



@check50.check()
def exists():
    """salesTax.cpp exists."""
    check50.exists("salesTax.cpp")

@check50.check(exists)
def compiles():
    """salesTax.cpp compiles."""
    check50.c.compile("salesTax.cpp", lcs50=True)


@check50.check(compiles)
def produces_correct_output():
    """encrypts "a" as "b" using 1 as key"""
    check50.run(
        "./salesTax").stdin("100").stdin(".20").stdin("0.24").stdout("100 0.30 0.24 130 31.2 161.2").exit(0)

