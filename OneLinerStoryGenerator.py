# ONE LINER STORY GENERATOR.

import random

when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago', 'On 20th Jan']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle', 'a cat']
residence = ['Barcelona', 'India', 'Germany', 'Venice', 'England','Canada']
went = ['cinema', 'university', 'seminar', 'school', 'laundry']
happened = ['made a lot of friends', 'ate a burger', 'found a secret key', 'solved a mistery', 'wrote a book']

print()
story = f'{random.choice(when)}, {random.choice(who)} that lived in {random.choice(residence)}, went to the {random.choice(went)} and {random.choice(happened)}.'
print(story)
