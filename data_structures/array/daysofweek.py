'''
Given a date, return the corresponding day of the week for that date.
The input is given as three integers representing the day, month and year respectively.
Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.
The given dates are valid dates between the years 1971 and 2100.

Example 1:
Input: day = 31, month = 8, year = 2019
Output: "Saturday"
'''
 # :type day: int , :type month: int , :type year: int , :rtype: str

class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        day_of_week_map = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        t = [ 0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4 ] 
        year -= month < 3
        return day_of_week_map[((year  + int(year / 4) - int(year / 100) + int(year / 400) + t[month - 1] + day) % 7)]