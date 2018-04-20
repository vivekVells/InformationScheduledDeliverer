from __future__ import absolute_import, unicode_literals
import random
from celery import task

@task(name="multiply_two_numbers")
def mul(x, y):
    total = x * (y * random.randint(3, 100))
    print("total: ", total)
    return total
