from collections import deque


def produce_elements(dq, n):
    for i in range(n):
        if len(dq) < dq.maxlen:
            dq.append(i)
        else:
            print('Queue full...')
            yield


def consume_elements(dq):
    while True:
        while len(dq) > 0:
            processed = dq.pop()
            print(f'Processed {processed}')
        yield


def coordinator():
    dq = deque(maxlen=10)
    producer = produce_elements(dq, 30)
    consumer = consume_elements(dq)

    while True:
        try:
            next(producer)
        except StopIteration:
            break
        finally:
            next(consumer)


