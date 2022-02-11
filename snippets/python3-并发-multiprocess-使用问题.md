# python3 并发 multiprocess 使用问题

`multiprocess.Pool` 是用进程实现的进程池，运行时会拷贝整个内存空间，坑太多，性能差，使用 `concurrent.futures.ThreadPoolExecutor` 代替

**NotImplementedError: pool objects cannot be passed between processes or pickled**

pool 对象无法在进程之间传递，其原理是复制，而复制 pool 对象会创建出一个新的进程池，这是一般都是不符合预期，所以不允许这种操作

**AssertionError: daemonic processes are not allowed to have children**

进程不允许有子进程

**AttributeError: module '__main__' has no attribute '__spec__'**

直接运行 `python3 main.py` 可以正常执行，使用 `python3 setup.py install` 安装到本地之后，执行报错

不是代码的问题，python 执行器的问题

## 参考

- pool objects cannot be passed between processes or pickled: <https://stackoverflow.com/questions/25382455/python-notimplementederror-pool-objects-cannot-be-passed-between-processes>
- daemonic processes are not allowed to have children: <https://stackoverflow.com/questions/51485212/multiprocessing-gives-assertionerror-daemonic-processes-are-not-allowed-to-have>
- Python Multiprocessing error: AttributeError: module '__main__' has no attribute '__spec__': <https://stackoverflow.com/questions/45720153/python-multiprocessing-error-attributeerror-module-main-has-no-attribute>
