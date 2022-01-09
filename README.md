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

### 県IDから市一覧を取得 ( /get_city )
### リクエスト
- pref_id: int

### レスポンス
- city: list
  - city_id: int
  - city_name: string

### ルーム作成 （ /create_room ）
### リクエスト
- room_name: str
- pref_id: int
- city_id: int
- user_id: int
- token: str
- room_description: str (optional)
- topic_id_1: int
- topic_id_2: int (optional)
- topic_id_3: int (optional)

### レスポンス
- room_id: int

### 県IDからルーム一覧を取得 ( /search_rooms_by_prefecture )
### リクエスト
- pref_id: int
- user_id: int
- token: str

### レスポンス
- rooms: list
  - room_id: int
  - room_name: str
  - room_description: str
  - pref_id: int
  - city_id: int
  - topic_id_1: int
  - topic_id_2: int
  - topic_id_3: int

### 市IDからルーム一覧を取得 ( /search_rooms_by_city )
### リクエスト
- city_id: int
- user_id: int
- token: str

### レスポンス
- rooms: list
  - room_id: int
  - room_name: str
  - room_description: str
  - pref_id: int
  - city_id: int
  - topic_id_1: int
  - topic_id_2: int
  - topic_id_3: int

### ルーム情報を取得 ( /get_room )
### リクエスト
- room_id: int
- user_id: int
- token: str

### レスポンス
- room_id: int
- room_name: str
- room_description: str
- pref_id: int
- city_id: int
- topic_id_1: int
- topic_id_2: int
- topic_id_3: int

### ユーザが所属しているルームを取得 ( /get_rooms_by_user_id )
### リクエスト
- user_id: int
- token: str

### レスポンス
- rooms: list
  - room_id: int
  - room_name: str
  - room_description: str
  - pref_id: int
  - city_id: int
  - topic_id_1: int
  - topic_id_2: int
  - topic_id_3: int

### ルームに所属しているユーザを取得 ( /get_users_by_room_id )
### リクエスト
- room_id: int
- user_id: int
- token: str

### レスポンス
- users: list
  - name: str
  - user_id: int
  - email: str
  - birthday: int
  - city: int

### ルームの名前を変更 ( /rename_room )
### リクエスト
- room_id: int
- new_name: str
- user_id: int
- token: str

### レスポンス
なし

### ルームに参加 ( /join_room )
### リクエスト
- room_id: int
- user_id: int
- token: str

### レスポンス
なし