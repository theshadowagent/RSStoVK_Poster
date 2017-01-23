import time
import rsspost


def main(t_interval):
    posted = rsspost.main()

    while not posted == 'Error':
        posted = rsspost.main()
        time.sleep(t_interval * 60)

    if posted == 'Error':
        print('Лимит постов в эту группу на сегодня превышен. Возвращайтесь завтра')


if __name__ == '__main__':
    time_interval = int(input())
    main(time_interval)

