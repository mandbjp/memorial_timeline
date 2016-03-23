#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    print "hello"
    import config
    from logic import vine_test
    v = vine_test.Vine(config=config)
    v.start_session().login()

if __name__ == '__main__':
    main()
