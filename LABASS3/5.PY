
def uniform_cost_search(goal, start):
	global graph,cost
	answer = []
	queue = []

	for i in range(len(goal)):
		answer.append(1000)
	queue.append([0, start])
	visited = {}
	count = 0
	while (len(queue) > 0):
		queue = sorted(queue)
		p = queue[-1]
		del queue[-1]

		p[0] *= -1
		if (p[1] in goal):
			index = goal.index(p[1])

			if (answer[index] == 10**8):
				count += 1

		
			if (answer[index] > p[0]):
				answer[index] = p[0]

			
			del queue[-1]

			queue = sorted(queue)
			if (count == len(goal)):
				return answer

		
		if (p[1] not in visited):
			for i in range(len(graph[p[1]])):

				
				queue.append( [(p[0] + cost[(p[1], graph[p[1]][i])])* -1, graph[p[1]][i]])

		visited[p[1]] = 1

	return answer



	
graph,cost = [[] for i in range(6)],{}

graph[0].append(1)
graph[0].append(3)
graph[1].append(4)
graph[1].append(2)
graph[2].append(3)
graph[3].append(4)

	
cost[(0, 1)] = 1
cost[(0, 3)] = 10
cost[(1, 4)] = 15
cost[(1, 2)] = 5
cost[(2, 3)] = 5
cost[(3, 4)] = 5
goal = []

goal.append(3)
answer = uniform_cost_search(goal, 0)

print(answer[0])

