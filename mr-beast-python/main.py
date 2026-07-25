from datetime import datetime

# take the max number from user
maxNum = int(input("Enter the max number: "))


# files numbers
# maxFileNum = int(input("Enter the max file: number: "))

FILE_NAME = "mr_file"
FILE_EXT = ".txt"

time1 = datetime.now()


for n in range(maxNum):
    print(f"[Info] Creating \'{FILE_NAME}_{n+1}{FILE_EXT}\' file...")
    with open(f"store/{FILE_NAME}_{n+1}{FILE_EXT}", "w") as file:
        file.write(str(n + 1))


time2 = datetime.now()

duration = time2 - time1

print(f"\n[Time] {duration.seconds // 3600}h {duration.seconds // 60}m {duration.seconds % 60}s {duration.microseconds}ms\n")
Commit at 2026-07-29T09:42:27
