import check50
import check50.c

@check50.check()
def Cppexists():
    """Staff.cpp exists."""
    check50.exists("Staff.cpp")


@check50.check(Cppexists)
def Chexists():
    """Staff.h exists."""
    check50.exists("Staff.h")


@check50.check()
def StaffCppexists():
    """testStaff.cpp exists."""
    check50.exists("testStaff.cpp")

@check50.check(StaffCppexists)
def Ccompiled():
   """C++ testStaff executable is generated"""
   check50.exists("testStaff")


@check50.check(Ccompiled)
def Cproduces_correct_output():
    """C++ code produces correct output for sample input"""
    check50.run(
        "./testStaff ").stdout("Maira Kotsovoulou IT").exit(0)


@check50.check()
def Jexists():
    """Staff.java exists."""
    check50.exists("Staff.java")


@check50.check(Jexists)
def Jcompiled():
   """Staff.class java executable is generated"""
   check50.exists("Staff.class")


@check50.check(Jcompiled)
def Jproduces_correct_output():
    """Java code produces correct output for sample input"""
    check50.run(
        "java testStaff ").stdout("Maira Kotsovoulou IT").exit(0)
