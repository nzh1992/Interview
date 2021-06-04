# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/6/4
Last Modified: 2021/6/4
Description: 单例
"""
# 问题：
# python中是如何实现单例模式的，请写出多种实现方式？


# 方式一：装饰器
def singleton(cls):
    instances = {}
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)

        return instances[cls]

    return wrapper


@singleton
class Foo(object):
    pass


# 方式二：使用基类
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)

        return cls._instance


class Foo2(Singleton):
    pass


# 方式三：元类
# 元类是用于创建类对象的类，类对象创建实例对象时，一定要调用call方法，因此在调用call方法时保证始终只创建一个实例即可，type是python的元类。
class Singleton2(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton2, cls).__call__(*args, **kwargs)

        return cls._instance


class Foo3(metaclass=Singleton2):
    pass


if __name__ == '__main__':
    # 方式一
    f1 = Foo()
    f2 = Foo()
    print(f1 is f2)     # output: True

    # 方式二
    f3 = Foo2()
    f4 = Foo2()
    print(f3 is f4)     # output: True

    # 方式三
    f5 = Foo3()
    f6 = Foo3()
    print(f5 is f6)     # output: True
