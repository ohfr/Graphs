import random

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # Add users
        for i in range(0, num_users):
            self.add_user(f"User {i+1}")

        # Create friendships
        # Generate ALL possible friendships
        # Avoid duplicate friendships 
        possible_friendships = []

        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                # user_id == user_id_2 cannot happen
                # if friendship between user_id and user_id_2 already exists
                #   dont add friendship between user_id_2 and user_id
                possible_friendships.append( (user_id, friend_id) )
                
        # print("possible", possible_friendships)

        # lookup = {}
        # new_friendships = []
        # for user_id in self.users:
        #    lookup[user_id] = (user_id, user_id+1)
        
        # for user_id in self.users:
        #     new_friendships.append(lookup[user_id])
            
            
        # Randomly select X friendships
        # the formula for X is  num_users * avg_friendships  // 2 
        # shuffle the array and pick X elements from the front of it
        random.shuffle(possible_friendships)
        num_friendships = num_users * avg_friendships // 2
        for i in range(0, num_friendships):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        queue = Queue()

        queue.enqueue([user_id])

        while queue.size() > 0:
            curPath = queue.dequeue()

            cur = curPath[-1]

            if cur not in visited:
                visited[cur] = curPath

            # make neighbors function
            for v in self.get_neighbors(cur):
                if v not in visited:
                    tempPath = list.copy(curPath)
                    tempPath.append(v)
                    queue.enqueue(tempPath)

        return visited

    def get_neighbors(self, node):
        return self.friendships[node]


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)


## 3. Questions

## 1. To create 100 users with an average of 10 friends each, how many times would you need to call `add_friendship()`? Why?

    # It would be called 500 times because 100 * 10 // 2 = 500, it's divided by 2 because each friendship is a pair (goes both ways)

## 2. If you create 1000 users with an average of 5 random friends each, what percentage of other users will be in a particular user's extended social network? What is the average degree of separation between a user and those in his/her extended network?

    # 
