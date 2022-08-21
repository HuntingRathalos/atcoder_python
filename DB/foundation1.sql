create table test_db.test_table (
    id int(6) unsigned default 0 comment "ID"
)
# アクティブDBを指定すると、次回以降のコマンドでDB名省略できる
use test_db:
# 削除
drop table test_db.test_table:
# データ型以降の順番はなんでもいい(id, int(6)以降),最後はカンマなし
create table test_table (
    id int(6) not null comment 'ID'、
    value vacharr(20) unique comment '値'
)
# table定義の確認
desc test_table;
show full colums from sqlite3 import Timestamp
from test_table;
show create table test_table;
# 主キー定義(NOT NULL UNIQUEと同義)
create table test_db.test_table(
    key1 int primary key
);
# 複合主キー(カラムの後に書く表制約を使う)
create table test_db.test_table(
    key1 int,
    key2 int,
    primary key (key1, key2)
);
# auto_incrementを使うにはindex(検索を高速化する仕組み)が振られている必要あり(unique, primary keyなどで割り振られる)
# 1tableにつき一つまで
# default値は設定できない
create table test_db.test_table(
    key1 int auto_increment primary key
);
# index確認
show index from test_db.test_table:

# table定義を変更する
alter table test_db.test_table
add column key2 varchar(20) not null;
add column key3 varchar(20) not null;
# addするからむの順番指定
alter table test_db.test_table
add column key4 varchar(20) after key2;

alter table test_db.test_table
add column key5 varchar(20) first;

# 変更
alter table test_db.test_table
modify column key5 int;
# 削除
alter table test_db.test_table
drop column key5 int;
# index削除
alter table test_db.test_table
drop primary key;
# 外部キー
# 型情報は合わせる、インデックスの自動付与
alter table test_db.test_table(
    add constraint fk_prf_id #外部キー名
    foreign key (pref_id)
    refelences prefs(id) #対象テーブル
    on update cascade
    on update delete;
)
#複数に対する外部キー
alter table test_db.test_table(
    add constraint fk_product_id #外部キー名
    foreign key (product_id)
    refelences products(id) #対象テーブル
    on update cascade
    on update delete,
    add constraint fk_shop_id #外部キー名
    foreign key (shop_id)
    refelences shops(id) #対象テーブル
    on update cascade
    on update delete;
)
# table作成時に外部キー制約
create table test_db.test_table(
    key1 int unsigene auto_increment primary key,
    constraint fk_pref_id #カラム名とは別の制約に対する名前？
    foreign key (pref_id)
    refelences prefs(id) #対象テーブル
    on update cascade
    on update delete;
);
# 削除フラグ、更新日など
create table test_table (
    id int(6) not null comment 'ID'、
    value vacharr(20) unique comment '値',
    delete_flg int(1) not null default 0,
    updated_at timestamp default current_timestampon updated current_timestamp,
    updated_by varchar(20) not null
)
