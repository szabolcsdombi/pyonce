# [pyonce](https://pypi.org/project/pyonce/)

Run code once! -- or once in a while...

```py
def once(every: int = 0, key: Any = None) -> bool
```

### Example

```py
import pyonce


def update():
    if pyonce.once(key='ONCE-001'):
        print('global unique key')
    if pyonce.once():
        print('this is called from update')
    if pyonce.once(every=5):
        print('update() / 5')


for i in range(10):
    if pyonce.once(every=2):
        print(f'hello {i}')
    update()
    update()
```

**output**

```
hello 0
global unique key
this is called from update
update() / 5
this is called from update
update() / 5
hello 2
hello 4
update() / 5
update() / 5
hello 6
hello 8
```

The `once()` function relies on the traceback to derive the key.
A unique key corresponds to a unique state which is a simple counter.
When the counter hits zero the return value is `True`.
The first call for a key is always `True`.

---

Do not use it in production, such magic is pure evil.
