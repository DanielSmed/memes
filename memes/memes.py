from QA_CSE_102 import QA_CSE_102
from Assignment_5 import Assignment_5

if __name__ == "__main__":
    meme_test = True
    while meme_test:
        print("0: quit")
        print("1: QA_CSE_102")
        print("2: Assignment_5")
        meme = int(input("input meme number: "))
        if  meme == 0:
            meme_test = False
        elif meme == 1:
            QA_CSE_102.QA_CSE_102(int(input("QA_CSE_102, Number of lines: ")))
        elif meme == 2:
            Assignment_5.Assignment_5(int(input("Assignment_5, For n=")))
    print("Good bye")