from core import translate


def main():
    text = "abandon"
    dest = "fa"
    src = "EN"

    print(translate(text, dest, src))
    return 0


if __name__ == '__main__':
    main()
