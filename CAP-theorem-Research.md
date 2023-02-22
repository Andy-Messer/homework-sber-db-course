# CAP

У Вас есть три поинта, выбрать можно только два:

> - (C)Consistency
> - (A)Availabitility
> - (P)Partition tolerance
  
---

## Согласно теореме CAP к какой части вы можете отнести СУБД:
 - DragonFly
 - ScyllaDB
 - ArenadataDB
  
---
  
| DB          | CAP-type |
| ----------- | -------- |
| DragonFly   | CA       |
| ScyllaDB    | AP       |
| ArenadataDB | CP       |

---

## Описание
### DragonFly
 - Цитата с [сайта](https://dragonflydb.io/): 
 - > "Dragonfly is architected to scale vertically on a single machine, saving teams the cost and complexity of managing a multi-node cluster. For in-memory datasets up to 1TB, Dragonfly offers the simplest and most reliable scale on the market." 
   - Одна машина, значит на Partition tolerance забиваем, потому что прямо сказали нет $\Rightarrow$ (-P).
  --- 
 - Опять же цитата с того же [сайта](https://dragonflydb.io/): 
 - > "High Throughput: Dragonfly's new in-memory engine, optimized for throughput, uses a thread-per-core architecture without locks to deliver stable and low latencies. By implementing true async interfaces, Dragonfly takes full advantage of the underlying hardware to deliver maximum performance. 
   - Основная мысль в (deliver stable and low latencies), задержек нет, а это хорошо $\Rightarrow$ (+A) 
---
 - Аналогично с [сайта](https://dragonflydb.io/):
 -  > Dragonfly utilizes an innovative hash table structure called dashtable to minimize memory overhead and tail latency. Dragonfly also utilizes bitpacking and denseSet techniques to compress the in-memory data, making it on average 30% more memory efficient than Redis. Lastly, Dragonfly uses consistent memory during the snapshotting, eliminating the need to over-provision memory that is typical with Redis.
      - uses consistent memory during the snapshotting... Это и есть ответ на наш вопрос $\Rightarrow$ (+C)

---------------------------------------------------------

### ScyllaDB
Идём на [сайт](https://docs.scylladb.com/stable/architecture/architecture-fault-tolerance.html)
 - Готовый ответ на сайте, они пожертвовали cosistency, в угоду network partition. (-C +P)
 - Повышенная отказоустойчивость даёт нам Availability (+A)

---
### ArenadataDB
Идём на [сайт](https://arenadata.tech/products/arenadata-db/) и читаем:
 - > Arenadata DB реализована на кластере из множества (от двух до сотен) серверов и равномерно распределяет нагрузку и данные между ними.
    - это значит есть Partition, т.к. есть исходный код GreenPlum. Еще с работы знаю понятие "партиционирования" для GP. Если опираться на эти идеи, то учитывая множество серверов. (+P)
    - У GP адский пинг при нагрузке, знаю на собственной шкуре (-A)
    - Поддержка целостности БД за счёт бэкапов - это выгодно, если все нестабильно, но до чёртиков медленно. Так мы получаем бан на доступность, следовательно (+С)
---
P.s. всем рекомендую делать связку c clickhouse и несколькими кластерами GP c дуплицированием баз, тогда ETL-процесс будет устойчив к нагрузке и можно будет не терять время, а обращаться к нужному кластеру, а хранить на клике только исторические данные. 

 - Тогда для комфортной аналитики используем дуплицированные базы данных с кластеров ГП
 - А когда нужна быстрый доступ идём в клик



