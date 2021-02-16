
def outer_function(message):
    print(message + ' in ourter function.')

    def nested_function():
        print(message + ' in nexted function.')
    
    return nested_function

return_value = outer_function('Message')
print(return_value())