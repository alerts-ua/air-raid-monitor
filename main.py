import json
import time
from urllib.error import HTTPError, URLError
from urllib.request import urlopen
from eink import Eink
from observer import Observable
from ups import is_low_battery, battery_capacity

def get_state():
    with urlopen('https://api.alerts.in.ua/v1/adapters/rpi/alerts/active', timeout=15) as response:
        data = response.read()
        return json.loads(data)
    return None


def main():
    observable = Observable()
    Eink(observable)
    try:
        main_cycle(observable)
    except IOError as e:
        print("IOError: "+str(e))
    except KeyboardInterrupt:
        observable.close()


def main_cycle(observable):
    curr_state = {}
    prev_state = {}
    timeout_count = 0
    curr_battery_capacity = battery_capacity()
    prev_battery_capacity = curr_battery_capacity
    while True:
        try:
            curr_state = get_state()
            timeout_count = 0
        except (HTTPError, URLError) as e:
            print("HTTP,URL Error: "+str(e))
            timeout_count += 1
        finally:
            curr_battery_capacity = battery_capacity()
            battery_capacity_abs = abs(prev_battery_capacity - curr_battery_capacity)
            if timeout_count >= 3:
                curr_state = None
            if curr_state != prev_state or battery_capacity_abs > 5:
                prev_battery_capacity = curr_battery_capacity
                prev_state = curr_state
                observable.update_observers(curr_state)
            time.sleep(10)


if __name__ == "__main__":
    main()
