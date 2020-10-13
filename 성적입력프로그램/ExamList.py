import ExamVo as ee

class ExamList:
    def __init__(self, list=list(), current=0):
        self.list = list
        self.current = current

    def input_exam(self):
        print("┌───────────────────────────┐")
        print("│        성적  입력         │")
        print("└───────────────────────────┘")

        i = int(self.current) + 1
        while True:
            kor = int(input("국어 %d : " % i))
            if (0 > kor or 100 < kor):
                print("국어성적은 0~100까지의 범위만 입력이 가능합니다.")
            if(0 <= kor and 100 >= kor):
                break

        while True:
            eng = int(input("영어 %d : " % i))

            if (0 > eng or 100 < eng):
                print("영어성적은 0~100까지의 범위만 입력이 가능합니다.")
            if(0 <= eng and 100 >= eng):
                break

        while True:
            math = int(input("수학 %d : " % i))

            if (0 > math or 100 < math):
                print("수학성적은 0~100까지의 범위만 입력이 가능합니다.")
            if(0 <= math and 100 >= math):
                break

        exam = ee.ExamVo()
        exam.kor = kor
        exam.eng = eng
        exam.math = math
        self.current += 1
        self.list.append(exam)
        print("─────────────────────────────")

    def print_exam(self):
        print("┌───────────────────────────┐")
        print("│        성적  출력         │")
        print("└───────────────────────────┘")
        # for i, exam in enumerate(self.get_list()):
        # for i in range(len(self.get_list())):
        for i in range(len(self.list)):   
            exam = self.list[i]
            kor = exam.kor
            eng = exam.eng
            math = exam.math
            total = kor + eng + math
            avg = total / 3.0

            print("[국어 %d : %3d]  " % (i+1, kor), end=" ")
            print("[영어 %d : %3d]  " % (i+1, eng), end=" ")
            print("[수학 %d : %3d]  " % (i+1, math), end=" ")

            print("\n[총점 : %3d]" % total)
            print("[평균 : %6.2f]" % avg)
            print("─────────────────────────────")


# if __name__ == "__main__":
#     exam = ExamOop()
#     exam.main()
