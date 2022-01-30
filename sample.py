# これからデータベースに接続していく
# サービスの場合は、ユーザー情報などが入っていく。GITの管理にいれてしまうと、間違ってそちらに上げてしまう可能性がある（情報流出となる）
# そうならないために、「.env」というファイルを作った。

import os

from dotenv import load_dotenv

load_dotenv()

print(os.environ.get("SECRET"))
