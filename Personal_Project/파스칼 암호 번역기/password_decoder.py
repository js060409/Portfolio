def reverse_transform_string(input_str):
    char_list = list(input_str)
    transformed_list = []
    
    for index, char in enumerate(char_list):
        
        if char.isalpha():
            shift = index + 1
            new_char = chr(ord(char) - shift)
            
            if char.islower():
                
                if new_char < 'a':
                    new_char = chr(ord(new_char) + 26)
                    
            elif char.isupper():
                
                if new_char < 'A':
                    new_char = chr(ord(new_char) + 26)
            transformed_list.append(new_char)
            
        else:
            transformed_list.append(char)
    transformed_str = ''.join(transformed_list)
    
    return transformed_str

user_input = input("역변환할 문자열을 입력하세요: ")
result = reverse_transform_string(user_input)
print(result)
