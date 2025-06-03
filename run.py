import json
import os
from src.users.manager import verify_users
from src.support_points.display import menu

support_points = {}
next_id = 0
json_file = "support_points.json"

menu()