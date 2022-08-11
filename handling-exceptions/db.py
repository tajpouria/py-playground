import sqlite3


class SQLite:
    def __init__(self, file="application.db"):
        self.file = file

    def __enter__(self):
        conn = sqlite3.connect(self.file)
        self.conn = conn
        cur = conn.cursor()
        return cur

    def __exit__(self, type, value, traceback):
        self.conn.close()


class NotFoundException(Exception):
    pass


class UnauthorizedException(Exception):
    pass


def blog_lst_to_json(item):
    return {
        "id": item[0],
        "published": item[1],
        "title": item[2],
        "content": item[3],
        "public": bool(item[4]),
    }


def fetch_blogs():
    try:
        with SQLite("application.db") as cur:
            cur.execute("SELECT * FROM blogs WHERE public=1")
            result = list(map(blog_lst_to_json, cur.fetchall()))
            return result
    except Exception as e:
        print(e)
        return []


def fetch_blog(id: str):
    try:
        conn = sqlite3.connect("application.db")
        cur = conn.cursor() 

        cur.execute("SELECT * FROM blogs WHERE id=?", [id])
        result = cur.fetchone()

        if result is None:
            raise NotFoundException(f"There is no blog with id {id}")

        data = blog_lst_to_json(result)

        if not data["public"]:
            raise UnauthorizedException(
                f"You are not allowed to access blog with id {id}"
            )

        return data
    except sqlite3.OperationalError as e:
        print(e)
        raise NotFoundException(f"There is no blog with id {id}")
    finally:
        conn.close()
