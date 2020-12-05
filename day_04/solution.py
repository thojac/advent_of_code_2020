import re
import sys

sys.path.insert(0,'..')
from advent_lib import *

PATH = 'input.txt'

def read_passports():
    text = open(PATH).read()
    text = re.split(r"\n\n", text)
    text = [group.replace('\n', ' ') for group in text]
    text = [group.split() for group in text]
    passports = [[value.split(':') for value in group] for group in text]
    passports = [{k:v for (k,v) in group} for group in passports]
    return passports

checks = dict()

def register_check(name):
    def decorator(func):
        checks[name] = func
    return decorator

@register_check('byr')
def check_byr(passport):
    byr = int(passport['byr'])
    return byr >= 1920 and byr <= 2002

@register_check('iyr')
def check_iyr(passport):
    iyr = int(passport['iyr'])
    return iyr >= 2010 and iyr <= 2020

@register_check('eyr')
def check_eyr(passport):
    eyr = int(passport['eyr'])
    return eyr >= 2020 and eyr <= 2030

@register_check('hgt')
def check_hgt(passport):
    return re.match(r"^(1[5-8]\d|19[0-3])cm$|^(([5-6]\d|7[0-6])in)$", passport['hgt']) != None

@register_check('hcl')
def check_hcl(passport):
    return re.match(r"^#[0-9a-f]{6}$", passport['hcl']) != None

@register_check('ecl')
def check_ecl(passport):
    return passport['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

@register_check('pid')
def check_pid(passport):
    return re.match(r"^[0-9]{9}$", passport['pid']) != None

def check_fields(passport):
    required = {'byr','iyr','eyr','hgt','hcl','ecl','pid','cid'}
    return required-{key for key in passport.keys()} in (set(), {'cid'})

def is_valid_passport(passport, required):
    if check_fields(passport):
        return sum([check(passport) for check in required]) == len(required)
    else:
        return False

def solve(required):
    passports = read_passports()
    return sum([is_valid_passport(passport, required) for passport in passports])

print(solve([]))
print(solve(list(checks.values())))
