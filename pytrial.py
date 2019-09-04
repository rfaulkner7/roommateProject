import sched, time, json, requests
api_key = "CY3MCLHOMLVH2KBT"
api_base = "https://api.iextrading.com/1.0/tops?symbols=fb,%2b"
s = sched.scheduler(time.time, time.sleep)
def do_something(sc):
    response = requests.get('https://api.iextrading.com/1.0/tops?symbols=fb,%2b')
    print(response.text)
    s.enter(15,1,do_something, (s,))

s.enter(1,1,do_something, (s,))
s.run()
