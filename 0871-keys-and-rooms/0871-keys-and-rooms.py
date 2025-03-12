class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        Determines if all rooms can be visited starting from room 0.

        :param rooms: List[List[int]] - Each room contains keys to other rooms.
        :return: bool - True if all rooms can be visited, False otherwise.
        """
        seen = [False] * len(rooms)  # Track visited rooms
        seen[0] = True  # Mark the first room as visited
        stack = [0]  # Use a stack to track rooms to visit

        while stack:
            current_room = stack.pop()  # Get the next room to process
            for key in rooms[current_room]:  # Iterate over keys in the current room
                if not seen[key]:  # If the room hasn't been visited yet
                    seen[key] = True  # Mark it as visited
                    stack.append(key)  # Add it to the stack for future visits

        return all(seen)  # Return True if all rooms have been visited