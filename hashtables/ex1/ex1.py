def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # so first up is making a dictionary with all the value combinations
    combinations={}
    for i in range(limit+1):
        combinations[i]= limit-i
    # print(combinations)
    #going to also make our list a dictionary for O(1) lookup
    weights_dict={}
    for index, value in enumerate(weights):
        if value in weights_dict:
            weights_dict[value].append(index)
        elif value<=limit:
            weights_dict[value]=[index]
    #now we loop through weights and see which match the table
    for item in weights:
        if item >= limit:
            continue
        if combinations[item] in weights_dict:
            if(len(weights_dict[combinations[item]]) > 1):
                # print(weights_dict[combinations[item]])
                result = weights_dict[combinations[item]].sort(reverse=True)
                return (weights_dict[combinations[item]])
            else:
                result= weights_dict[item] + weights_dict[combinations[item]]
                result.sort(reverse=True)
                return(result)

        
    # print(weights_dict)
    return None
weights_2 = [4, 5]
print(get_indices_of_item_weights(weights_2, 2, 9))