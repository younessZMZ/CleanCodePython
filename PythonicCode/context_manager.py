def stop_database():
    print("systemctl stop postgresql.service")


def start_database():
    print("systemctl start postgresql.service")


def db_backup():
    print("pg_dump database")


class DBHandler:
    def __enter__(self):
        stop_database()
        return self

    def __exit__(self, exc_type, ex_value, ex_traceback):
        start_database()

    @staticmethod
    def do_something():
        print("This function is doing something")


def main():
    with DBHandler() as d:
        db_backup()
        d.do_something()


if __name__ == '__main__':
    main()
