# 파일이름 : 부대 체력측정 관리 시스템
# 작 성 자 : 김대홍
print("="*40)
("[신규 용사 체력 측정 판독기]")
print("="*40)
rank = input("계급을 입력하세요: ")
name = input("이름을 입력하세요: ")

run_m = int(input("3km 달리기 (분): "))
run_s = int(input("3km 달리기 (초): "))
run_sec = (run_m*60) + run_s

push = int(input("팔굽혀펴기 (개수): "))
sit = int(input("윗몸일으키기 (개수): "))


if run_sec <= 750:
    run_grade = "특급"
elif run_sec <= 810:
    run_grade = "1급"
elif run_sec <= 870:
    run_grade = "2급"
elif run_sec <= 930:
    run_grade = "3급"
else:
    run_grade = "불합격"

if push >= 72:
    push_grade = "특급"
elif push >= 64: 
    push_grade = "1급"
elif push >= 56: 
    push_grade = "2급"
elif push >= 48: 
    push_grade = "3급"
else:
    push_grade = "불합격"

if sit >= 86:
    sit_grade = "특급"
elif sit >= 78: 
    sit_grade = "1급"
elif sit >= 70: 
    sit_grade = "2급"
elif sit >= 62: 
    sit_grade = "3급"
else:
    sit_grade = "불합격"

if run_grade == "불합격" or push_grade == "불합격" or sit_grade == "불합격":
    overall = "불합격"
elif run_grade == "3급" or push_grade == "3급" or sit_grade == "3급":
    overall = "3급"
elif run_grade == "2급" or push_grade == "2급" or sit_grade == "2급":
    overall = "2급"
elif run_grade == "1급" or push_grade == "1급" or sit_grade == "1급":
    overall = "1급"
else:
    overall = "특급"

if overall == "특급":
    vacation = "특급 전사 (4박5일 포상휴가 부여)"
else:
    vacation = "대상 아님"


print("\n" + "="*40)
print(f"[{rank} {name}] 체력 측정 결과")
print("="*40)
print(f"3km 달리기 : {run_m}분 {run_s}초 ({run_grade})")
print(f"팔굽혀펴기 : {push}개 ({push_grade})")
print(f"윗몸일으키기 : {sit}개 ({sit_grade})")
print("="*40)
print(f"종합 체력 등급 : {overall}")
print(f"포상휴가 여부 : {vacation}")
print("="*40)

run
