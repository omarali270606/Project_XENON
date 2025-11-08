def is_in(str1, str2):
    return str1 in str2 or str2 in str1

def test_is_in(is_in):
    str1_list = ['a','abc','x','','abc','','a']
    str2_list = ['abc','a','abc','a','','','A']
    expected_results =[True, True, False, True, True, True, False]
    for i in range(len(str1_list)):
        if is_in(str1_list[i],str2_list[i]) != expected_results[i]:
            return False
    return True

test_is_in(is_in)