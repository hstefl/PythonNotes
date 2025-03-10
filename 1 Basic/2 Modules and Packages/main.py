# Import specific elements from module
from module_01 import print_hello, PI
# Define namespace for module
import module_02 as m02
# Using modules from simple package
import pkg1.module_11 as m11
import pkg1.module_12 as m22
# Using modules from complex package
import pkg2.pkg21.module_211 as m211


def main() -> None:
    print(f"[main] Starting main method")

    # Playing with modules
    print_hello()
    print(f"[main] PI: {PI}")
    m02.print_hello()
    m11.print_hello()
    m22.print_hello()
    m211.print_hello()


if __name__ == "__main__":
    main()
