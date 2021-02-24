
#!/usr/bin/env python3

def func(fore_color='black', back_color='white', link_color='blue', visited_color='yellow'):
    return (fore_color, back_color, link_color, visited_color)

def test1_func():
    test = ('red', 'blue', 'yellow', 'chartreuse')
    assert test == func('red', 'blue', 'yellow', 'chartreuse')

def test2_func():
    test = ('black', 'blue', 'red', 'yellow')
    assert test == func(link_color='red', back_color='blue')

def test3_func():
    test = ('purple', 'blue', 'red', 'yellow')
    assert test == func('purple', link_color='red', back_color='blue')

regular = ('red', 'blue')
links = {'link_color': 'chartreuse'}

def test4_func():
    test = ('red', 'blue', 'chartreuse', 'yellow')
    assert test == func(*regular, **links)

def func2(*args, **kwargs):
    print('args: ', args)
    print('kwargs: ', kwargs)
    return (args, kwargs)

def test1_func2():
    test = (('red', 'blue', 'yellow', 'chartreuse'), {})
    assert test == func2('red', 'blue', 'yellow', 'chartreuse')

def test2_func2():
    test = ((), {'link_color': 'red', 'back_color': 'blue'})
    assert test == func2(link_color='red', back_color='blue')

def test3_func2():
    test = (('purple',), {'link_color': 'red', 'back_color': 'blue'})
    assert test == func2('purple', link_color='red', back_color='blue')

def test4_func2():
    test = (('red', 'blue'), {'link_color': 'chartreuse'})
    assert test == func2(*regular, **links)


