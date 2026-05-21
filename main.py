# 파일이름 : 부대 체력측정 관리 시스템
# 작 성 자 : 김대홍
soldiers = []
total_push_ups = 0
push_ups_list = []

print("="*40)
def display_menu():
    print("\n" + "=" * 50)
    print("체력측정 관리 시스템")
    print("="*50)
    print("1. 신규 용사 체력 기록 등록")
    print(" 2. 부대 체력측정 종합 통계 조회")
    print(" 3. 프로그램 종료")
    print("=" * 50)
    choice = input("원하시는 메뉴 번호를 입력하세요: ")
    return choice

def evaluate_grade(run_time, push_ups, situps) :
    if run_time <= 12.30: run_grade = "특급"
    elif run_time <= 13.30: run_grade = "1급"
    elif run_time <= 14.30: run_grade = "2급"
    elif run_time <= 15.30: run_grade = "3급"
    else: run_grade = "불합격"

    if push_ups >= 72 : push_grade = "특급"
    elif push_ups >= 64 : push_grade = "1급"
    elif pushups >= 56: push_grade = "2급"
    elif pushups >= 48: push_grade = "3급"
    else: push_grade = "불합격"

    if situps >= 86: sit_grade = "특급"
    elif situps >= 78: sit_grade = "1급"
    elif situps >= 70: sit_grade = "2급"
    elif situps >= 62: sit_grade = "3급"
    else: sit_grade = "불합격"

    if run_grade == "불합격" or push_grade =="불합격" or sit_grade == "불합격" :
        final_grade = "불합격"
    elif run_grade == "3급" or push_grade == "3급" or sit_grade == "3급":
        final_grade = "3급"
    elif run_grade == "2급" or push_grade == "2급" or sit_grade == "2급":
        final_grade = "2급"
    elif run_grade == "1급" or push_grade == "1급" or sit_grade == "1급":
        final_grade = "1급"       
    else:
        if push_ups >= 85 and situps >= 95 :
            final_grade = "*최우수 특급전사*"
        else : 
            final_grade =  "특급전사"
    return final_grade

def register_soldier():
    global total_pushups

    print(f"\n ▶ [신규 용사 데이터 등록]")
    name = str(input("이름: "))
    rank = str(input("계급 :"))
    run_time = float(input("3km 뜀걸음 기록 (예 : 12.30)"))
    push_ups = int(input("팔굽혀펴기 횟수: "))
    situps = int(input("윗몸일으키기 횟수: "))

    if run_time < 0 or push_ups < 0 or situps <0:
        print(">> [오류] 올바르지 않은 기록입니다. 메인 메뉴로 돌아갑니다.")
        return
    
    overall = evaluate_grade(run_time, push_ups, situps)

    total_pushups += push_ups
    soldiers.append([name, rank, run_time, overall])
    push_ups_list.append(push_ups)

    print(f">> {rank} {name} 용사의 기록이 성공적으로 저장되었습니다! (등급: {overall})")

def show_statistics():
    if len(soldiers) == 0:
        print("\n>> [알림] 아직 등록된 용사 데이터가 없습니다.")
        return
    
    push_ups_list.sort(reverse=True)
    count = len(soldiers)
    max_record = max(push_ups_list)

    print("\n" + "=" * 50)
    print(f" 📊 부대 체력측정 종합 통계 (총 {count}명) 📊")
    print(f" - 중대 팔굽혀펴기 총합: {total_pushups}개")
    print(f" - 최고 기록자 점수: {max_record}개")
    print("-" * 50)
    for s in soldiers:
        print(f"[{s[1]} {s[0]}] 종합 등급: {s[3]} (뜀걸음: {s[2]})")
    print("=" * 50)

while True:
    user_choice = display_menu()

    if user_choice == "1":
        register_soldier()
    elif user_choice == "2" :
        show_statistics()
    elif user_choice == "3" :
        print("\n>> 7군단 강습대대 체력측정 시스템을 종료합니다. 충성!\n")
        break 
    else:
        print("1, 2, 3번 중에서 선택해주세요")