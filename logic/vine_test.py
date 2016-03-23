#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


class Vine:
    """
    @see http://ottati.hatenablog.com/entry/2013/08/13/193642
    """
    def __init__(self, config):
        self.session = None
        self.config = config
        self.vine_session_id = None
        pass

    def start_session(self):
        self.session = requests.session()
        return self

    def login(self):
        # ログイン処理
        d = {'username': self.config.VINE_USERNAME, 'password': self.config.VINE_PASSWORD, }
        r = self.session.post("https://api.vineapp.com/users/authenticate", data=d)

        # ログイン時に返ってきたデータに含まれるVineのセッションIDを取得
        self.vine_session_id = r.json()['data']['key']

        # 人気タイムラインを取得
        # ※ HTTP Headerに「vine-session-id」を付与するのがポイント。
        h = {'vine-session-id': self.vine_session_id}

        r = self.session.get("https://api.vineapp.com/timelines/popular", headers=h)
        time_line = r.json()  # タイムラインのデータ

        print time_line
        pass
