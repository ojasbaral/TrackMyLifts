from datetime import date, timedelta
import random
# create our user
create = "INSERT INTO users (user_email, user_first_name, user_last_name, user_password) VALUES ('ojas@gmail.com', 'Ojas', 'Baral', '12345678');\n"

# create our splits
create += (
    "INSERT INTO splits (split_name, split_desc, _user_id) VALUES\n"
    "('Push', 'Chest, shoulders, and triceps', 1),\n"
    "('Pull', 'Back and biceps', 1),\n"
    "('Legs', 'Worst day', 1);\n"
)

# create our exercises
create += (
    "INSERT INTO exercises (exercise_name, _split_id) VALUES\n"
    "('Bench Press', 1),\n"
    "('Incline Bench Press', 1),\n"
    "('Dumbell Incline Fly', 1),\n"
    "('Dumbell Shoulder Press', 1),\n"
    "('Dumbell Lateral Raise', 1),\n"
    "('Rope Tricep Pulldowns', 1),\n"
    "('Dumbell Overhead Tricep Extensions', 1),\n"
    "('Lat Pulldowns', 2),\n"
    "('Dumbell Rows', 2),\n"
    "('Barbell Rows', 2),\n"
    "('Rear Delt Flys', 2),\n"
    "('Shrugs', 2),\n"
    "('Bicep Curls', 2),\n"
    "('Hammer Curls', 2),\n"
    "('Barbell Forearm Curls', 2),\n"
    "('Squats', 3),\n"
    "('RDLs', 3),\n"
    "('Bulgarian Split Squats', 3),\n"
    "('Quad Extensions', 3),\n"
    "('Calf Raises', 3);\n"
)

curr = (date.today() - timedelta(days=28))

pushWeights = {
    '1': 135,
    '2': 50,
    '3': 25,
    '4': 35,
    '5': 20,
    '6': 4,
    '7': 20
}

pullWeights = {
    '8': 12,
    '9': 55,
    '10': 135,
    '11': 2,
    '12': 135,
    '13': 27,
    '14': 33,
    '15': 45
}

legsWeights = {
    '16': 155,
    '17': 155,
    '18': 35,
    '19': 13,
    '20': 45
}

"""
create starting weights for each exercise
    update this to the next weight after each sessions

for reps numbers start with 8 apply some weight each set to 3

loop through the days
    if day%7 == 1 || 4 -> push day
        create session
        walk through each exercise and create reps for it

    elif day%7 == 2 || 5 -> pull day
        create session
        walk through each exercise and create reps for it

    elif day%7 == 3 || 6 -> leg day
        create session
        walk through each exercise and create reps for it
"""

# round(x * random.uniform(0.98, 1.03) * 2) / 2.0
sessions = 0
for day in range(1, 29):
    if day % 7 == 1 or day % 7 == 4:
        create += f"INSERT INTO sessions (session_date, _split_id) VALUES ('{curr.isoformat()}', 1);\n"
        sessions += 1
        for key, value in pushWeights.items():
            weight = round(value * random.uniform(0.98, 1.03) * 2) / 2.0
            pushWeights[key] = weight
            for i in range(1, 4):
                create += f"INSERT INTO sets (set_number, weight, reps, _exercise_id, _session_id) VALUES ({i}, {weight}, {round(8*random.uniform(0.8, 1.2))}, {key}, {sessions});\n"

    elif day % 7 == 2 or day % 7 == 5:
        create += f"INSERT INTO sessions (session_date, _split_id) VALUES ('{curr.isoformat()}', 2);\n"
        sessions += 1
        for key, value in pullWeights.items():
            weight = round(value * random.uniform(0.98, 1.03) * 2) / 2.0
            legsWeights[key] = weight
            for i in range(1, 4):
                create += f"INSERT INTO sets (set_number, weight, reps, _exercise_id, _session_id) VALUES ({i}, {weight}, {round(8*random.uniform(0.8, 1.2))}, {key}, {sessions});\n"

    elif day % 7 == 3 or day % 7 == 6:
        create += f"INSERT INTO sessions (session_date, _split_id) VALUES ('{curr.isoformat()}', 3);\n"
        sessions += 1
        for key, value in legsWeights.items():
            weight = round(value * random.uniform(0.98, 1.03) * 2) / 2.0
            legsWeights[key] = weight
            for i in range(1, 4):
                create += f"INSERT INTO sets (set_number, weight, reps, _exercise_id, _session_id) VALUES ({i}, {weight}, {round(8*random.uniform(0.8, 1.2))}, {key}, {sessions});\n"

    curr = (curr + timedelta(days=1))


file = open("db/init_data/insert.sql", 'w')
file.write(create)
