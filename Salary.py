def get_salary(job, rank):
    if job == "engineer":
        if rank == "junior":
            return 3000
        elif rank == "associate":
            return 3500
        else:
            return 4000
    elif job == "teacher":
        return 4800
    elif job == "nurse":
        return 2500
    elif job == "professor":
        return 5500
    else:
        return 0


job = "engineer"
rank = "senior"

salary = get_salary(job, rank)
print(salary)
