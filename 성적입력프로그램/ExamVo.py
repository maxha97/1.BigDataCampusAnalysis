import Subject as sb
#캡슐화
class ExamVo:
    def __init__(self, kor=0, eng=0, math=0): #디폴트값을 0으로 지정시, 클래스를 불러들일 때 점수를 입력을 하지 않는 상황에서도 실행되게 해줌
       self.seq = 0
       self.title=""
       self.reg_date = ""
       self.__subject = sb.Subject(kor, eng, math)
        #__는 외부에서 접근을 막아주는 것
        #나만 접근하게하고, setKor처럼 조건에 제약을 줄 수 있음
    
    def setKor(self, kor):
        self.__subject.setKor(kor)
        #외부 접근 방지
        #통제할 수 있는 로직 추가
    
    def getKor(self):
        return self.__subject.getKor()

    def setEng(self, eng):
        self.__subject.setKor(eng)
        #외부 접근 방지
        #통제할 수 있는 로직 추가
    
    def getEng(self):
        return self.__subject.getEng()
    
    def setMath(self, math):
        self.__subject.setMath(math)
        #외부 접근 방지
        #통제할 수 있는 로직 추가
        
    def getEng(self):
        return self.__subject.getMath()


# a = ExamVo(10,20,30)
# a.get_kor()
