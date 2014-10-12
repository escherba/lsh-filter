from lsh_filter import LSHCache


def main():
    cache = LSHCache()

    docs = [
        "lipstick on a pig",
        "you can put lipstick on a pig",
        "you can put lipstick on a pig but it's still a pig",
        "you can put lipstick on a pig it's still a pig",
        "i think they put some lipstick on a pig but it's still a pig",
        "putting lipstick on a pig",
        "you know you can put lipstick on a pig",
        "they were going to send us binders full of women",
        "they were going to send us binders of women",
        "a b c d e f",
        "a b c d f"
    ]

    dups = {}
    for i, doc in enumerate(docs):
        dups[i] = cache.insert(doc.split(), i)

    for i, duplist in dups.items():
        if duplist:
            print 'orig [%d]: %s' % (i, docs[i])
            for dup in duplist:
                print'\tdup : [%d] %s' % (dup, docs[dup])
        else:
            print 'no dups found for doc [%d] : %s' % (i, docs[i])


if __name__ == '__main__':
    main()
