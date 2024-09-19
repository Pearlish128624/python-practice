# Return search keyword
print("The program is to return search words from input url. \n")

youtube_keyword = "youtube.com"
baha_keyword = "ani.gamer.com.tw"
# https://www.w3schools.com/tags/ref_urlencode.ASP
_url_encode_dict = {'%2B': '+', '%2A': '*','%25': '%'}

def read_sample()->list:
    INPUT_FILE = "hw\input.txt"
    ANS_FILE = "hw\expect.txt"
    
    inputs = []
    with open(INPUT_FILE, 'r') as f:
        for line in f.readlines():
            inputs.append([line.strip()])
    
    with open(ANS_FILE, 'r') as f:
        i = 0
        for line in f.readlines():
            inputs[i].append(line.strip())
            i += 1
    
    return inputs

def decode_youtube(s: str)->str:
    s = s.partition('=')[-1].replace('+', ' ')
    for key in _url_encode_dict:
        s = s.replace(key, _url_encode_dict[key])
    return s


def decode_baha(s: str)->str:
    s = s.partition('=')[-1].replace('+', ' ')
    for key in _url_encode_dict:
        s = s.replace(key, _url_encode_dict[key])
    return s


def check_answer(_in: str, ans: str, ex_ans:str)->None:
    print("Input:[{}], Answer:[{}]".format(_in, ans))

    _check = "correct" if ans == ex_ans else "wrong"
    print("The answer is %s! \n" % _check)


samples = read_sample()

for sample in samples:
    _input, _expect_output = sample
    if youtube_keyword in _input:
        _answer = decode_youtube(_input)
    elif baha_keyword in _input:
        _answer = decode_baha(_input)

    check_answer(_input, _answer, _expect_output)
    

