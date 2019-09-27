import argparse
import subprocess
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="file to run forever")
    args = parser.parse_args()

    if args.file:
        while os.path.exists(args.file):
            print('\033[95m' + "\nStarting script " + args.file + '\x1b[0m')
            p = subprocess.Popen("python " + args.file, shell=True)
            p.wait()
            pass
        else:
            print(os.strerror(2))
            return


if __name__ == "__main__":
    main()
