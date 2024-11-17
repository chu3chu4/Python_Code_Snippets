"""
Parse JSON data to all the students cores from their first test
you are given a variable json_course_data which is a JSON object that holds informaiton about a course and the stuents in that course:
Your task: Inside the get_scores function, return a list of all the students's scores on their first test. you can find the data you need in json_course_data'
"""

# Python code below

show_expected_result = False

import json

thestr = """
{
	"title":"Intermediate Python",
	"students": [
		{
			"name":"Nick",
			"scores": [
				56,
				73,
				68,
				84
			]
		},
		{
			"name":"Jane",
			"scores": [
				88,
				74,
				91,
				73
			]
		},
		{
			"name":"Mark",
			"scores": [
				93,
				66,
				52,
				33
			]
		}
	]
}
"""
json_course_data = json.loads(thestr)

def get_scores():
    first_test_scores = []
    #first_test_scores = [56, 88, 93] # to test if this is the expected result. This is the correct result.
    #first_test_scores = [json_course_data["students"]["scores"][0]]
    #first_test_scores = (json_course_data["Scores"], json_course_data["Jane"][Scores(0)], json_course_data["Mark"][Scores(0)])# another test if this is the expected result

    for student in json_course_data["students"]: #students is a key and its value is a list of 3 dictionaries. what this code does is to loop through the list
        first_test_scores.append(student["scores"][0]) #student is dictionary!. Adds the first value from the list named scores to first_test_score which is a list.

    return first_test_scores

print(get_scores())