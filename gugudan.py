dan = int(input("단을 입력하세요."))
startGop = int(input("시작 곱을 입력하세요."))
endGop = int(input("끝 곱을 입력하세요."))
start = startGop
while start <= endGop:
    print(f"{dan}  * {start} = {dan * start}")
    start += 1