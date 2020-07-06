import os


def parametrized_decor(parameter=os.path.abspath('result.py')):
    def decor(foo):
        def new_foo(*args, **kwargs):
            result = foo(*args, **kwargs)
            with open(parameter, 'w', encoding='utf8') as file:
                file.write(parameter)
            return result
        return new_foo

    return decor
os.getcwd()


if __name__ == "__main__":
    @parametrized_decor(parameter=os.path.abspath('result.py'))
    def one(*args, **kwargs):
        list = []
        for i in range(10**4):
            if i % 2 == 0:
                list.append(i)
        return list


    print(one(1, 2, 3, name='bob'))