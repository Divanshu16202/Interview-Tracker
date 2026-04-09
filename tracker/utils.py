def calculate_readiness(user):
    coding = user.codingpractice_set.count()
    topics = user.studytopic_set.filter(completed=True).count()
    mocks = user.mockinterview_set.count()
    goals = user.goal_set.filter(achieved=True).count()

    score = (coding * 2) + (topics * 3) + (mocks * 5) + (goals * 4)

    return min(score, 100)