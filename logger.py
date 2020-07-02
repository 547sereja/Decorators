from datetime import datetime


def logger(old_func):
    def new(*args, **kwargs):
        where_to_save = input("Enter where to save: ")
        result = old_func(*args, **kwargs)
        all_logs = f"Time when function was called, {datetime.now()},\n" \
                   f"Function name, {old_func.__name__},\n" \
                   f"All arguments: {args}, {kwargs},\n" \
                   f"Returned values: {result}"

        with open(where_to_save, 'w', encoding='utf8') as file:
            file.write(all_logs)
        return result
    return new


if __name__ == "__main__":
    @logger
    def one(*args, **kwargs):
        list = []
        for i in range(10**4):
            if i % 2 == 0:
                list.append(i)
        return list


    print(one(1, 2, 3, name='bob'))