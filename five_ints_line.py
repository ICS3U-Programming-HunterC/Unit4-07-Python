#!/usr/bin/env python3
# Created by: Hunter Connolly
# Created on: May 3, 2022
# This program uses one for loop and one if statement, prints the integers from 1000 to 2000
# outputting five integers per line with each separated by a space


def main():
    for counter in range(1000, 2000 + 1):
        if counter % 5 == 0 and counter != 1000:
            print()
        print(counter, end=" ")


if __name__ == "__main__":
    main()
