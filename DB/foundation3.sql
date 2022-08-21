-- レコードの更新(事故防止のためにselectで更新前に確認するのが良い)
select * from test_db.stocks
where product_id = 1 and shop_id = 1;

update test_db.stocks set amount = 50
where product_id = 1 and shop_id = 1;
-- 削除も同様に確認してから消す
delete from test_db.stocks
where product_id = 1 and shop_id = 1;
-- 複数カラムを更新
update test_db.stocks set amount = amount - 10, delete_flg = 1
where product_id = 1 and shop_id = 1;
-- inner join(内部結合)
select * from テーブル１
inner join テーブル２
on テーブル１.値が一致する属性 = テーブル２.値が一致する属性
-- 両テーブルのレコード取得
select * from test_db,shops sh
inner join test_db,prefs pr
on sh.pref_id = pr.id;
-- pref_idがprefテーブルのidに一致するレコードでshopsテーブルの部分のみを取得
select sh.* from test_db,shops sh
inner join test_db,prefs pr
on sh.pref_id = pr.id;
-- 右テーブルのレコード取得
select pr.* from test_db,shops sh
inner join test_db,prefs pr
on sh.pref_id = pr.id;
-- カラム指定もできる
select sh.name, pr.* from test_db,shops sh
inner join test_db,prefs pr
on sh.pref_id = pr.id;

select sh.name "店舗名", pr.name "都道府県名" from test_db,shops sh
inner join test_db,prefs pr
on sh.pref_id = pr.id;
-- where句でも結合できる
select sh.name "店舗名", pr.name "都道府県名"
from test_db,shops sh, test_db,prefs pr
where sh.pref_id = pr.id;
-- 結合後に条件指定
select sh.name "店舗名", pr.name "都道府県名" from test_db,shops sh
inner join test_db,prefs pr
on sh.pref_id = pr.id
where sh.id = 1;
-- where句の場合はandで繋ぐ
select sh.name "店舗名", pr.name "都道府県名"
from test_db,shops sh, test_db,prefs pr
where sh.pref_id = pr.id
and sh.id = 1;

-- left join(外部結合)
-- 左外部結合(left joinの後のテーブルは右テーブルのこと)
-- 逆のイメージだから注意する
-- 左テーブルは全て取得して、右テーブルについてはonで取得できたもののみ
select * from 左テーブル
left join 右テーブル
on 左テーブル.値が一致する属性 = 右テーブル.値が一致する属性

select * from test_db.prefs pr
left join test_db.shops sh
on sh.pref_id = pr.id;
-- カラム指定
select pr.name "都道府県名", sh.name "店舗名"
from test_db.prefs pr
left join test_db.shops sh
on sh.pref_id = pr.id;
-- 右外部結合(right joinの後のテーブルを元(左)にして右テーブルのデータを取得)
select pr.name "都道府県名", sh.name "店舗名"
from test_db.shops sh
right join test_db.prefs pr
on sh.pref_id = pr.id;
-- 複数のinner join
select
  sh.name "店舗名", pro.name "商品名", st.amount "在庫数"
from test_db.stocks st
inner join test_db.shops sh
on st.shop_id = sh.id
inner join test_db.products pro
on st.product_id = pro.id
order by sh.name;
