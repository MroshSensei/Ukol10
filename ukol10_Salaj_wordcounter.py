import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description='ŘádkoSlovoZnakočet napsal Marek Salaj')
    parser.add_argument("nazev", help="Napište název souboru")
    parser.add_argument("--lines", help="součet řádků", action="store_true")
    parser.add_argument("--words", help="součet slov", action="store_true")
    parser.add_argument("--chars", help="součet znaků", action="store_true")
    args = parser.parse_args()

    try:

        if args.chars and args.words and args.lines:
            soubor = open(args.nazev)
            text = soubor.read()
            znaky = len(text)
            radky = len(text.split("\n"))
            slova = len(text.split(" ")) + (radky - 1)
            print(
                f"\n{text} \n\nPočet řádků: [{radky}] \nPočet slov: [{slova}] \nPočet znaků: [{znaky}] \n")
            soubor.close()

        elif args.chars and args.words:
            soubor = open(args.nazev)
            text = soubor.read()
            znaky = len(text)
            radky = len(text.split("\n"))
            slova = len(text.split(" ")) + (radky - 1)
            print(f"\n{text} \n\nPočet slov: [{slova}] \nPočet znaků: [{znaky}] \n")
            soubor.close()

        elif args.chars and args.lines:
            soubor = open(args.nazev)
            text = soubor.read()
            znaky = len(text)
            radky = len(text.split("\n"))
            print(f"\n{text} \n\nPočet řádků: [{radky}] \nPočet znaků: [{znaky}] \n")
            soubor.close()

        elif args.words and args.lines:
            soubor = open(args.nazev)
            text = soubor.read()
            radky = len(text.split("\n"))
            slova = len(text.split(" ")) + (radky - 1)
            print(f"\n{text} \n\nPočet řádků: [{radky}] \nPočet slov: [{slova}] \n")
            soubor.close()

        elif args.chars:
            soubor = open(args.nazev)
            text = soubor.read()
            znaky = len(text)
            print(f"\n{text} \n\nPočet znaků: [{znaky}]\n")
            soubor.close()

        elif args.words:
            soubor = open(args.nazev)
            text = soubor.read()
            radky = len(text.split("\n"))
            slova = len(text.split(" ")) + (radky - 1)
            print(f"\n{text}\n\nPočet slov: [{slova}] \n")
            soubor.close()

        elif args.lines:
            soubor = open(args.nazev)
            text = soubor.read()
            radky = len(text.split("\n"))
            print(f"\n{text}\n\nPočet řádků: [{radky}] \n")
            soubor.close()

        else:
            soubor = open(args.nazev)
            text = soubor.read()
            znaky = len(text)
            radky = len(text.split("\n"))
            slova = len(text.split(" ")) + (radky - 1)
            print(
                f"\n{text} \n\nPočet řádků: [{radky}] \nPočet slov: [{slova}] \nPočet znaků: [{znaky}] \n")
            soubor.close()

    except PermissionError:
        print("Pokus o neoprávněný přístup k souboru")
    except:
        print("Chyba při nahrávání souboru")

if __name__ == "__main__":
    main()