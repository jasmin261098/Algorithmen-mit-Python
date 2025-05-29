class GreedyAlgorithmn:
    pass

def activitySelection(start, finish):
    ans = 0
    arr = []

    for i in range(len(start)):
        arr.append((finish[i], start[i]))

    arr.sort()
    finishtime = -1

    for i in range(len(arr)):
        activity = arr[i]
        if activity[1] > finishtime:
            finishtime = activity[0]
            ans += 1
    return ans

if __name__ == "__main__":
    start = [1, 2, 3, 4, 5, 6]
    finish = [1, 3, 5, 6, 3, 3]
    print(activitySelection(start, finish))