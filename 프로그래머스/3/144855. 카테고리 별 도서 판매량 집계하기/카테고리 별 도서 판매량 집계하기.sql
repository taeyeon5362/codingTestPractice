select a.category category, sum(b.sales) total_sales
from   book a,
       book_sales b
where  a.book_id = b.book_id
and    b.SALES_DATE between to_Date('2022-01-01','yyyy-mm-dd') and to_Date('2022-01-31','yyyy-mm-dd')
group by a.category
order by category