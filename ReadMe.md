# Manipuldate
Date/Time/DateTime Manipulation Done Right
<sub><sub>Still In Active Development - Not Production Ready</sub></sub>

### Badges
[![Build Status](https://travis-ci.org/JenkinsDev/manipuldate.svg?branch=master)](https://travis-ci.org/JenkinsDev/manipuldate)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/JenkinsDev/manipuldate/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/JenkinsDev/manipuldate/?branch=master)

## Installation

`pip install manipuldate`

## Trivial Usage

Here I will just show a very trivial usage, for more in-depth usage options check out our Documentation (Coming Soon TM)

```python
from manipuldate import Manipuldate


today = Manipuldate.today()
# Let's go ahead and print out our current date in a human readable string
print(today.strftime("%m/%d/%Y"))


# Now let's get tomorrow's date
tomorrow = Manipuldate.tomorrow()
print(tomorrow.strftime("%m/%d/%Y"))

# Is tomorrow a weekend?
if tomorrow.is_weekend():
    print("Partayyyyyy")
else:
    print("Get to work!")


# Oh! Let's add a month to tomorrow.
next_month = tomorrow.add_month()
print(next_month.strftime("%m/%d/%Y"))
```
