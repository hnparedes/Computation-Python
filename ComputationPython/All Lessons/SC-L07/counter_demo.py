from counter import Counter

tally = Counter()

tally.reset()

tally.setLimit(2)

tally.click()
tally.click()
tally.click()

result = tally.getValue()
print("Value:", result)

tally.click()
tally.click()
result = tally.getValue()
print("Value:", result)
