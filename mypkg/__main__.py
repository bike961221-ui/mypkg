import argparse


def main():
    parser = argparse.ArgumentParser(
        prog="mypkg",
        description="내가 만든 CLI 프로그램 😎"
    )

    subparsers = parser.add_subparsers(dest="command")

    # add 명령
    add_parser = subparsers.add_parser("add", help="숫자 덧셈")
    add_parser.add_argument("numbers", nargs="+", type=int)

    # mul 명령
    mul_parser = subparsers.add_parser("mul", help="숫자 곱셈")
    mul_parser.add_argument("numbers", nargs="+", type=int)

    args = parser.parse_args()

    if args.command == "add":
        print("덧셈 결과 =", sum(args.numbers))

    elif args.command == "mul":
        result = 1
        for n in args.numbers:
            result *= n
        print("곱셈 결과 =", result)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()

version_parser = subparsers.add_parser("version", help="버전 출력")

elif args.command == "version":
    print("mypkg version 0.1.0 😎")

stats_parser = subparsers.add_parser("stats", help="통계 계산")
stats_parser.add_argument("numbers", nargs="+", type=int)

elif args.command == "stats":
    nums = args.numbers
    print("개수 =", len(nums))
    print("합계 =", sum(nums))
    print("평균 =", sum(nums) / len(nums))

config_parser = subparsers.add_parser("config", help="설정 보기")

elif args.command == "config":
    print("설정 없음 😆 (나중에 추가 가능)")



