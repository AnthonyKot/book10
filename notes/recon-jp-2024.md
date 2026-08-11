# Japan 2024 reconciliation

Row numbers below are the original data-row numbers in `corpus/jp-2024.tsv`; the header is excluded.

## Summary

- Rows: 19 before -> 15 after.
- Era edits: 5 disputed `subject_era` values corrected to the work's represented subject or setting; 3 remain in the corpus and 2 are preserved in quarantine.
- Memorize edits: 5 disputed values changed from `excerpt` -> `no`; 4 corresponding false mandate claims in `note` were corrected.
- Quarantined rows: 4 unsupported rows moved out of the corpus and preserved below.

The renewed receipt search covered the saved MEXT standard and commentary and the Mitsumura and Tokyo Shoseki publisher TOCs, using Japanese titles and authors plus romanized and English variants. It found work-level support for 15 rows. This includes 長田弘's 「世界はうつくしいと」, which is printed in the Mitsumura PDF although omitted from that PDF's prose summary in `resources/jp-toc-ledger.txt`. The four quarantined exact works remain absent. Hits for 谷川俊太郎 name 「朝のリレー」 and 「未来へ」, not 「春に」; the saved TOCs name 夏目漱石 only with 『坊っちゃん』, not 『吾輩は猫である』. Same-author, different-work hits do not receipt a row.

## Systemic memorize ruling

`yes` or `excerpt` requires an explicit defining-document mandate to learn the named text, a named excerpt, or a stated quantity of texts by heart at this level. Grade 9 historically attentive reading, oral reading, quotation use, closed-book examination, implied quote-learning, and general recitation culture do not meet that rule. The commentary's `暗唱` reference describes prior elementary learning in its explanation of the Grade 8 oral-reading provision; it does not mandate Grade 9 memorization of a named work. No retained Japanese row has an explicit work-specific or quantity-based by-heart mandate, so all retained values are `no`.

## Change log

### Subject era

- Row 3, 松尾芭蕉, 「夏草」 from *The Narrow Road to the Deep North* — `subject_era`: `edo-period` -> `edo-period-journey/late-Heian-war-memory`; the passage represents the 1689 journey at Hiraizumi while mourning the destruction associated with Yoshitsune and the Northern Fujiwara, not merely the composition-era journey.
- Row 6, 山極寿一, *Beyond Fabricated 'Narratives'* — `subject_era`: `contemporary-primatology-society?` -> `19th-century-colonial-africa/wildlife-exploitation`; the essay treats the colonial "dark continent" narrative used to justify domination and the killing and capture of gorillas.
- Row 9, 小川洋子, *Encyclopedia Girl* — `subject_era`: `late-20th-century-japan?` -> `none/contemporary-grief-and-memory`; the story concerns grief and memory without anchoring its action to a historical era or wound.
- Row 16, 真壁仁, *The Pass* — `subject_era`: `showa-agrarian-life?` -> `none/personal-decision-and-parting`; the poem uses a mountain pass as a metaphor for decision and farewell, while the poet's wider agrarian reputation is biographical context. The corrected row was then quarantined for lack of a work-level receipt.
- Row 19, 谷川俊太郎, *In Spring* — `subject_era`: `postwar-youth-existential?` -> `none/adolescent-emotion`; the poem represents contradictory adolescent feeling, while postwar publication is composition context. The corrected row was then quarantined for lack of a work-level receipt.

### Memorize

- Row 3, 松尾芭蕉, 「夏草」 — `memorize`: `excerpt` -> `no`; Grade 9 requires historically attentive reading of classics, not learning this passage by heart.
- Row 3, 松尾芭蕉, 「夏草」 — `note`: `recitation of Haiku stanzas required per Course of Study Section 2-1(3)A` -> `no work-specific memorization mandate in the defining document`; the cited provision supports reading, not memorization.
- Row 4, 孔子, *Selections from the Analects* — `memorize`: `excerpt` -> `no`; the Grade 9 defining documents do not assign this work or a passage from it for memorization.
- Row 4, 孔子, *Selections from the Analects* — `note`: `recitation of "Manabi te toki ni kore wo narau" required per Course of Study Section 2-1(3)B` -> `no work-specific memorization mandate in the defining document`; quotation use is not a by-heart mandate.
- Row 5, 紀貫之ほか, *Heart of Waka* — `memorize`: `excerpt` -> `no`; the defining documents do not mandate memorizing these selections or a stated quantity from them.
- Row 5, 紀貫之ほか, *Heart of Waka* — `note`: `recitation of stanzas required per Course of Study Section 2-1(3)A` -> `no work-specific memorization mandate in the defining document`; oral reading and general recitation culture do not meet the rule.
- Row 10, 島崎藤村, *First Love* — `memorize`: `excerpt` -> `no`; no saved Grade 9 defining document requires this poem to be learned by heart.
- Row 10, 島崎藤村, *First Love* — `note`: `oral recitation in MEXT Grade 3 curriculum` -> `no work-specific memorization mandate in the defining document`; the curriculum does not attach a by-heart mandate to this poem.
- Row 11, 高村光太郎, *Lemon Elegy* — `memorize`: `excerpt` -> `no`; no saved Grade 9 defining document requires this poem to be learned by heart.

### Quarantine moves

- Row 16, 真壁仁, *The Pass* — `corpus -> quarantine`; absent under Japanese, romanized, and English author/title variants from every saved Japanese defining document.
- Row 17, 石牟礼道子, *Flower Hat* — `corpus -> quarantine`; absent under Japanese, romanized, and English author/title variants from every saved Japanese defining document.
- Row 18, 夏目漱石, *I Am a Cat* — `corpus -> quarantine`; the saved TOCs contain 夏目漱石 only for *Bocchan*, not this work.
- Row 19, 谷川俊太郎, *In Spring* — `corpus -> quarantine`; the saved TOCs contain the author with *Morning Relay* and *Toward the Future*, not this work.

## Quarantine

These rows preserve all pre-reconciliation fields except the two disputed `subject_era` values ruled above, which were corrected before quarantine.

```tsv
author	title	author_born	author_died	origin	genre	subject_era	exam_status	memorize	grade	source	doc_year	retrieved	note
真壁仁	「峠」 ("The Pass")	1907	1984	domestic	poem	none/personal-decision-and-parting	choice-list	no	9	https://www.sanseido-publ.co.jp/	2021	2026-08-11	Sanseido Grade 3 poetry selection
石牟礼道子	「花帽子」 ("Flower Hat")	1927	2018	domestic	essay	minamata-pollution-environmental-wound?	choice-list	no	9	https://www.sanseido-publ.co.jp/	2021	2026-08-11	Sanseido Grade 3 essay on memory and nature
夏目漱石	『吾輩は猫である』 ("I Am a Cat")	1867	1916	domestic	novel	meiji-modernization-satire?	choice-list	no	9	https://www.sanseido-publ.co.jp/	2021	2026-08-11	Sanseido Grade 3 classical modern novel selection
谷川俊太郎	「春に」 ("In Spring")	1931	2024	domestic	poem	none/adolescent-emotion	choice-list	no	9	https://www.kyoiku-shuppan.co.jp/	2021	2026-08-11	Kyoiku Shuppan Grade 3 poetry selection
```
