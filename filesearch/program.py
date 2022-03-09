# print header
# get folder from user
# get search text from user
# search_file
import collections
import os.path

searchresult = collections.namedtuple('searchresult', 'file line text')


def main():
    txt = ""
    print_header()
    folder = get_folder_from_user()
    if folder:
        txt = get_search_text_from_user()

    matches = search_file(folder, txt)
    line_count = 0
    for m in matches:
        print(f"file name: {m.file}")
        print(f"line number: {m.line}")
        print(f"text: {m.text}")
        line_count += 1
    print(f"total line {line_count}")


def print_header():
    print('-------------------------------------')
    print('         search text in file')
    print('-------------------------------------')


def get_folder_from_user():

    folder = input("enter the folder name u want to search")
    if not folder or not folder.strip():
        return None
    if os.path.isdir(folder):
        return folder
    else:
        return False


def get_search_text_from_user():
    txt = "happy"  # input("enter the text to search")
    return txt.lower()


def search_file(folder, txt):
    # allmatches = []
    items = os.listdir(folder)
    for item in items:
        full_item_path = os.path.join(folder, item)
        if os.path.isdir(full_item_path):
            matches = search_file(full_item_path, txt)
            # allmatches.extend(matches)
            for m in matches:
                yield m
        else:
            yield from search_txt(full_item_path, txt)
            # matches = search_txt(full_item_path, txt)
            # allmatches.extend(matches)

    # return allmatches


def search_txt(item_full_path, txt):
    try:
        # matches = []
        line_number = 0
        with open(item_full_path, 'r', encoding='utf-8') as fout:
            for line in fout:
                line_number += 1
                if line.lower().find(txt) >= 0:
                    m = searchresult(file=item_full_path, line=line_number, text=line)
                    yield m
                    # matches.append(m)
        # return matches
    except UnicodeDecodeError:
        print(f"Notice: binary file {item_full_path} is skipped")


if __name__ == '__main__':
    main()
