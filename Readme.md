# Manipuldate
Date/Time/DateTime Manipulation Done Right
<sub><sub>Still In Active Development - Not Production Ready</sub></sub>

### Badges
[![Build Status](https://travis-ci.org/JenkinsDev/manipuldate.svg?branch=master)](https://travis-ci.org/JenkinsDev/manipuldate)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/JenkinsDev/manipuldate/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/JenkinsDev/manipuldate/?branch=master)

## Installation

Coming Soon (Pip Installation): `pip install manipuldate`

Current Installation Process: `git clone https://github.com/JenkinsDev/manipuldate.git`

## Trivial Usage

Here I will just show a very trivial usage, for more in-depth usage options check out our Documentation (Coming Soon TM)

```python
from manipuldate.manipuldate import Manipuldate


today = Manipuldate.today()
# Let's go ahead and print out our current date in a human readable string
today.strftime("%m/%d/%Y")


# Now let's get tomorrow's date
tomorrow = today.tomorrow()
# Now let's print out tomorrow's date in a human readable string
tomorrow.strftime("%m/%d/%Y")

# Is tomorrow a weekend?
if tomorrow.is_weekend():
    pass # Do Some Work
else:
    pass # Well then, it must be a weekday!


# Oh! Let's get today's date next month!
next_month = today.next_month() # Or you can use add_month() or add_months(1)
next_month.strftime("%m/%d/%Y")
```
