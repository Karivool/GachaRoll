rolls = {
    "+1 boost for 1 hour to random buff/debuff": 3.5,
    "+1 boost for 1 hour to buff/debuff of choice": 3.25,
    "+1 boost for 12 hours to random buff/debuff": 3.7,
    "+1 boost for 12 hours to buff/debuff of choice": 3.1,
    "+1 boost for 1 day to random buff/debuff": 3.6,
    "+1 boost for 1 day to buff/debuff of choice": 3,
    "Cooldown time for next Redistribution use reduced 10%": 3,
    "Cooldown time for next Redistribution use reduced 25%": 1.5,
    "Cooldown time for next Redistribution use reduced 33%": 0.75,
    "Cooldown time for next Redistribution use reduced 50%": 0.5,
    "+5 points you can apply to your current ability set": 0.7,
    "+10 points you can apply to your current ability set": 0.4,
    "+1 point added to your pool permanently": 0.2,
    "+2 points added to your pool permanently": 0.1,
    "+5 points added to your pool permanently": 0.05,
    "Random debuff is neutralized for 1 hour": 3.5,
    "Debuff of choice is neutralized for 1 hour": 3.25,
    "Random debuff is neutralized for 12 hours": 3.2,
    "Debuff of choice is neutralized for 12 hours": 3.1,
    "Random debuff is neutralized for 1 day": 3.1,
    "Debuff of choice is neutralized for 1 day": 2.5,
    "Last Chance buff can be used one more time after it revives you": 0.01,
    "Cooldown time for a random buff reduced by 1 day": 3.5,
    "Cooldown time for a buff of choice reduced by 1 day": 2.75,
    "Cooldown time for a random buff reduced by 3 days": 3.3,
    "Cooldown time for a buff of choice reduced by 3 days": 2.65,
    "Cooldown time for a random buff reduced by 1 week": 3.1,
    "Cooldown time for a buff of choice reduced by 1 week": 2.2,
    "Cooldown time for a random debuff increased by 1 day": 3.5,
    "Cooldown time for a debuff of choice increased by 1 day": 2.75,
    "Cooldown time for a random debuff increased by 3 days": 3.3,
    "Cooldown time for a debuff of choice increased by 3 days": 2.65,
    "Cooldown time for a random debuff increased by 1 week": 3.1,
    "Cooldown time for a debuff of choice increased by 1 week": 2.2,
    "Equivalent of $50 USD in cash or your bank account + 3 days of natural life span": 3.75,
    "Equivalent of $100 USD in cash or your bank account + 4 days of natural life span": 3.5,
    "Equivalent of $1,000 USD in cash or your bank account + 5 days of natural life span": 1.8,
    "Equivalent of $2,500 USD in cash or your bank account + 6 days of natural life span": 0.85,
    "Equivalent of $5,000 USD in cash or your bank account + 1 week of natural life span": 0.6,
    "Equivalent of $10,000 USD in cash or your bank account + 2 weeks of natural life span": 0.1,
    "-1 day of natural life span applied to the person of your choice (excluding self)": 2,
    "-2 days of natural life span applied to the person of your choice  (excluding self)": 1.61,
    "-3 days of natural life span applied to the person of your choice  (excluding self)": 0.81,
    "-1 week of natural life span applied to the person of your choice  (excluding self)": 0.31,
    "+1 day of natural life span applied to an animal of your choice (including self)": 1.2,
    "+3 days of natural life span applied to the person of your choice (including self)": 0.81,
    "+1 week of natural life span applied to an animal of your choice (including self)": 0.45,
    "+2 weeks of natural life span applied to an animal of your choice (including self)": 0.25,
    "+1 month of natural life span applied to an animal of your choice (including self)": 0.05,
    "Apply a debuff to a random person of your choice": 0.9
}

def makeRolls(rolls):
    output = []
    totalAmt = 0
    for x in rolls:
        totalAmt += rolls[x] * 100
        output.append([x, int(totalAmt)])
    print(output)
    
makeRolls(rolls)
