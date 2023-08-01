# Handling ordered pairs
def first_member(ordered_pair):
    return ordered_pair[0]

def second_member(ordered_pair):
    return ordered_pair[1]

# Example ordered pair
ordered_pair = (3, 5)
print("First member:", first_member(ordered_pair))
print("Second member:", second_member(ordered_pair))

# Handling ordered triples
def ordered_triple(ordered_pair, third_member):
    return (ordered_pair[0], ordered_pair[1], third_member)

# Example ordered triple
third_member = 7
print("Ordered triple:", ordered_triple(ordered_pair, third_member))


# Answer: First member: 3
#         Second member: 5
#         Ordered triple: (3, 5, 7)
