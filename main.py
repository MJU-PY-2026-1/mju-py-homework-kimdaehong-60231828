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
    print(" 1. 신규 용사 체력 기록 등록")
    print(" 2. 부대 체력측정 종합 통계 조회")
    print(" 3. 체력측정 데이터 파일 저장 (.csv)")
    print(" 4. 프로그램 종료")
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
    elif push_ups >= 56: push_grade = "2급"
    elif push_ups >= 48: push_grade = "3급"
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
    global total_push_ups
    print(f"\n ▶ [신규 용사 데이터 등록]")

    try :
        name = str(input("이름: "))
        rank = str(input("계급 :"))
        run_time = float(input("3km 뜀걸음 기록 (예 : 12.30)"))
        push_ups = int(input("팔굽혀펴기 횟수: "))
        situps = int(input("윗몸일으키기 횟수: "))
    except ValueError:
        print(">> [오류] 올바르지 않은 기록입니다. 메인 메뉴로 돌아갑니다.")
        return

    if run_time < 0 or push_ups < 0 or situps <0:
        print(">> [오류] 음수는 입력할 수 없습니다.")
        return
    
    overall = evaluate_grade(run_time, push_ups, situps)
    total_push_ups += push_ups
    soldiers.append([name, rank, run_time, push_ups, situps, overall])
    print(f">> {rank} {name} 용사의 기록이 성공적으로 저장되었습니다! (등급: {overall})")

def show_statistics():
    if len(soldiers) == 0:
        print("\n>> [알림] 아직 등록된 용사 데이터가 없습니다.")
        return
    
    print("\n" + "=" * 60)
    print(f" 📊 부대 체력측정 세부 조회 (총 {len(soldiers)}명) 📊")
    print("=" * 60)
    
    for i in range(len(soldiers)):
        s = soldiers[i] # s는 ['이름', '계급', 뜀걸음, 팔굽, 윗몸, '종합등급'] 형태의 내부 리스트
        print(f"No.{i+1} | {s[1]} {s[0]} | 뜀걸음:{s[2]:.2f} | 팔굽:{s[3]}개 | 윗몸:{s[4]}개 | 결과: {s[5]}")
    print("=" * 60)

def save_to_file():
    if not soldiers : 
        print("\n>> [오류] 저장할 데이터가 없습니다")
        return
    
    try:
        with open("military_records.csv", "w", encoding="utf-8") as file:
            file.write("이름,계급,뜀걸음,팔굽혀펴기,윗몸일으키기,종합등급\n") # 헤더(머리글) 쓰기
            for s in soldiers:
                file.write(f"{s[0]},{s[1]},{s[2]},{s[3]},{s[4]},{s[5]}\n")
        print("\n>> [성공] 'military_records.csv' 파일로 안전하게 저장되었습니다!")
    except Exception as e:
        print(f"\n>> [오류] 파일 저장 중 문제가 발생했습니다: {e}")

def load_startup():
    try:
        with open("military_records.csv", "r", encoding="utf-8") as file:
            lines = file.readlines()
            print(f"\n>> [시스템 알림] 기존 데이터({len(lines)-1}명)가 존재합니다. 시스템을 시작합니다.")
    except FileNotFoundError:
        print("\n>> [시스템 알림] 기존 저장된 파일이 없습니다. 빈 데이터베이스로 새로 시작합니다.")


load_startup()

while True:
    user_choice = display_menu()

    if user_choice == "1":
        register_soldier()
    elif user_choice == "2" :
        show_statistics()
    elif user_choice == "3" :
        save_to_file()
    elif user_choice == "4" :
        print("\n>> 7군단 강습대대 체력측정 시스템을 종료합니다. \n")
        break 
    else:
        print("1, 2, 3, 4번 중에서 선택해주세요")