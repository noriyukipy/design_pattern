import threading


class UnsafeShop:
    """訪れたユーザの数をカウントするクラス。
    複数のスレッドから変更されるインスタンス変数numn_visitorを
    排他制御していないのでスレッドセーフではない。
    """
    def __init__(self):
        self._num_visitor = 0

    def visit(self):
        self._num_visitor += 1

    @property
    def num_visitor(self):
        return self._num_visitor


class SafeShop:
    """UnsafeShop のスレッドセーフ版のクラス"""
    def __init__(self):
        self._num_visitor = 0
        self._condition = threading.Condition(lock=threading.Lock())

    def visit(self):
        with self._condition:
            self._num_visitor += 1

    @property
    def num_visitor(self):
        with self._condition:
            return self._num_visitor


class UserThread:
    def __init__(self, shop):
        self._shop = shop

    def visit_shop(self, n):
        for _ in range(n):
            self._shop.visit()


def run(shop):
    num_each_visit = 500000
    kwargs = {"n": num_each_visit}
    num_threads = 2

    for _ in range(num_threads):
        user = UserThread(shop=shop)
        thread = threading.Thread(target=user.visit_shop, kwargs=kwargs)
        thread.start()

    for _ in range(num_threads):
        # スレッドが完了するまで待機する
        # 行わないと、return shop.num_visitor は処理途中の値を返してしまう
        thread.join()

    return shop.num_visitor, num_each_visit*2


def test_unsafe():
    result, expected = run(UnsafeShop())
    assert result != expected


def test_safe():
    result, expected = run(SafeShop())
    assert result == expected
