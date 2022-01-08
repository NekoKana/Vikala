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
- token: string