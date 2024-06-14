# 841. Keys and Rooms
# Medium
# Topics
# Companies
# There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

# When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

# Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

 

# Example 1:

# Input: rooms = [[1],[2],[3],[]]
# Output: true
# Explanation: 
# We visit room 0 and pick up key 1.
# We then visit room 1 and pick up key 2.
# We then visit room 2 and pick up key 3.
# We then visit room 3.
# Since we were able to visit every room, we return true.
# Example 2:

# Input: rooms = [[1,3],[3,0,1],[2],[0]]
# Output: false
# Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.



def canVisitAllRooms(rooms):

	keys_in_hand = rooms[0]

	rooms_unlocked = {0}

	while keys_in_hand:

		room_to_unlock = keys_in_hand.pop()

		if room_to_unlock not in rooms_unlocked:

			rooms_unlocked.add(room_to_unlock)

			keys_in_hand += rooms[room_to_unlock]

	return len(rooms_unlocked) == len(rooms)

print(canVisitAllRooms([[1],[2],[3],[]]))
