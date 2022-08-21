# 文字列の場合クォーテーション必要
insert into test_db.table名(属性１、属性２) values ("値１", 値２)
# 単一レコード
insert into test_db.prefs(name, updated_by) values ("北海道", "yokogi");
# 複数レコード
insert into test_db.prefs(name, updated_by) values
("山形", "yokogi"),
("青森", "yokogi");

select * from test_db.prefs
# asでlabelをつけられる(asは省略可)
# mp は as mpの省略table名にlabelをつけてるイメージ
# count(*)はcount(1)でもおけ
select count(*) as "件数" from test_db.prefs mp
select count(*) as "件数" from test_db.prefs
select count(*) "件数" from test_db.prefs

# この場合はnameにlabelをつけている
select id, name "都道府県名" from test_db.prefs
# distinctで重複レコード省けるnameが北海道のレコード２件あったら１件だけ取得する
select count(distinct name) "都道府県名" from test_db.prefs

# レコード全件削除
delete from test_db.prefs;

# auto_incrementの初期化(レコード削除時にincrenemtを振り直すため)
alter table test_db.prefs auto_increment = 1;
-- 一致
select * from test_db.stocks
where product_id = 1;
-- 非一致(!=または<>)
select * from test_db.stocks
where product_id != 1;
-- 数値の比較
select * from test_db.stocks
where amount > 50;
-- AND条件,OR条件
select * from test_db.stocks
where product_id = 1 and shhp_id = 1;

select * from test_db.stocks
where product_id = 1 or shhp_id = 1;
-- 条件を括る
select * from test_db.stocks
where (product_id = 1 and shhp_id = 1)
or (product_id = 2 and shhp_id = 2);
-- 部分検索一致
select * from test_db.shops
where name like '店舗%'; -- 店舗A、店舗Bみたいなやつ

select * from test_db.shops
where name like '店%A'; -- 店舗Aなど
-- いずれかの値に一致(not inで否定にできる)
select * from test_db.shops
where name in ('店舗A', '店舗B');
-- AからBの値
select * from test_db.shops
where amount between 60 and 100;
-- null以外に一致
select * from test_db.shops
where amount is not null;
-- ソート
-- defaultはasc(昇順)
select * from test_db.stocks
order by amount;
select * from test_db.stocks
order by amount desc;
-- 条件付けも併用できる
select * from test_db.stocks
where amount > 50
order by amount desc;
-- 複数キーでソート(product_idでソート後、shop_idでソートされる)
select * from test_db.stocks
order by product_id desc,
shop_id asc;
-- 取得件数を制限する
select * from test_db.stocks
order by product_id desc,
shop_id asc
limit 1;
-- 0インデックススタートなので、この場合2つ目のレコードから2つ取得
select * from test_db.stocks
order by product_id desc,
shop_id asc
limit 2 offset 1;
-- 以下も同義
select * from test_db.stocks
order by product_id desc,
shop_id asc
limit 1, 2;
