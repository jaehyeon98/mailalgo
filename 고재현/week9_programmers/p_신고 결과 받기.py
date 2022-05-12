def solution(id_list, report, k):
    r_tmp = {}

    num = {}
    ans = {}
    for name in id_list:
        num[name] = 0
        ans[name] = 0

    for i in range(len(report)):
        reporter = report[i].split()[0]
        reportee = report[i].split()[1]

        if reporter in r_tmp.keys():
            if reportee not in r_tmp[reporter]:
                num[reportee] += 1
                r_tmp[reporter].append(reportee)
        else:
            num[reportee] += 1
            r_tmp[reporter] = [reportee]

    for i in num.keys():
        if num[i] >= k:
            for z in r_tmp.keys():
                if i in r_tmp[z]:
                    ans[z] += 1

    answer = [0] * len(id_list)
    for i in ans.keys():
        for j in range(len(id_list)):
            if i == id_list[j]:
                answer[j] = ans[i]
    return answer