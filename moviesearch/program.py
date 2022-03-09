import requests.exceptions

import movie_svc

def main():
    print_header()
    search_event_loop()


def print_header():
    print("-------------------------------")
    print("           movie search")
    print("-------------------------------")


def search_event_loop():
    search = 'ONCE_THROUGH_LOOP'

    while search != 'x':
        try:
            search = input("movie search text (enter 'x' to exit)")
            if(search != 'x'):
                result = movie_svc.find_movie(search)
                print(f"found {len(result)} matched movies ")
                for r in result:
                    print(f'{r.year}---------------{r.title}')
        except requests.exceptions.ConnectionError:
            print("Error:network down")
        except ValueError:
            print("Search text is required")
        except Exception as X:
            print(f"error {X}")
    print("existing......")


if __name__ == '__main__':
    main()
