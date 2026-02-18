-- 코드를 입력하세요 
select book_id, to_Char(PUBLISHED_DATE,'YYYY-MM-DD')PUBLISHED_DATE
from   book
where  CATEGORY = '인문'
and    PUBLISHED_DATE between to_date('2021-01-01','YYYY-MM-DD') AND to_date('2021-12-31','YYYY-MM-DD')
order by PUBLISHED_DATE