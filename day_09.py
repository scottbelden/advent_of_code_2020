from collections import deque

from utils import answer1, answer2, get_input

ANSWER1 = None
ANSWER2 = None

nums = [int(num) for num in get_input("day_09_input")]

preamble = 25

holder = deque(maxlen=preamble)
for num in nums[:preamble]:
    holder.append(num)


def is_valid(holder, num):
    for index, i in enumerate(holder):
        if index + 1 == len(holder):
            break
        for j in list(holder)[index + 1 :]:
            if i + j == num:
                holder.append(num)
                return True
    return False


for num in nums[preamble:]:
    if is_valid(holder, num):
        continue
    else:
        ANSWER1 = answer1(num)
        break


def get_weakness(nums, value):
    for index, num in enumerate(nums):
        total = num
        offset = 1
        while True:
            total += nums[index + offset]
            if total == ANSWER1:
                return min(nums[index : index + offset]) + max(
                    nums[index : index + offset]
                )
            elif total > ANSWER1:
                break
            offset += 1


ANSWER2 = answer2(get_weakness(nums, ANSWER1))
