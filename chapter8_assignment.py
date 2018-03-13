import math

def course_grader(test_scores):
    avg_score = sum(test_scores) / len(test_scores)
    pass_score = "pass"
    fail = "fail"

    if min(test_scores) >= 50 and avg_score >= 70:
        return pass_score
    else:
        return fail



def main():
    print(course_grader([100,75,45]))     # "fail"
    print(course_grader([100,70,85]))     # "pass"
    print(course_grader([80,60,60]))      # "fail"
    print(course_grader([80,80,90,30,80]))  # "fail"
    print(course_grader([70,70,70,70,70]))  # "pass"

if __name__ == "__main__":
    main()


