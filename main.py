# 파일이름 : 부대 체력측정 관리 시스템
# 작 성 자 : 김대홍
soldiers = []
total_push = 0
push_list = []

print("="*40)
print("[신규 용사 체력 측정 판독기]")
print("="*40)
for i in range(3):
    print(f"\n---{i+1}번째 용사 입력---")
    rank = input("계급을 입력하세요: ")
    name = input("이름을 입력하세요: ")

    run_m = int(input("3km 달리기 (분): "))
    run_s = int(input("3km 달리기 (초): "))
    run_sec = (run_m*60) + run_s

    push = int(input("팔굽혀펴기 (개수): "))
    sit = int(input("윗몸일으키기 (개수): "))

    if run_sec < 0 or sit < 0:
        print(">> [오류] 잘못된 값입니다. 다음으로 넘어갑니다")
        continue

    total_push += push

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
        if push >= 85 and sit >= 95:
            overall = "최우수 특급전사"
        else:
            overall = "특급"

        soldiers.append([rank, name, run_sec, overall])
        push_list.append(push)


print("\n" + "="*40)
print(f"부대 체력측정 통계 (총 {len(soldiers)}명)")
print("="*40)
print(f"중대 팔굽혀펴기 총합: {total_push}개")
print(f"부대 최고 팔굽혀펴기: {max(push_list)}개")
print("-"*40)

for s in soldiers:
    print(f"{s[0]} {s[1]} 결과: {s[3]}")
print("="*40)
