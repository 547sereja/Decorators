import os
from datetime import datetime


def parametrized_decor(parameter=os.path.abspath('result.txt')):
    def decor(foo):
        def new_foo(*args, **kwargs):
            result = foo(*args, **kwargs)
            all_logs = f"Time when function was called, {datetime.now()},\n" \
                       f"Function name, {parametrized_decor().__name__},\n" \
                       f"All arguments: {args}, {kwargs},\n" \
                       f"Returned values: {result}"
            with open(parameter, 'w', encoding='utf8') as file:
                file.write(all_logs)
            return result
        return new_foo

    return decor
os.getcwd()


if __name__ == "__main__":
    @parametrized_decor(parameter=os.path.abspath('result.txt'))
    def one(*args, **kwargs):
        list = []
        for i in range(10**4):
            if i % 2 == 0:
                list.append(i)
        return list


    print(one(1, 2, 3, name='bob'))