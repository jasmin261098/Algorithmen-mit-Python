class DynamicAlgorithm:
    pass

def getFinishTime(activity):
    return activity[1]

def activitySelection(start, finish):
    n = len(start)
    
    activities = list(zip(start, finish))
    activities.sort(key=getFinishTime)

    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if activities[j][1] <= activities[i][0]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

if __name__ == "__main__":
    start = [1, 2, 3, 4, 5, 6]
    finish = [1, 3, 5, 6, 3, 3]
    print(activitySelection(start, finish))