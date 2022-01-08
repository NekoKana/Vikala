# Vikala
Neon 用の Web API です。

## エンドポイント
### ユーザ登録 ( /signup )
#### リクエスト
- name: string
- email: string
- password: string
- birthday: int
- city: int
- topic_list: int[]

#### レスポンス
- user_id: int
- token: string

### ログイン ( /login )
#### リクエスト
- email: string
- password: string

#### レスポンス
- user_id: int
- token: 

### ユーザ情報取得 ( /get_user )
#### リクエスト
- user_id: int
- token: string

#### レスポンス
- name: string
- user_id: int
- email: string
- birthday: int
- city: int
- topic: int[]

### ユーザにトピックを追加 ( /add_topics )
#### リクエスト
- user_id: int
- token: string
- topics: int[]

#### レスポンス
なし