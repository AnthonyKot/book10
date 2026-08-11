# China 2024 reconciliation

Row numbers below are the original data-row numbers in `corpus/cn-2024.tsv`; the header is excluded.

## Summary

- Rows: 72 before -> 69 after.
- Era edits: 8 disputed `subject_era` values corrected to the work's represented subject or setting.
- Memorize edits: 60 (`yes -> no` on 54 rows; `excerpt -> no` on 6 rows).
- Exam-status edits (second pass): 69 (`mandatory -> choice-list` on every row).
- Note-field corrections (second pass): 69 (60 Appendix 1 rows; 9 whole-book rows).
- Quarantined rows: 3 unsupported rows moved out of the corpus and preserved below.

Systemic memorize ruling: `yes` or `excerpt` requires an explicit defining-document mandate to learn the named text, a named excerpt, or a stated quantity of eligible texts by heart at this level. Appendix 1 says that compulsory-education students must memorize excellent poetry/prose in general, but it describes its 135 named pieces as recommendations, leaves the specific pieces to textbook editors and teachers, and states no required quantity for Grades 7–9. Therefore no individual Appendix 1 row meets the work-level rule. Closed-book examination, implied quotation learning, and general recitation culture likewise do not qualify.

The three flagged rows were rechecked against all saved China defining-document evidence: the MOE curriculum PDF and extraction, the full Appendix 1/2 OCR and page captures, and the saved MOE landing page. Searches used Chinese author/title forms and Latin variants including `Fabre`/`Souvenirs Entomologiques`, `Fu Lei`/`Family Letters`, and `Wu Jingzi`/`Wu Ching-tzu`/`The Scholars`. None appears, and no PEP textbook receipt is saved in `resources/`; the rows are therefore quarantined.

## Change log

### Subject era

- Row 4, Cao Cao, `subject_era`: `three-kingdoms-warlord? -> late-han-warlord-campaign` — the poem represents the sea viewed during Cao Cao's 207 Wuhuan campaign, before the conventionally dated Three Kingdoms period.
- Row 28, Yan Shu, `subject_era`: `northern-song-peace -> none/transience` — the lyric concerns spring's passing, recurrence, and personal transience, not Northern Song political conditions.
- Row 29, Wang Anshi, `subject_era`: `song-reform-ambition -> northern-song-political-aspiration` — the poem voices political confidence in 1050, before the New Policies began in 1069.
- Row 31, Su Shi, `subject_era`: `song-dynasty-midautumn -> none/family-separation` — Mid-Autumn is the occasion; separation from the speaker's brother is the represented burden.
- Row 32, Li Qingzhao, `subject_era`: `song-jin-war-displacement -> none/visionary-escape` — the undated dream lyric represents visionary escape and frustrated aspiration without identifying the Jin war or displacement.
- Row 39, Gong Zizhen, `subject_era`: `qing-dynasty-decline -> late-qing-reform/resignation` — the poem directly concerns his 1839 resignation and resolve to continue serving renewal.
- Row 49, Tao Qian, `subject_era`: `jin-dynasty-utopia -> qin-war-refuge/eastern-jin-utopia` — its Eastern Jin encounter reveals a community founded by ancestors fleeing Qin-era war and disorder.
- Row 69, Ai Qing, `subject_era`: `anti-japanese-resistance -> 1930s-1970s-rural-suffering/anti-japanese-war/post-mao-renewal` — the collection spans prewar rural suffering, resistance-era poetry, and later post-Mao work.

### Memorize

- Row 1, 《关雎》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity (systemic ruling above).
- Row 2, 《蒹葭》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 3, 《十五从军征》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 4, 《观沧海》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 5, 《饮酒》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 6, 《木兰辞》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 7, 《送杜少府之任蜀州》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 8, 《登幽州台歌》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 9, 《次北固山下》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 10, 《使至塞上》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 11, 《闻王昌龄左迁龙标遥有此寄》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 12, 《行路难》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 13, 《黄鹤楼》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 14, 《望岳》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 15, 《春望》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 16, 《茅屋为秋风所破歌》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 17, 《白雪歌送武判官归京》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 18, 《酬乐天扬州初逢席上见赠》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 19, 《卖炭翁》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 20, 《钱塘湖春行》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 21, 《雁门太守行》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 22, 《赤壁》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 23, 《泊秦淮》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 24, 《夜雨寄北》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 25, 《无题》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 26, 《相见欢》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 27, 《渔家傲》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 28, 《浣溪沙》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 29, 《登飞来峰》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 30, 《江城子》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 31, 《水调歌头》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 32, 《渔家傲》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 33, 《游山西村》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 34, 《南乡子》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 35, 《破阵子》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 36, 《过零丁洋》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 37, 《天净沙·秋思》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 38, 《山坡羊·潼关怀古》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 39, 《己亥杂诗》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 40, 《满江红》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 41, 《论语》十二章, `memorize`: `excerpt -> no` — Appendix 1 recommends the named selections but mandates neither these excerpts nor a Grade 7–9 quantity.
- Row 42, 《曹刿论战》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 43, 《孟子》三则, `memorize`: `excerpt -> no` — Appendix 1 recommends the named selections but mandates neither these excerpts nor a Grade 7–9 quantity.
- Row 44, 《庄子》一则, `memorize`: `excerpt -> no` — Appendix 1 recommends the named selection but mandates neither this excerpt nor a Grade 7–9 quantity.
- Row 45, 《礼记》一则, `memorize`: `excerpt -> no` — Appendix 1 recommends the named selection but mandates neither this excerpt nor a Grade 7–9 quantity.
- Row 46, 《吕氏春秋》一则, `memorize`: `excerpt -> no` — Appendix 1 recommends the named selection but mandates neither this excerpt nor a Grade 7–9 quantity.
- Row 47, 《邹忌讽齐王纳谏》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 48, 《出师表》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 49, 《桃花源记》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 50, 《答谢中书书》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 51, 《三峡》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 52, 《杂说（四）》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 53, 《陋室铭》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 54, 《小石潭记》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 55, 《岳阳楼记》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 56, 《醉翁亭记》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 57, 《爱莲说》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 58, 《记承天寺夜游》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.
- Row 59, 《送东阳马生序》, `memorize`: `excerpt -> no` — Appendix 1 recommends the named passage but mandates neither this excerpt nor a Grade 7–9 quantity.
- Row 60, 《湖心亭看雪》, `memorize`: `yes -> no` — Appendix 1 recommends the named pieces but mandates neither this text nor a Grade 7–9 quantity.

### Exam status (second pass)

Systemic ruling: `exam_status` records the force the defining document itself gives a named
work. Neither China appendix gives a named work a work-level mandate. Appendix 1 is headed
优秀诗文背诵推荐篇目 and its headnote calls the named pieces recommendations
(「这里仅推荐古诗文135篇（段）」), delegating the specific pieces to textbook editors and
language teachers (`resources/appendix1_full_ocr.txt:5-10`). Appendix 2 disclaims its own
catalogue: 「下列推荐的读物仅为举例」 (`resources/appendix1_full_ocr.txt:353-358`). The nine
whole-book rows' claim to compulsory textbook status rests on a PEP receipt that is not saved
in `resources/`, so it cannot carry `mandatory` either.

- Rows 1-60 (Appendix 1), `exam_status`: `mandatory -> choice-list` — named recommendations
  inside a general recitation requirement; the specific pieces are the editors' and teachers'
  choice.
- Rows 61-69 (whole-book shelf), `exam_status`: `mandatory -> choice-list` — Appendix 2 names
  them as examples only; no saved document makes any of them examinable.

`anthology-only` was considered and rejected for both groups: neither appendix is an anthology
that prints the texts, and Appendix 1 states the opposite (「在教科书中可作不同的安排，不必都编成课文」).

### Note fields (second pass)

- Rows 1-60, `note`: "Grade 7-9 compulsory memorization" -> "Grade 7-9 recitation
  recommendation; specific pieces left to editors and teachers" — the old wording contradicted
  the `memorize=no` coding this pass established and the headnote it rests on.
- Rows 61-69, `note`: "compulsory extended reading (名著导读); MOE 2022 Appendix 2" ->
  "名著导读 unit; grade placement unreceipted in resources/; named as an example in MOE 2022
  Appendix 2" — "compulsory" was unsourced, and the grade placements come from PEP textbook
  pages that are not saved. The `grade` values are retained as recorded but stand unreceipted;
  no essay claim may rest on them until a work-level textbook page is saved.

### Quarantine moves

- Row 66, Jean-Henri Fabre, 《昆虫记》: `corpus -> quarantine` — absent under Chinese and Latin author/title variants from every saved defining document; the claimed PEP receipt is not saved.
- Row 67, Fu Lei, 《傅雷家书》: `corpus -> quarantine` — absent under Chinese and Latin author/title variants from every saved defining document; the claimed PEP receipt is not saved.
- Row 71, Wu Jingzi, 《儒林外史》: `corpus -> quarantine` — absent under Chinese and Latin author/title variants from every saved defining document; the claimed PEP receipt is not saved.

## Quarantine

These rows are preserved verbatim from the pre-reconciliation TSV.

```tsv
author	title	author_born	author_died	origin	genre	subject_era	exam_status	memorize	grade	source	doc_year	retrieved	note
让-亨利·法布尔 (Jean-Henri Fabre)	"《昆虫记》 (""Souvenirs Entomologiques"")"	1823	1915	translated:french	essay	19th-c-natural-history	mandatory	no	8	http://www.pep.com.cn	2024	2026-08-10	PEP Tongbian Textbook Grade 8 S1 compulsory extended reading (名著导读); MOE 2022 Appendix 2
傅雷 (Fu Lei)	"《傅雷家书》 (""Fu Lei's Family Letters"")"	1908	1966	domestic	essay	1950s-1960s-intellectual-upbringing	mandatory	no	8	http://www.pep.com.cn	2024	2026-08-10	PEP Tongbian Textbook Grade 8 S2 compulsory extended reading (名著导读); MOE 2022 Appendix 2
吴敬梓 (Wu Jingzi)	"《儒林外史》 (""The Scholars"")"	1701	1754	domestic	novel	qing-dynasty-civil-service-satire	mandatory	no	9	http://www.pep.com.cn	2024	2026-08-10	PEP Tongbian Textbook Grade 9 S2 compulsory extended reading (名著导读); MOE 2022 Appendix 2
```
